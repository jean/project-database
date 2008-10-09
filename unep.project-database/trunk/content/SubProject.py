# -*- coding: utf-8 -*-
#
# File: SubProject.py
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
from Products.ProjectDatabase.content.CurrencyMixin import CurrencyMixin
from Products.ProjectDatabase.content.FinancialsMixin import FinancialsMixin
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.DataGridField import CalendarColumn
import ProjectGeneralInformation
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn, CalendarColumn
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
        widget=StringField._properties['widget'](
            label='Website',
            label_msgid='ProjectDatabase_label_Website',
            i18n_domain='ProjectDatabase',
        ),
    ),
    copied_fields['ProjectCoordinator'],

    copied_fields['LeadExecutingAgency'],

    StringField(
        name='OtherLeadExecutingAgency',
        widget=SelectionWidget(
            label="Other Project Executing Partners",
            label_msgid='ProjectDatabase_label_OtherLeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        relationship="SubProject_OtherLeadExecutingAgency",
    ),
    StringField(
        name='AccountCode',
        widget=StringField._properties['widget'](
            label="Account Code",
            label_msgid='ProjectDatabase_label_AccountCode',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='ProjectImplementationStatus',
        widget=DataGridField._properties['widget'](
            label="Project Implementation Status",
            columns={'status_date':CalendarColumn('Date'), 'status_remark':Column('Remark')},
            label_msgid='ProjectDatabase_label_ProjectImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        columns=('status_date','status_remark'),
    ),
    StringField(
        name='Website',
        widget=StringField._properties['widget'](
            description="Project Website Address",
            label='Website',
            label_msgid='ProjectDatabase_label_Website',
            description_msgid='ProjectDatabase_help_Website',
            i18n_domain='ProjectDatabase',
        ),
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

class SubProject(BaseFolder, CurrencyMixin, FinancialsMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.ISubProject)

    meta_type = 'SubProject'
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



