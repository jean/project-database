# -*- coding: utf-8 -*-
#
# File: Project.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Jean Jordaan <jean.jordaan@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
import zope
from Products.ProjectDatabase.interfaces.IProjectDatabase import IProjectDatabase
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.ProjectDatabase.widgets.SelectedLinesField import SelectedLinesField
from Products.CMFCore.utils import getToolByName
from Products.ProjectDatabase.content import permissions
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn
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

class Project(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IProjectDatabase)

    # This name appears in the 'add' box
    archetype_name = 'Project'

    meta_type = 'Project'
    portal_type = 'Project'
    allowed_content_types = ['ATFolder', 'MonitoringAndEvaluation', 'MilestoneFolder', 'ProjectGeneralInformation', 'FMIFolder']
    filter_content_types = 1
    global_allow = 1
    #content_icon = 'Project.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Project"
    typeDescMsgId = 'description_edit_project'


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

    _at_rename_after_creation = True

    schema = Project_schema

    ##code-section class-header #fill in your manual code here
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
    def getVocabulary(self, vocabName):
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


registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
##/code-section module-footer



