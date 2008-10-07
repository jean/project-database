# -*- coding: utf-8 -*-
#
# File: Project.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Jean Jordaan <jean.jordaan@gmail.com>, Jurgen Blignaut
<jurgen.blignaut@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope import interface
from zope.interface import implements
import interfaces
from Products.ProjectDatabase.interfaces.IProjectDatabase import IProjectDatabase
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.ProjectDatabase.widgets.SelectedLinesField import SelectedLinesField
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn, CalendarColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
del Project
from Products.ProjectDatabase.content.FMIFolder import FMIFolder
from Products.ProjectDatabase.content.MonitoringAndEvaluation import MonitoringAndEvaluation
from Products.ProjectDatabase.content.ProjectGeneralInformation import ProjectGeneralInformation
from Products.ProjectDatabase.content.MilestoneFolder import MilestoneFolder
##/code-section module-header

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Project_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Project(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IProject, IProjectDatabase)

    meta_type = 'Project'
    _at_rename_after_creation = True

    schema = Project_schema

    ##code-section class-header #fill in your manual code here
    actions =  (
       {'action': "string:${object_url}/project_search",
        'category': "object_tabs",
        'id': 'search',
        'name': 'Project Search',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },
       {'action': "string:${object_url}/export_project_data",
        'category': "object_tabs",
        'id': 'export_project_data',
        'name': 'Export Project Data (csv)',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:0'
       },
       {'action': "string:${object_url}/reports_view",
        'category': "object_tabs",
        'id': 'reports',
        'name': 'reports',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },
       {'action': "string:${object_url}/export_view",
        'category': "object_tabs",
        'id': 'export',
        'name': 'export',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },
    )
    ##/code-section class-header

    # Methods

    security.declarePublic('getLeadAgencies')
    def getLeadAgencies(self):
        """
        """
        catalog = getToolByName(self, 'portal_catalog')
        proxies = catalog(portal_type='Agency')
        pl = [p.getObject().Title() for p in proxies]
        return ','.join(pl)

    security.declarePublic('getVocabulary')
    def getVocabulary(self):
        """
        """
        pv_tool = getToolByName(self, 'portal_vocabularies')
        vocab = pv_tool.getVocabularyByName(vocabName)
        return vocab.getDisplayList(vocab)

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container):
        """
        """
        if 'project_general_information' not in self.objectIds():
            self._setObject('project_general_information', ProjectGeneralInformation('project_general_information'))
            self['project_general_information'].edit(title='Project General Information')
            self['project_general_information'].reindexObject()
        self['project_general_information'].reindexObject()
        if 'fmi_folder' not in self.objectIds():
            self._setObject('fmi_folder', FMIFolder('fmi_folder'))
            self['fmi_folder'].edit(title='Financial Management Information')
        if 'monitoring_and_evaluation' not in self.objectIds():
            self._setObject('monitoring_and_evaluation', MonitoringAndEvaluation('monitoring_and_evaluation'))
            self['monitoring_and_evaluation'].edit(title='Monitoring and Evaluation')
        if 'milestonesfolder' not in self.objectIds():
            self._setObject('milestonesfolder', MilestoneFolder('milestonesfolder'))
            self['milestonesfolder'].edit(title='Milestones')
        if 'contacts-1' not in self.objectIds():
            from Products.mxmContacts.mxmContacts import mxmContacts
            self._setObject('contacts-1', mxmContacts('contacts-1'))
            self['contacts-1'].edit(title='Contacts')
        BaseFolder.manage_afterAdd(self, item, container)

    security.declarePublic('getProjectGeneralInformation')
    def getProjectGeneralInformation(self):
        """
        """
        return self['project_general_information']

    security.declarePublic('getAProject')
    def getAProject(self):
        """
        """
        return self

    # Manually created methods

    def contactsVocab(self):
        """
        """
        path = '/'.join(self.getAProject().getPhysicalPath()) + '/contacts-1'
        brains = self.portal_catalog(portal_type='mxmContactsPerson', path=path)
        pairs=[]
        pairs.append(("", "<no reference>"))
        for b in brains:
            pairs.append((b.getObject().UID(), b.getObject().Title()))
        return DisplayList(pairs)


registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
##/code-section module-footer



