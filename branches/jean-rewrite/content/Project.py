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
from Products.FinanceFields.Money import Money
##/code-section module-header

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Project_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
idField = Project_schema['id']
idField.widget.visible = {'edit': 'hidden', 'view': 'visible'}
idField.widget.label = 'Internal Id'
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
    allowed_content_types = ['ATFolder', 'ProjectGeneralInfromation', 'Financials', 'MonitoringAndEvaluation', 'MilestoneFolder']
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
        pass

    security.declarePublic('getVocabulary')
    def getVocabulary(self):
        """
        """
        pass

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container):
        """
        """
        if 'financials' not in self.objectIds():
            self.invokeFactory('Financials', 'financials')
            self['financials'].setTitle('Financial Management Information')
#        if 'tranchedfolder' not in self.objectIds():
#            self.invokeFactory('TranchedFolder', 'tranchedfolder')
#            self['tranchedfolder'].setTitle('Tranched Projects')
#        if 'phasedfolder' not in self.objectIds():
#            self.invokeFactory('PhasedFolder', 'phasedfolder')
#            self['phasedfolder'].setTitle('Phased Projects')
#        if 'addonfolder' not in self.objectIds():
#            self.invokeFactory('AddOnFolder', 'addonfolder')
#            self['addonfolder'].setTitle('Add On Projects')
        if 'monitoring_and_evaluation' not in self.objectIds():
            self.invokeFactory('MonitoringAndEvaluation', 'monitoring_and_evaluation')
            self['monitoring_and_evaluation'].setTitle('Monitoring and Evaluation')
        if 'project_general_information' not in self.objectIds():
            self.invokeFactory('ProjectGeneralInformation', 'project_general_information')
            self['project_general_information'].setTitle('Project General Information')
        if 'milestonesfolder' not in self.objectIds():
            self.invokeFactory('MilestoneFolder', 'milestonesfolder')
            self['milestonesfolder'].setTitle('Milestones Folder')
        BaseFolder.manage_afterAdd(self, item, container)
#        if 'monitoring_and_evaluation' in self.objectIds():
    # Manually created methods

    security.declarePublic('getTotalGEFAllocation')
    def getTotalGEFAllocation(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getGEFProjectAllocation():
                total += fmi_obj.getGEFProjectAllocation()
        for sp_obj in subproject_objs:
            if sp_obj.getGEFProjectAllocation():
                total += sp_obj.getGEFProjectAllocation()
        return total

    security.declarePublic('getTotalUNEPAllocation')
    def getTotalUNEPAllocation(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getCashUNEPAllocation():
                total += fmi_obj.getCashUNEPAllocation()
        return total

    security.declarePublic('getTotalCofinancingPlanned')
    def getTotalCofinancingPlanned(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCofinCashPlanned():
                total += fmi_obj.getSumCofinCashPlanned()
            if fmi_obj.getSumCofinInKindPlanned():
                total += fmi_obj.getSumCofinInKindPlanned()
        for sp_obj in subproject_objs:
            if sp_obj.getSumCofinCashPlanned():
                total += sp_obj.getSumCofinCashPlanned()
            if sp_obj.getSumCofinInKindPlanned():
                total += sp_obj.getSumCofinInKindPlanned()
        return total

    security.declarePublic('getTotalCofinancingActual')
    def getTotalCofinancingActual(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCofinCashActual():
                total += fmi_obj.getSumCofinCashActual()
            if fmi_obj.getSumCofinInKindActual():
                total += fmi_obj.getSumCofinInKindActual()
        for sp_obj in subproject_objs:
            if sp_obj.getSumCofinCashActual():
                total += sp_obj.getSumCofinCashActual()
            if sp_obj.getSumCofinInKindActual():
                total += sp_obj.getSumCofinInKindActual()
        return total

    security.declarePublic('getTotalCashDisbursements')
    def getTotalCashDisbursements(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCashDisbursements():
                total += fmi_obj.getSumCashDisbursements()
        for sp_obj in subproject_objs:
            if sp_obj.getSumCashDisbursements():
                total += sp_obj.getSumCashDisbursements()
        return total

    security.declarePublic('getTotalIMISExpenditures')
    def getTotalIMISExpenditures(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumIMISExpenditures():
                total += fmi_obj.getSumIMISExpenditures()
        for sp_obj in subproject_objs:
            if sp_obj.getSumIMISExpenditures():
                total += sp_obj.getSumIMISExpenditures()
        return total

    security.declarePublic('getPDFAStatus')
    def getPDFAStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF A':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getPDFBStatus')
    def getPDFBStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF B':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getMSPStatus')
    def getMSPStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'MSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getFSPStatus')
    def getFSPStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'FSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """ Code copied from previous project; dunno what it means...
        """
        start_date_val = ''
        start_date_val_comp = ''
        r_str = ''

        for fobj in self.contentValues('Financials'):
            start_date_val = fobj.getStartDate()
            if start_date_val_comp == '':
                start_date_val_comp = fobj.getStartDate()
                r_str = fobj.Title()
            else:
                if start_date_val > start_date_val_comp:
                    start_date_val_comp = start_date_val
                    r_str = fobj.Title()
        return r_str

    security.declarePublic('validate_TranchedNumber')
    def validate_TranchedNumber(self, value):
        """
        """
        val=0
        try:
            val = int(value)
        except ValueError:
            return 'Value must be an integer'

        if self.REQUEST.get('Tranched') == 'Yes':
            if val <= 0:
                return 'Value must be bigger than zero if Tranched is Yes'
        if self.REQUEST.get('Tranched') == 'No':
            if val != 0:
                return 'Value must be zero if Tranched is No'
        return

    security.declarePublic('validate_PhasedNumber')
    def validate_PhasedNumber(self, value):
        """
        """
        val=0
        try:
            val = int(value)
        except ValueError:
            return 'Value must be an integer'

        if self.REQUEST.get('Phased') == 'Yes':
            if val <= 0:
                return 'Value must be bigger than zero if Phased is Yes'
        if self.REQUEST.get('Phased') == 'No':
            if val != 0:
                return 'Value must be zero if Phased is No'
        return

    security.declarePublic('getProjectTitle')
    def getProject(self):
        return self.aq_inner

    security.declarePublic('getCategoryVocab')
    def getCategoryVocab(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('Category')
        return vocab.getDisplayList(self)

    security.declarePublic('displayContentsTab')
    def displayContentsTab(self):
        """ Don't display the contents tab
        """
        return False



registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
def modify_fti(fti):
    for a in fti['actions']:
        if a['id'] in ('metadata', 'references'):
            a['visible'] = 0
    return fti

##/code-section module-footer



