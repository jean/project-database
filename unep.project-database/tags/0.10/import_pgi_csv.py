import csv
import logging
import transaction
from cStringIO import StringIO

from zope import event
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.event import ObjectInitializedEvent

# Some module wide defaults
DEBUG_LEVEL = 0
RESULT_LINES = []
# not self.plone_log?
LOGGER = logging.Logger('[PGI import]')

def writeMessage(msg):
    '''
    Write the message to response stream and plone log depending on the
    debug level.
    '''
    if DEBUG_LEVEL == 1:
        LOGGER.warn(msg)

def getListFromString(tmp_string):
    delimeter = tmp_string.find(',') > 0 and ',' or ' '
    raw_list = tmp_string.split(delimeter)
    raw_list = [value.strip() for value in raw_list]
    return raw_list

def getFieldNames(csv_file):
    '''
    '''
    field_names = []
    csv_reader = csv.reader(csv_file)
    line = csv_reader.next()
    try:
        if line and line.index('GEFid') > -1:
            field_names = line
    except ValueError:
        msg = 'CSV file does not contain necessary headings.'
        writeMessage(msg)
        raise AttributeError(msg)
    return field_names

def getDictReader(csv_file, site_props, coding):
    '''
    '''
    csv_buffer = csv_file.read()
    encoding = site_props.default_charset or 'utf-8'
    csv_string = StringIO(csv_buffer.decode(coding, 'replace').encode(encoding))
    field_names = getFieldNames(csv_string)
    if field_names:
        dict_reader = csv.DictReader(csv_string, field_names, dialect=csv.excel)
        return dict_reader
    return None

def checkUserRole(context):
    '''
    '''
    pms = getToolByName(context, 'portal_membership')
    member = pms.getAuthenticatedMember()
    if not member.has_role('Manager'):
        raise Unauthorized, "Only a manager may perform this action"

def createProject(context):
    '''
    Create a new project and fire the event to create the relevant
    contained objects.
    '''
    project_id = context.getNextProjectId()
    context.invokeFactory(id=project_id, type_name='Project')
    transaction.commit()
    new_project = context[project_id]
    event.notify(ObjectInitializedEvent(new_project))
    return new_project

def getField(field_name, parent):
    '''
    Get the field from the parent using the parent schema.
    Search the string for '.' which indicates that this field_name must be
    interpreted as [field_name].[column_name], because we are dealing with a
    datagridfield.
    '''
    if field_name.find('.') > -1:
        tmp_name = field_name.split('.')[0]
    else:
        tmp_name = field_name
    field = parent.schema.get(tmp_name, parent.schema.get(field_name.lower()))
    return field

def setFieldLines(field, pgi, field_value):
    raw_field_values = getListFromString(field_value)
    field_value_list = []
    for raw_value in raw_field_values:
        vocab_value = getVocabValue(field, pgi, raw_value)
        if vocab_value:
            field_value_list.append(vocab_value)
    mutator = getMutator(field, pgi)
    mutator(field_value_list)

def setField(field, pgi, field_value):
    vocab_value = getVocabValue(field, pgi, field_value)
    if vocab_value:
        mutator = getMutator(field, pgi)
        mutator(vocab_value)

def setDataGridField(field, pgi, field_value):
    raw_field_values = getListFromString(field_value)
    column_names = field.columns
    field_dict = {}
    for count in range(0, len(raw_field_values)):
        raw_value = raw_field_values[count]
        column_name = column_names[count]
        column = field.widget.columns.get(column_name)
        vocab = hasattr(column, 'vocabulary') and column.getVocabulary(pgi)
        if vocab:
            for key, value in vocab.items():
                if raw_value == key or raw_value == value:
                    field_dict[column_name] = key
            else:
                msg = 'Vocab:%s has no entry for:%s' % \
                      (field.getName(), raw_value)
        else:
            field_dict[column_name] = raw_value
    field.set(pgi, [field_dict])

def getVocabValue(field, parent, raw_value):
    vocab = field.vocabulary
    if vocab:
        for key, value in vocab.getDisplayList(parent).items():
            if raw_value == key or raw_value == value:
                return key
        else:
            msg = 'Vocab:%s has no entry for:%s' % (field.getName(), raw_value)
            writeMessage(msg)
            return None
    else:
        return raw_value

def getMutator(field, parent):
    mutator = field.getMutator(parent)
    if not mutator:
        msg = 'Cannot set field:%s, mutator not found!' % field.getName()
        writeMessage(msg)
    return mutator

def updatePGI(context, pgi_data):
    '''
    Update the PGI that was created during the project create step.
    '''
    pgi = context.get('project_general_info', None)
    if pgi:
        for field_name, field_value in pgi_data.items():
            field = getField(field_name, pgi)
            if field:
                if field.type == 'datagrid':
                    setDataGridField(field, pgi, field_value)
                elif field.type == 'lines':
                    setFieldLines(field, pgi, field_value)
                elif field.type == 'string':
                    setField(field, pgi, field_value)
            else:
                msg = 'Field %s was not found.' % field_name
                writeMessage(msg)
    else:
        msg = 'No PGI found! Aborting import.'
        writeMessage(msg)
        raise msg

def getPGIData(dict_reader, pc, projects_not_created):
    '''
    Return a list and removes those entries that have been imported
    before based on GEFid.
    We can assume GEFid is in the dict_reader, because we checked in a previous
    step of the process.
    '''
    pgi_data_list = []
    for line in dict_reader:
        gef_id = line.get('GEFid')
        if projectExists(gef_id, pc):
            projects_not_created += 1
        else:
            pgi_data_list.append(line)
    return pgi_data_list

def projectExists(gef_id, pc):
    '''
    Search for a project by GEFid.
    '''
    query = {'portal_type': 'Project',
             'getGEFid': gef_id}
    brains = pc(**query)
    if len(brains):
        return True
    return False

def run(self, csv_file=None, coding='latin-1', debug=1):
    '''
    Entry point into the import module.
    csv_file: the file object with all the project and pgi information.
    coding: default is latin-1.
    debug: regulates the level of verbosity in loggin.
    '''
    # Explicit check for user role 'manager'

    checkUserRole(self)
    DEBUG_LEVEL = debug
    RESULT_LINES = []

    portal_url         = getToolByName(self, 'portal_url')
    portal             = portal_url.getPortalObject()
    pc                 = getToolByName(self, 'portal_catalog')
    portal_properties  = self.portal_properties
    site_props         = portal_properties.site_properties
    project_databases  = getattr(portal, 'projectdatabases')

    projects_created     = 0
    projects_not_created = 0
    pgis_created         = 0
    pgis_not_created     = 0
    
    dict_reader = getDictReader(csv_file, site_props, coding)
    if dict_reader:
        pgi_data_list = getPGIData(dict_reader, pc, projects_not_created)
        for pgi_data in pgi_data_list:
            new_project = createProject(project_databases)
            if new_project:
                projects_created += 1
                transaction.commit()
                pgi = updatePGI(new_project, pgi_data)
                pgis_created += 1
        
        msg = ("[unep.import_fsp_from_csv] - 100.0% complete")
        writeMessage(msg)

        msg = "Projects: %s created; %s not created" \
              % (projects_created, projects_not_created)
        RESULT_LINES.append(msg)
        writeMessage(msg)

        msg = "PGI's: %s created; %s not created" \
              % (pgis_created, pgis_not_created)
        RESULT_LINES.append(msg)
        writeMessage(msg)
    else:
        RESULT_LINES = "An error occured. Please check the log files."

    return RESULT_LINES
