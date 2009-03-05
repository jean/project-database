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



registerType(ProjectDatabase, PROJECTNAME)
# end of class ProjectDatabase

##code-section module-footer #fill in your manual code here
##/code-section module-footer



