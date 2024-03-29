# -*- coding: utf-8 -*-
#
# File: SubProject.py
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
from Products.ProjectDatabase.CurrencyMixin import CurrencyMixin
from Products.ProjectDatabase.content.FinancialsMixin import FinancialsMixin
from Products.ProjectDatabase.interfaces.ISubProject import ISubProject
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.DataGridField import CalendarColumn
import ProjectGeneralInformation
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['SummaryDescription'] = ProjectGeneralInformation.schema['SummaryDescription'].copy()
copied_fields['Country'] = ProjectGeneralInformation.schema['Country'].copy()
copied_fields['Scope'] = ProjectGeneralInformation.schema['Scope'].copy()
copied_fields['Region'] = ProjectGeneralInformation.schema['Region'].copy()
copied_fields['ImplementationMode'] = ProjectGeneralInformation.schema['ImplementationMode'].copy()
copied_fields['Office'] = ProjectGeneralInformation.schema['Office'].copy()
copied_fields['ProjectCoordinator'] = ProjectGeneralInformation.schema['ProjectCoordinator'].copy()
copied_fields['ProjectCoordinator'].relationship = "SubProject_ProjectCoordinator"
copied_fields['LeadExecutingAgency'] = Financials.schema['LeadExecutingAgency'].copy()
copied_fields['LeadExecutingAgency'].dummy = "Financials.schema"
copied_fields['LeadExecutingAgency'].relationship = "SubProject_LeadExecutingAgency"
schema = Schema((

    copied_fields['SummaryDescription'],
        copied_fields['Country'],
        copied_fields['Scope'],
        copied_fields['Region'],
        copied_fields['ImplementationMode'],
        copied_fields['Office'],
        StringField(
        name='Website',
        dummy="Website",
        widget=StringWidget(
            label='Website',
            label_msgid='ProjectDatabase_label_Website',
            i18n_domain='ProjectDatabase',
        )
    ),

    copied_fields['ProjectCoordinator'],
        copied_fields['LeadExecutingAgency'],
        StringField(
        name='OtherLeadExecutingAgency',
        dummy="""Financials.schema
        LeadAgency""",
        widget=SelectionWidget(
            label="Other Project Executing Partners",
            label_msgid='ProjectDatabase_label_OtherLeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        relationship="SubProject_OtherLeadExecutingAgency"
    ),

    StringField(
        name='AccountCode',
        widget=StringWidget(
            label="Account Code",
            label_msgid='ProjectDatabase_label_AccountCode',
            i18n_domain='ProjectDatabase',
        )
    ),

    DataGridField(
        name='ProjectImplementationStatus',
        widget=DataGridField._properties['widget'](
            label="Project Implementation Status",
            columns={'status_date':CalendarColumn('Date'), 'status_remark':Column('Remark')},
            label_msgid='ProjectDatabase_label_ProjectImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        columns=('status_date','status_remark')
    ),

    StringField(
        name='Website',
        widget=StringWidget(
            description="Project Website Address",
            label='Website',
            label_msgid='ProjectDatabase_label_Website',
            description_msgid='ProjectDatabase_help_Website',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

SubProject_schema = BaseFolderSchema.copy() + \
    getattr(FinancialsMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class SubProject(BaseFolder, CurrencyMixin, FinancialsMixin):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),) + (getattr(CurrencyMixin,'__implements__',()),) + (getattr(FinancialsMixin,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(ISubProject)

    # This name appears in the 'add' box
    archetype_name = 'SubProject'

    meta_type = 'SubProject'
    portal_type = 'SubProject'
    allowed_content_types = ['ProjectImplementation'] + list(getattr(FinancialsMixin, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'SubProject.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "SubProject"
    typeDescMsgId = 'description_edit_subproject'

    _at_rename_after_creation = True

    schema = SubProject_schema

    ##code-section class-header #fill in your manual code here
    schema.moveField('FinanceCategory', after='title')
    schema.moveField('PMSNumber', after='FinanceCategory')
    schema.moveField('IMISNumber', after='PMSNumber')
    schema.moveField('GEFProjectAllocation', after='IMISNumber')
    schema.moveField('CofinancingCash', after='IMISNumber')
    schema.moveField('CofinancingInKind', after='CofinancingCash')
    schema.moveField('ApprovedUNEPBudget', after='CofinancingCash')
    schema.moveField('CashDisbursements', after='ApprovedUNEPBudget')
    schema.moveField('SumCashDisbursements', after='CashDisbursements')
    schema.moveField('IMISExpenditures', after='SumCashDisbursements')
    schema.moveField('Status', after='IMISExpenditures')
    schema.moveField('SumIMISExpenditures', after='Status')
    schema.moveField('PlannedDuration', after='SumIMISExpenditures')
    schema.moveField('InitialCompletionDate', after='PlannedDuration')
    schema.moveField('RevisedCompletionDate', after='InitialCompletionDate')
    schema.moveField('DelayReason', after='RevisedCompletionDate')
    schema.moveField('Reports', after='DelayReason')
    schema.moveField('LeadExecutingAgency', after='Reports')
    schema.moveField('OtherLeadExecutingAgency', after='LeadExecutingAgency')

    security.declarePublic('validate_GEFProjectAllocation')
    def validate_GEFProjectAllocation(self, value):
        """
        """
        if not value:
            value = self.getZeroMoneyInstance()
        fmi = self.aq_parent
        maxtotal = fmi.getGEFProjectAllocation()
        if maxtotal is None:
            maxtotal = self.getZeroMoneyInstance()

        total =  self.getZeroMoneyInstance()
        for subProject in fmi.contentValues():
            if subProject.getId() == self.getId():
                continue
            val = subProject.getGEFProjectAllocation()
            if val:
                total += val
        if maxtotal < total + value:
            return 'Total may not exceed allocated FMI value'
        return




    ##/code-section class-header

    # Methods

    # Manually created methods

    security.declarePublic('validate_GEFProjectAllocation')
    def validate_GEFProjectAllocation(self, value):
        """
        """
        if not value:
            value = self.getZeroMoneyInstance()
        fmi = self.aq_parent
        maxtotal = fmi.getGEFProjectAllocation()
        if maxtotal is None:
            maxtotal = self.getZeroMoneyInstance()

        total =  self.getZeroMoneyInstance()
        for subProject in fmi.contentValues():
            if subProject.getId() == self.getId():
                continue
            val = subProject.getGEFProjectAllocation()
            if val:
                total += val
        if maxtotal < total + value:
            return 'Total may not exceed allocated FMI value'
        return



registerType(SubProject, PROJECTNAME)
# end of class SubProject

##code-section module-footer #fill in your manual code here
##/code-section module-footer



