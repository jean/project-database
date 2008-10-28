# -*- coding: utf-8 -*-
#
# File: FinancialsMixin.py
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
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.DataGridField import CalendarColumn
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn, CalendarColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
import logging
logger = logging.getLogger('products/ProjectDatabase/content/FinancialsMixin.py')
##/code-section module-header

schema = Schema((

    StringField(
        name='FinanceCategory',
        widget=SelectionWidget(
            label="Finance Category",
            label_msgid='ProjectDatabase_label_FinanceCategory',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""FinanceCategory"""),
    ),
    StringField(
        name='TrusteeID',
        widget=StringField._properties['widget'](
            label="Trustee ID",
            label_msgid='ProjectDatabase_label_TrusteeID',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='PMSNumber',
        widget=StringField._properties['widget'](
            label="PMS Number",
            label_msgid='ProjectDatabase_label_PMSNumber',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='IMISNumber',
        widget=StringField._properties['widget'](
            label="IMIS Number",
            label_msgid='ProjectDatabase_label_IMISNumber',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='GEFProjectAllocation',
        widget=MoneyField._properties['widget'](
            label="Total GEF Allocation",
            description="Enter the total amount of GEF resources approved for this project",
            label_msgid='ProjectDatabase_label_GEFProjectAllocation',
            description_msgid='ProjectDatabase_help_GEFProjectAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='CofinancingCash',
        widget=DataGridField._properties['widget'](
            columns={ 'cofinancing_cash_source' : SelectColumn("Source", vocabulary="getDonorTypesVocabulary"), 'cofinancing_cash_donor_name' : Column("Name of donor"), 'cofinancing_cash_planned_amount' : Column("Planned Amount"), 'cofinancing_cash_actual_amount' : Column("Actual Amount") },
            label="Cofinancing: Cash",
            label_msgid='ProjectDatabase_label_CofinancingCash',
            i18n_domain='ProjectDatabase',
        ),
        columns=("cofinancing_cash_source", "cofinancing_cash_donor_name", "cofinancing_cash_planned_amount", "cofinancing_cash_actual_amount"),
    ),
    DataGridField(
        name='CofinancingInKind',
        widget=DataGridField._properties['widget'](
            columns={ 'cofinancing_inkind_source' : SelectColumn("Source", vocabulary="getDonorTypesVocabulary"), 'cofinancing_inkind_donor_name' : Column("Name of donor"), 'cofinancing_inkind_planned_amount' : Column("Planned Amount"), 'cofinancing_inkind_actual_amount' : Column("Actual Amount") },
            label="Cofinancing: In Kind",
            label_msgid='ProjectDatabase_label_CofinancingInKind',
            i18n_domain='ProjectDatabase',
        ),
        columns=("cofinancing_inkind_source", "cofinancing_inkind_donor_name", "cofinancing_inkind_planned_amount", "cofinancing_inkind_actual_amount"),
    ),
    ComputedField(
        name='SumCofinCashPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: Cash (Planned)",
            label_msgid='ProjectDatabase_label_SumCofinCashPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='SumCofinCashActual',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: Cash (Actual)",
            label_msgid='ProjectDatabase_label_SumCofinCashActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='SumCofinInKindPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: In Kind (Planned)",
            label_msgid='ProjectDatabase_label_SumCofinInKindPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='SumCofinInKindActual',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: In Kind (Actual)",
            label_msgid='ProjectDatabase_label_SumCofinInKindActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCostOfProjectStagePlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Project Stage (Planned)",
            label_msgid='ProjectDatabase_label_TotalCostOfProjectStagePlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCostOfProjectStageActual',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Project Stage (Actual)",
            label_msgid='ProjectDatabase_label_TotalCostOfProjectStageActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='ApprovedUNEPBudget',
        widget=MoneyField._properties['widget'](
            label="Approved UNEP Budget",
            description="Enter GEF amount to be directly used by UNEP",
            label_msgid='ProjectDatabase_label_ApprovedUNEPBudget',
            description_msgid='ProjectDatabase_help_ApprovedUNEPBudget',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='CashDisbursements',
        widget=DataGridField._properties['widget'](
            columns={ 'cash_disbursements_date' : CalendarColumn("Date"), 'cash_disbursements_amount' : Column("Amount"), 'cash_disbursements_imis_rcpt_number' : Column("IMIS RCPT Number") },
            label="Cash Disbursements",
            label_msgid='ProjectDatabase_label_CashDisbursements',
            i18n_domain='ProjectDatabase',
        ),
        columns=("cash_disbursements_date", "cash_disbursements_amount", "cash_disbursements_imis_rcpt_number"),
    ),
    ComputedField(
        name='SumCashDisbursements',
        widget=ComputedField._properties['widget'](
            label="Total Cash Disbursements",
            label_msgid='ProjectDatabase_label_SumCashDisbursements',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='IMISExpenditures',
        widget=DataGridField._properties['widget'](
            columns={ 'imis_expenditure_year' : CalendarColumn("Date"), 'imis_expenditure_amount' : Column("Amount") },
            label="Yearly Expenditures",
            label_msgid='ProjectDatabase_label_IMISExpenditures',
            i18n_domain='ProjectDatabase',
        ),
        columns=("imis_expenditure_year", "imis_expenditure_amount"),
    ),
    ComputedField(
        name='SumIMISExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total Yearly Expenditures",
            label_msgid='ProjectDatabase_label_SumIMISExpenditures',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='Status',
        widget=SelectionWidget(
            label="Project Status",
            label_msgid='ProjectDatabase_label_Status',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Status"""),
    ),
    IntegerField(
        name='PlannedDuration',
        widget=IntegerField._properties['widget'](
            label="Planned Duration",
            description="The number of months",
            label_msgid='ProjectDatabase_label_PlannedDuration',
            description_msgid='ProjectDatabase_help_PlannedDuration',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='InitialCompletionDate',
        widget=CalendarWidget(
            label="Initial Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_InitialCompletionDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='RevisedCompletionDate',
        widget=CalendarWidget(
            label="Revised Completion Date",
            description="As per last revision",
            show_hm=False,
            label_msgid='ProjectDatabase_label_RevisedCompletionDate',
            description_msgid='ProjectDatabase_help_RevisedCompletionDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='DelayReason',
        widget=TextAreaWidget(
            label="Reasons for delay",
            label_msgid='ProjectDatabase_label_DelayReason',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='Reports',
        widget=DataGridField._properties['widget'](
            columns={ 'report_type' : SelectColumn("Report Type", vocabulary="getReportTypesVocabulary"), 'report_period' : Column("Report Period"), 'report_received_date' : CalendarColumn("Report Received Date") },
            label="Reports",
            label_msgid='ProjectDatabase_label_Reports',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ReportType"""),
        columns=("report_type", "report_period", "report_received_date"),
    ),
    TextField(
        name='FinancialStatusRemarks',
        widget=TextAreaWidget(
            label="Project Financial Status - Remarks",
            label_msgid='ProjectDatabase_label_FinancialStatusRemarks',
            i18n_domain='ProjectDatabase',
        ),
    ),
    LinesField(
        name='DonorTypes',
        widget=MultiSelectionWidget(
            label="Donor Type",
            label_msgid='ProjectDatabase_label_DonorTypes',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""DonorType"""),
    ),
    MoneyField(
        name='ImplementingAgencyFee',
        widget=MoneyField._properties['widget'](
            label="Implementing Agency Fee",
            description="Enter the Full Implementing Agency Fee",
            label_msgid='ProjectDatabase_label_ImplementingAgencyFee',
            description_msgid='ProjectDatabase_help_ImplementingAgencyFee',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='UNEPImplentingAgencyFee',
        widget=MoneyField._properties['widget'](
            label="UNEP Implementing Agency Fee",
            label_msgid='ProjectDatabase_label_UNEPImplentingAgencyFee',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='ProjectRevision',
        widget=DataGridField._properties['widget'](
            columns={"revision_number":Column("Revision Number"), "revision_type":SelectColumn("Revision Type", vocabulary="getRevisionTypeVocabulary"),"revision_date":CalendarColumn("Revision Date")},
            label="Project Revision",
            label_msgid='ProjectDatabase_label_ProjectRevision',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectRevisionType"""),
        columns=("revision_number", "revision_type","revision_date"),
    ),
    MoneyField(
        name='RevisedAllocationToUNEP',
        widget=MoneyField._properties['widget'](
            label="Revised allocation to UNEP",
            description="Revised amount after Project Council or CEO approval",
            label_msgid='ProjectDatabase_label_RevisedAllocationToUNEP',
            description_msgid='ProjectDatabase_help_RevisedAllocationToUNEP',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='CommittedGEFGrant',
        widget=MoneyField._properties['widget'](
            label="Committed GEF Grant",
            description="Project budget in the internalized project document",
            label_msgid='ProjectDatabase_label_CommittedGEFGrant',
            description_msgid='ProjectDatabase_help_CommittedGEFGrant',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='Difference',
        widget=ComputedField._properties['widget'](
            label='Difference',
            label_msgid='ProjectDatabase_label_Difference',
            i18n_domain='ProjectDatabase',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

FinancialsMixin_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
FinancialsMixin_schema['GEFProjectAllocation'].widget.size = 15
FinancialsMixin_schema['ApprovedUNEPBudget'].widget.size = 15
FinancialsMixin_schema['ApprovedUNEPBudget'].widget.size = 15
FinancialsMixin_schema['ImplementingAgencyFee'].widget.size = 15
FinancialsMixin_schema['UNEPImplentingAgencyFee'].widget.size = 15
FinancialsMixin_schema['UNEPImplentingAgencyFee'].widget.label = 'UNEP Implementing Agency Fee'
##/code-section after-schema

class FinancialsMixin(BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IFinancialsMixin)

    meta_type = 'FinancialsMixin'
    _at_rename_after_creation = True

    schema = FinancialsMixin_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getDonorTypesVocabulary')
    def getDonorTypesVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('DonorType')
        return vocab.getDisplayList(self)

    security.declarePublic('getReportTypesVocabulary')
    def getReportTypesVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('ReportType')
        return vocab.getDisplayList(self)

    security.declarePublic('computeDataGridAmount')
    def computeDataGridAmount(self,column):
        """
        """
        properties = getToolByName(self, 'portal_properties')
        default_currency = properties.financial_properties.default_currency
        amount = Money(0, default_currency)
        for v in column:
            if v:
                amount += v
        return amount

    security.declarePublic('getMoneyFieldDefault')
    def getMoneyFieldDefault(self):
        """
        """
        return self.getZeroMoneyInstance()

    security.declarePublic('getSumCofinCashPlanned')
    def getSumCofinCashPlanned(self):
        """
        """
        cash_values = self.getCofinancingCash()
        return self.computeDataGridAmount([v['cofinancing_cash_planned_amount'] for v in cash_values if v['cofinancing_cash_planned_amount']])

    security.declarePublic('getSumCofinActual')
    def getSumCofinActual(self):
        """
        """
        pass

    security.declarePublic('getSumCofinInKindPlanned')
    def getSumCofinInKindPlanned(self):
        """
        """
        cash_values = self.getCofinancingInKind()
        return self.computeDataGridAmount([v['cofinancing_inkind_planned_amount'] for v in cash_values if v['cofinancing_inkind_planned_amount']])

    security.declarePublic('getSumCofinInKindActual')
    def getSumCofinInKindActual(self):
        """
        """
        cash_values = self.getCofinancingInKind()
        return self.computeDataGridAmount([v['cofinancing_inkind_actual_amount'] for v in cash_values if v['cofinancing_inkind_actual_amount']])

    security.declarePublic('getSumCashDisbursements')
    def getSumCashDisbursements(self):
        """
        """
        cash_values = self.getCashDisbursements()
        return self.computeDataGridAmount([v['cash_disbursements_amount'] for v in cash_values if v['cash_disbursements_amount']])

    security.declarePublic('getSumIMISExpenditures')
    def getSumIMISExpenditures(self):
        """
        """
        cash_values = self.getIMISExpenditures()
        return self.computeDataGridAmount([v['imis_expenditure_amount'] for v in cash_values if v['imis_expenditure_amount']])

    security.declarePublic('getTotalCostOfProjectStagePlanned')
    def getTotalCostOfProjectStagePlanned(self):
        """
        """
        #projObj = self.getProject()
        if self.portal_type == 'Financials':
            total = self.getCashUNEPAllocation()
            if self.getSumCofinCashPlanned():
                total += self.getSumCofinCashPlanned()
            if self.getSumCofinInKindPlanned():
                total += self.getSumCofinInKindPlanned()
            return total
        elif self.portal_type == 'SubProject':
            total = self.getZeroMoneyInstance()
            if self.getSumCofinCashPlanned():
                total += self.getSumCofinCashPlanned()
            if self.getSumCofinInKindPlanned():
                total += self.getSumCofinInKindPlanned()

        else:
            return self.getZeroMoneyInstance()

    security.declarePublic('getTotalCostOfProjectStageActual')
    def getTotalCostOfProjectStageActual(self):
        """
        """
        if self.portal_type == 'Financials':
            total = self.getCashUNEPAllocation()
            if self.getSupplementaryUNEPAllocation():
                total += self.getSupplementaryUNEPAllocation()
            if self.getSumCofinCashActual():
                total += self.getSumCofinCashActual()
            if self.getSumCofinInKindActual():
                total += self.getSumCofinInKindActual()
            return total
        elif self.portal_type == 'SubProject':
            total = self.getZeroMoneyInstance()
            if self.getSumCofinCashActual():
                total += self.getSumCofinCashActual()
            if self.getSumCofinInKindActual():
                total += self.getSumCofinInKindActual()
            return total
        else:
            return self.getZeroMoneyInstance()

    security.declarePublic('getRevisionTypeVocabulary')
    def getRevisionTypeVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('ProjectRevisionType')
        return vocab.getDisplayList(self)

    security.declarePublic('getDifference')
    def getDifference(self):
        """ calculate the difference between the committed and allocated GEF grant
        """
        # TODO: get working properly
        # import pdb; pdb.set_trace()
        revAllocUNEP = self.getField('RevisedAllocationToUNEP')
        committedGEFgrant = self.getField('CommittedGEFGrant')
        try:
            return revAllocUNEP - committedGEFgrant
        except TypeError:
            logger.error('Could not retrieve revisedAllocationToUNEP or committedGEFGrant value')
            return 0

    # Manually created methods

    security.declarePublic('validate_CashDisbursements')
    def validate_CashDisbursements(self, value):
        """
        """
        request = self.REQUEST
        total_cost = self.computeDataGridAmount([v['cash_disbursements_amount'] for v in value if v['cash_disbursements_amount']])
        total = self.getZeroMoneyInstance()
        if request.get('GEFTrustFund'):
            total = total + request.get('GEFTrustFund')
        if request.get('LDCFundAllocation'):
            total = total + request.get('LDCFundAllocation')
        if request.get('SCCFAllocation'):
            total = total + request.get('SCCFAllocation')
        if request.get('StrategicPartnership'):
            total = total + request.get('StrategicPartnership')
        if request.get('AdaptationTrustFund'):
            total = total + request.get('AdaptationTrustFund')
        if request.get('SupplementaryUNEPAllocation'):
            total = total + request.get('SupplementaryUNEPAllocation')

        if total_cost > total:
            return 'Total disbursements cannot exceed total allocation'
        return

    security.declarePublic('getSumCofinCashActual')
    def getSumCofinCashActual(self):
        """
        """
        cash_values = self.getCofinancingCash()
        return self.computeDataGridAmount([v['cofinancing_cash_actual_amount'] for v in cash_values if v['cofinancing_cash_actual_amount']])



# end of class FinancialsMixin

##code-section module-footer #fill in your manual code here
##/code-section module-footer



