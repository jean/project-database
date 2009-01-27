# -*- coding: utf-8 -*-
#
# File: Financials.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.1
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
from Products.ProjectDatabase.content.CurrencyMixin import CurrencyMixin
from Products.ProjectDatabase.content.FinancialsMixin import FinancialsMixin
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.ProjectDatabase.widgets.SelectedLinesField import SelectedLinesField
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn, CalendarColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
import permissions
##/code-section module-header

schema = Schema((

    StringField(
        name='GEFid',
        widget=StringField._properties['widget'](
            label="GEF ID",
            description="Enter the 5 digit GEF ID",
            label_msgid='ProjectDatabase_label_GEFid',
            description_msgid='ProjectDatabase_help_GEFid',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='FinanceCategory',
        widget=SelectionWidget(
            label="Finance Object",
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
    StringField(
        name='LeadExecutingAgency',
        widget=StringField._properties['widget'](
            label="Lead Executing Agency",
            label_msgid='ProjectDatabase_label_LeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='OtherLeadExecutingAgency',
        widget=SelectionWidget(
            label="Other Project Executing Partners",
            label_msgid='ProjectDatabase_label_OtherLeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""LeadAgency"""),
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
    TextField(
        name='FinancialStatusRemarks',
        widget=TextAreaWidget(
            label="Project Financial Status - Remarks",
            label_msgid='ProjectDatabase_label_FinancialStatusRemarks',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='FinanceObjectAmount',
        widget=DataGridField._properties['widget'](
            columns={ 'trust_fund' : SelectColumn("Trust Fund"), 'unep_allocation' : Column("UNEP Allocation"), 'other_ia_allocation' : Column("Other IA Alloaction"), 'unep_fee' : Column("UNEP Fee"), 'other_ia_fee' : Column("Other IA Fee") },
            label="Finance Object Amount",
            label_msgid='ProjectDatabase_label_FinanceObjectAmount',
            i18n_domain='ProjectDatabase',
        ),
        columns=("trust_fund", "unep_allocation", "other_ia_allocation", "unep_fee", "other_ia_fee"),
    ),
    ComputedField(
        name='TotalFinanceObjectGrant',
        widget=ComputedField._properties['widget'](
            label='Totalfinanceobjectgrant',
            label_msgid='ProjectDatabase_label_TotalFinanceObjectGrant',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalFee',
        widget=ComputedField._properties['widget'](
            label='Totalfee',
            label_msgid='ProjectDatabase_label_TotalFee',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalFinanceObject',
        widget=ComputedField._properties['widget'](
            label='Totalfinanceobject',
            label_msgid='ProjectDatabase_label_TotalFinanceObject',
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
        name='TotalCostOfFinanceObjectPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Finance Object (Planned)",
            label_msgid='ProjectDatabase_label_TotalCostOfFinanceObjectPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCostOfFinanceObjectActual',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Finance Object (Actual)",
            label_msgid='ProjectDatabase_label_TotalCostOfFinanceObjectActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='EvaluationFunds',
        widget=DataGridField._properties['widget'](
            columns= { 'EvaluationType':SelectColumn("EvaluationType"), 'Amount':Column('Amount'), 'BAC':Column('BAC') },
            label="Evaluation Funds",
            label_msgid='ProjectDatabase_label_EvaluationFunds',
            i18n_domain='ProjectDatabase',
        ),
        columns= ("EvaluationType", "Amount", "BAC"),
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
        name='YearlyExpenditures',
        widget=DataGridField._properties['widget'](
            columns={ 'year' : Column("Amount"), 'amount' : Column("Amount") },
            label="Yearly Expenditures",
            label_msgid='ProjectDatabase_label_YearlyExpenditures',
            i18n_domain='ProjectDatabase',
        ),
        columns=("year", "amount"),
    ),
    ComputedField(
        name='SumYearlyExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total Yearly Expenditures",
            label_msgid='ProjectDatabase_label_SumYearlyExpenditures',
            i18n_domain='ProjectDatabase',
        ),
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
        columns=("report_type", "report_period", "report_received_date"),
    ),
    DataGridField(
        name='FundManagementOfficer',
        widget=DataGridField._properties['widget'](
            columns= { 'FMO_Name': Column("Name"), "FMO_Type":Column("Type"), "FMO_Period":Column('Period')},
            label="Fund Management Officer",
            label_msgid='ProjectDatabase_label_FundManagementOfficer',
            i18n_domain='ProjectDatabase',
        ),
        columns= ("FMO_Name", "FMO_Type", "FMO_Period"),
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
    TextField(
        name='FinanceObjectPreparationResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Financeobjectpreparationresults',
            label_msgid='ProjectDatabase_label_FinanceObjectPreparationResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
    ),
    DataGridField(
        name='ExecutingAgencyRiskRating',
        widget=DataGridField._properties['widget'](
            columns= {'Risk_Level':Column("Risk Level"), "Assessment_Date":CalendarColumn("Assessment Date"), 'Remarks':Column("Remarks")},
            label="Executing Agency Risk Rating",
            label_msgid='ProjectDatabase_label_ExecutingAgencyRiskRating',
            i18n_domain='ProjectDatabase',
        ),
        columns= ("Risk_Level", "Assessment_Date", "Remarks"),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Financials_schema = BaseFolderSchema.copy() + \
    getattr(FinancialsMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
title_field = Financials_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
Financials_schema['GEFTrustFund'].widget.size=15
Financials_schema['LDCFundAllocation'].widget.size=15
Financials_schema['SCCFAllocation'].widget.size=15
Financials_schema['StrategicPartnership'].widget.size=15
Financials_schema['AdaptationTrustFund'].widget.size=15
Financials_schema['SupplementaryUNEPAllocation'].widget.size=15
Financials_schema['ActualTotalExpenditures'].widget.size=15

Financials_schema['FundManagementOfficer'].widget.startup_directory = '/contacts'
##/code-section after-schema

class Financials(BaseFolder, CurrencyMixin, FinancialsMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IFinancials)

    meta_type = 'Financials'
    _at_rename_after_creation = True

    schema = Financials_schema

    ##code-section class-header #fill in your manual code here
    schema.moveField('GEFid', after='title')
    schema.moveField('FinanceCategory', after='GEFid')
    schema.moveField('TrusteeID', after='FinanceCategory')
    schema.moveField('PMSNumber', after='TrusteeID')
    schema.moveField('IMISNumber', after='PMSNumber')
    schema.moveField('GEFProjectAllocation', after='IMISNumber')
    schema.moveField('CashUNEPAllocation', after='GEFProjectAllocation')
    schema.moveField('GEFTrustFund', after='CashUNEPAllocation')
    schema.moveField('LDCFundAllocation', after='GEFTrustFund')
    schema.moveField('SCCFAllocation', after='LDCFundAllocation')
    schema.moveField('StrategicPartnership', after='SCCFAllocation')
    schema.moveField('AdaptationTrustFund', after='StrategicPartnership')
    schema.moveField('SupplementaryUNEPAllocation', after='AdaptationTrustFund')
    schema.moveField('SupplementaryUNEPAllocationRemark', after='SupplementaryUNEPAllocation')
    schema.moveField('CofinancingCash', after='SupplementaryUNEPAllocationRemark')
    schema.moveField('CofinancingInKind', after='CofinancingCash')
    schema.moveField('SumCofinCashPlanned', after='CofinancingInKind')
    schema.moveField('SumCofinCashActual', after='SumCofinCashPlanned')
    schema.moveField('SumCofinInKindPlanned', after='SumCofinCashActual')
    schema.moveField('SumCofinInKindActual', after='SumCofinInKindPlanned')
    schema.moveField('TotalCostOfProjectStagePlanned', after='SumCofinInKindActual')
    schema.moveField('TotalCostOfProjectStageActual', after='TotalCostOfProjectStagePlanned')
    schema.moveField('ApprovedUNEPBudget', after='TotalCostOfProjectStageActual')
    schema.moveField('CashDisbursements', after='ApprovedUNEPBudget')
    schema.moveField('SumCashDisbursements', after='CashDisbursements')
    schema.moveField('IMISExpenditures', after='SumCashDisbursements')
    schema.moveField('SumIMISExpenditures', after='IMISExpenditures')
    schema.moveField('ActualTotalExpenditures', after='SumIMISExpenditures')
    schema.moveField('Status', after='ActualTotalExpenditures')
    schema.moveField('PlannedDuration', after='Status')
    schema.moveField('InitialCompletionDate', after='PlannedDuration')
    schema.moveField('RevisedCompletionDate', after='InitialCompletionDate')
    schema.moveField('DelayReason', after='RevisedCompletionDate')
    schema.moveField('Reports', after='DelayReason')
    schema.moveField('LeadExecutingAgency', after='Reports')
    schema.moveField('OtherLeadExecutingAgency', after='LeadExecutingAgency')
    schema.moveField('FundManagementOfficer', after='OtherLeadExecutingAgency')
    schema.moveField('FinancialStatusRemarks', after='FundManagementOfficer')
    ##/code-section class-header

    # Methods

    security.declarePublic('getCashUNEPAllocation')
    def getCashUNEPAllocation(self):
        """Compute the cash allocation for the field
        """
        total = self.getZeroMoneyInstance()
        if self.getGEFTrustFund():
            total = total + self.getGEFTrustFund()
        if self.getLDCFundAllocation():
            total = total + self.getLDCFundAllocation()
        if self.getSCCFAllocation():
            total = total + self.getSCCFAllocation()
        if self.getStrategicPartnership():
            total = total + self.getStrategicPartnership()
        if self.getAdaptationTrustFund():
            total = total + self.getAdaptationTrustFund()
        if self.getSupplementaryUNEPAllocation():
            total = total + self.getSupplementaryUNEPAllocation()
        return total

    security.declarePublic('validate_GEFid')
    def validate_GEFid(self, value):
        """
        Check that the GEF id consists of 5 digits
        """
        if len(value) != 5:
            return 'The GEF ID must be 5 digits in length'

        for char in value:
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 'Only digits are allowed in the GEF ID'

    # Manually created methods

    security.declarePublic('Title')
    def Title(self):
        """
        """
        if hasattr(self, 'getAProject'):
            return 'Financial Management Information: ' + str(self.getAProject().Title())
        else:
            return 'Financial Management Information'



registerType(Financials, PROJECTNAME)
# end of class Financials

##code-section module-footer #fill in your manual code here
##/code-section module-footer



