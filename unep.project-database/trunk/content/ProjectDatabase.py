# -*- coding: utf-8 -*-
#
# File: ProjectDatabase.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mikejmets@gmail.com>, Jurgen Blignaut
<jurgen.blignaut@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
from threading import Lock
from DateTime import DateTime
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProjectDatabase_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ProjectDatabase(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProjectDatabase)

    meta_type = 'ProjectDatabase'
    _at_rename_after_creation = True

    schema = ProjectDatabase_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def getNextProjectId(self):
        """
        Lock this method so only one thread can access it at a time.
        Search the project database for the highest numbered project.
        Increment that number by one.
        Check if the new id exists and increment if it does.
        Release the lock in all cases.
        """
        lock = Lock()
        try:
            pc = getToolByName(self, 'portal_catalog')

            lock.acquire()
            projectBrains = \
                pc.unrestrictedSearchResults(
                    portal_type='Project',
                    sort_on='created',
                    sort_order='reverse')
            if len(projectBrains) == 0:
                childrenCount = 0
            else:
                childrenCount = int(projectBrains[0].getId)
            newId = '%05d' % (childrenCount + 1)
            # In case some projects were deleted and we try to use
            # an existing id.
            while newId in self.keys():
                childrenCount += 1
                newId = '%05d' % (childrenCount + 1)
            return newId
        finally:
            lock.release()

    security.declarePublic('getStaffForProjects')
    def getStaffForProjects(self):
        projects = self.objectValues(spec='Project')
        staff = []
        for project in projects:
            staff.extend(project.getProjectStaff())
        if len(staff) > 0:
              staff.sort()
              return staff

    security.declarePublic('getProjectsByExecutingAgency')
    def getProjectsByExecutingAgency(self, executing_agency):
        projects = self.objectValues(spec='Project')
        results = []
        for project in projects:
            if executing_agency in project.getExecutingAgencies():
                results.append(project)
        return results

    def hasExecutingAgencyHighRiskRatingInTwoYears(self, agencylist):
        projects = []
        for agency in agencylist:
            agencyprojects = self.getProjectsByExecutingAgency(agency)
            projects.extend([prj for prj in agencyprojects if prj not in projects])
        for project in projects:
            mofu = project.fmi_folder.getMainFinanceObject()
            if mofu:
                for rating, date in mofu.getEARiskRatingsAndDates():
                    if rating in ['H', 'S'] and (DateTime() - date) < 730:
                        return True
        return False



registerType(ProjectDatabase, PROJECTNAME)
# end of class ProjectDatabase

##code-section module-footer #fill in your manual code here
import csv
import logging
import transaction
from cStringIO import StringIO
from DateTime import DateTime

from zope import event
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.event import ObjectInitializedEvent
from Products.DataGridField.MoneyColumn import MoneyColumn
from Products.FinanceFields.Money import Money

class CSVImporter:
    ALL_FEEDBACK =1
    SOME_FEEDBACK = 2
    NO_FEEDBACK = 3

    def __init__(self, context, csvfile, coding, debug):
        self._context            = context
        self._request            = self._context.REQUEST
        self._portal_url         = getToolByName(self._context, 'portal_url')
        self._portal             = self._portal_url.getPortalObject()
        self._pc                 = getToolByName(self._context, 'portal_catalog')
        self._portal_properties  = self._portal.portal_properties
        self._site_props         = self._portal_properties.site_properties
        self._projectdatabases  = getattr(self._portal, 'projectdatabases')

        self._csvfile = csvfile
        self._required_fields = ['GEFid',]
        self._coding = coding
        self.setDebugLevel(debug)
        self._result_lines = []
        self._LOGGER = logging.getLogger('[CSVImporter]')
        self._error_file_name = '%s_errors.log' % self._csvfile.filename
        self._errors = []
        self.writeMessage('Done setup')

    def setDebugLevel(self, debug):
        if isinstance(debug, str): 
            debug_level = int(debug)
        else:
            debug_level = debug
        debug_dict = {1: self.ALL_FEEDBACK,
                      2: self.SOME_FEEDBACK,
                      3: self.NO_FEEDBACK, }
        self._debug = debug_dict.get(debug_level, self.ALL_FEEDBACK)

    def writeMessage(self, msg, debug_level=None):
        '''
        Write the message to response stream and plone log depending on the
        debug level.
        '''
        if debug_level:
            local_debug_level = debug_level
        else:
            local_debug_level = self._debug

        if local_debug_level == self.ALL_FEEDBACK:
            self._LOGGER.warn(msg)
            self._errors.append('%s\n' % msg)

    def getListFromString(self, tmp_string):
        raw_list = []
        delimeter = tmp_string.find(',') > -1 and ',' or None
        if delimeter:
            raw_list = tmp_string.split(delimeter)
            raw_list = [value.strip() for value in raw_list]
        else:
            raw_list.append(tmp_string.strip())
        return raw_list

    def getDictReader(self):
        '''
        '''
        csv_buffer = self._csvfile.read()
        encoding = self._site_props.default_charset or 'utf-8'
        csv_io_buffer = StringIO(csv_buffer.decode(self._coding, 'replace' \
                                               ).encode(encoding))
        field_names = self.getFieldNamesFromDict(csv_io_buffer)
        if field_names:
            dict_reader = csv.DictReader(csv_io_buffer,
                                         field_names,
                                         dialect=csv.excel)
            return dict_reader
        return None

    def getFieldNamesFromDict(self, csv_io_buffer):
        '''
        Use the csv_reader to get get the normal field names from the first
        line in the csv file.
        '''
        csv_reader = csv.reader(csv_io_buffer)
        line = csv_reader.next()
        if self.existsRequiredFields(line):
            return line
        else:
            msg = 'CSV file does not contain necessary headings: %s' % \
                  self._required_fields
            self.writeMessage(msg)
            raise AttributeError(msg)

    def existsRequiredFields(self, line):
        for name in self._required_fields:
            if line and line.index(name) > -1:
                return True
            else:
                return False

    def checkUserRole(self, context):
        '''
        '''
        pms = getToolByName(context, 'portal_membership')
        member = pms.getAuthenticatedMember()
        if not member.has_role('Manager'):
            raise Unauthorized, "Only a manager may perform this action"

    def splitHeader(self, names_list):
        tmp_list = names_list.split(':')
        if len(tmp_list) > 1:
            return (tmp_list[0], self.getListFromString(tmp_list[1]))
             
        return (tmp_list[0], None)

    def getField(self, field_name, parent):
        '''
        Get the field from the parent using the parent schema.
        Search the string for '.' which indicates that this field_name must be
        interpreted as [field_name].[column_name], because we are dealing with a
        datagridfield.
        '''
        if field_name.find(':') > -1:
            tmp_name = field_name.split(':')[0]
        else:
            tmp_name = field_name
        field = parent.schema.get(tmp_name,
                parent.schema.get(field_name.lower()))
        return field

    def getFieldValue(self, field, context):
        # TODO: Implement fetch of current values in a datagrid, so we append
        #       instead of overwrite
        if field.multiValued:
            accessor = field.getAccessor(context)
            if accessor:
                return list(accessor())
            return []
        return None

    def setFieldLines(self, field, context, field_value):
        raw_field_values = self.getListFromString(field_value)
        #field_value_list = self.getFieldValue(field, context)
        field_value_list = []
        for raw_value in raw_field_values:
            value = self.getValue(field, context, raw_value)
            if value:
                field_value_list.append(value)
        mutator = self.getMutator(field, context)
        mutator(field_value_list)

    def setField(self, field, context, field_value):
        value = self.getValue(field, context, field_value)
        if value:
            mutator = self.getMutator(field, context)
            mutator(value)

    def setMoneyField(self, field, context, field_value):
        field.set(context, Money(field_value, 'USD'))

    def setDataGridField(self,
            field, context, field_name, column_names, field_value):
        """
        Set the values of a datagrid field.
        """
        raw_field_values = self.getListFromString(field_value)
        field_dict = {}
        for count in range(0, len(raw_field_values)):
            raw_value = raw_field_values[count]
            column_name = column_names[count]
            column = field.widget.columns.get(column_name)
            if isinstance(column, MoneyColumn):
                raw_value = raw_value.strip() and raw_value or '0'
                field_dict[column_name] = Money(raw_value, 'USD')
            elif isinstance(column, CalendarColumn):
                field_dict[column_name] = DateTime(raw_value)
            else:
                vocab = hasattr(column, 'vocabulary') and \
                        column.getVocabulary(context)
                if vocab:
                    field_dict[column_name] = self.getVocabValue(
                        context, vocab, raw_value)
                else:
                    field_dict[column_name] = raw_value
        row_values = [v for v in field.getRaw(context)]
        row_values.append(field_dict)
        field.set(context, row_values)

    def getValue(self, field, parent, raw_value):
        vocab = field.vocabulary
        if vocab:
            return self.getVocabValue(parent, vocab, raw_value) or None
        else:
            return raw_value
        
    def getVocabValue(self, parent, vocab, raw_value):
        """
        Search through the vocab keys and values to match the raw_value
        passed it and return the associated key.

        ARG! The isinstance check...
        Just in case vocab is actually a displayList... like when you ask a
        datagrid column for it's vocab.
        """
        if not isinstance(vocab, DisplayList):
            vocab = vocab.getDisplayList(parent)
        raw_value = raw_value.lower()
        for key, value in vocab.items():
            if raw_value == key.lower() or raw_value == value.lower():
                return key
        else:
            msg = 'Vocab in:%s has no entry for:%s' % (parent, raw_value)
            self.writeMessage(msg)
            return None
        return None

    def getMutator(self, field, parent):
        mutator = field.getMutator(parent)
        if not mutator:
            msg = 'Cannot set field:%s, mutator not found!' % field.getName()
            self.writeMessage(msg)
        return mutator

    def getProjectByGefId(self, gef_id):
        query = {'portal_type': 'Project',
                 'getGEFid': gef_id}
        brains = self._pc(**query)
        if len(brains) > 0:
            return brains[0].getObject()
        return None

    def updateFields(self, context, data_dict):
        for field_header, field_value in data_dict.items():
            try:
                field_name, column_names = self.splitHeader(field_header)
                field = self.getField(field_name, context)
            except AttributeError:
                raise 'Error'
            if field:
                if field.type == 'datagrid':
                    # datagrids are imported from a file with the field name
                    # and field column names in the same csv column, e.g.
                    # ProjectImplementationStatus:FiscalYear, Narrative
                    self.setDataGridField(field=field,
                                          context=context,
                                          field_name=field_name,
                                          column_names=column_names,
                                          field_value=field_value)
                elif field.type == 'lines':
                    self.setFieldLines(field, context, field_value)
                elif field.type == 'Money':
                    self.setMoneyField(field, context, field_value)
                elif field.type in ['string', 'text']:
                    self.setField(field, context, field_value)
                else:
                    msg = 'Field type %s not supported.' % field.type
                    self.writeMessage(msg)
            else:
                msg = 'Field %s was not found.' % field_name
                self.writeMessage(msg)

    def writeProgressTemplate(self, row_count):
        if self._request is not None:
            progress_template = self._context.uc_import_progress(
                                REQUEST=self._request)
            writer = self._request.RESPONSE
            writer.write(progress_template.encode('latin-1'))
            writer.write(
                '''<input style="display: none;"
                   id="inputTotal" value="%s">''' % row_count)

    def writeProgressLine(self, count):
        if self._request is not None:
            writer = self._request.RESPONSE
            writer.write(
                '''<input style="display: none;"
                   name="inputProgress" value="%s">''' % count)

    def writeRedirectUrl(self):
        if self._request is not None:
            # This trick is needed since previous calls to RESPONSE.write
            # trashes a normal redirect
            url = '<script>document.location.href="%s/@@unep.import-form' % \
                  self._portal.absolute_url()
            msg = '<br/>'.join(self._result_lines) 
            params = '?portal_status_message=%s"</script>' % msg
            self._request.RESPONSE.write('%s%s' % (url, params))

    def __del__(self):
        """
        Write all error messages to the error log file.
        """
        if self._debug == self.ALL_FEEDBACK:
            error_file = open(self._error_file_name, 'wb')
            error_file.writelines(self._errors)
            error_file.close()

##/code-section module-footer
