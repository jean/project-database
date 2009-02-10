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
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
from DateTime import DateTime
##/code-section module-header

schema = Schema((

    ComputedField(
        name='GEFid',
        widget=ComputedField._properties['widget'](
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
    ComputedField(
        name='LeadExecutingAgency',
        widget=ComputedField._properties['widget'](
            label="Lead Executing Agency",
            label_msgid='ProjectDatabase_label_LeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='OtherLeadExecutingAgency',
        widget=ComputedField._properties['widget'](
            label="Other Project Executing Partners",
            label_msgid='ProjectDatabase_label_OtherLeadExecutingAgency',
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
            columns={ 'trust_fund' : SelectColumn("Trust Fund", vocabulary="getTrustFundVocabulary"), 'grant_to_unep' : Column("Grant to UNEP") },
            label="Finance Object Amount",
            label_msgid='ProjectDatabase_label_FinanceObjectAmount',
            i18n_domain='ProjectDatabase',
        ),
        columns=("trust_fund", "grant_to_unep"),
    ),
    ComputedField(
        name='SumFinanceObjectAmount',
        widget=ComputedField._properties['widget'](
            label='Sumfinanceobjectamount',
            label_msgid='ProjectDatabase_label_SumFinanceObjectAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='FinanceObjectFee',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="Finance Object Fee",
            label_msgid='ProjectDatabase_label_FinanceObjectFee',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='CommittedGEFGrant',
        default='0.0',
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
        name='CoFinancingCash',
        widget=DataGridField._properties['widget'](
            columns={ 'cofinancing_cash_source' : SelectColumn("Source", vocabulary="getDonorTypesVocabulary"), 'cofinancing_cash_donor_name' : Column("Name of donor"), 'cofinancing_cash_planned_amount' : Column("Planned Amount"), 'cofinancing_cash_actual_amount' : Column("Actual Amount") },
            label="Cofinancing: Cash",
            label_msgid='ProjectDatabase_label_CoFinancingCash',
            i18n_domain='ProjectDatabase',
        ),
        columns=("cofinancing_cash_source", "cofinancing_cash_donor_name", "cofinancing_cash_planned_amount", "cofinancing_cash_actual_amount"),
    ),
    DataGridField(
        name='CoFinancingInKind',
        widget=DataGridField._properties['widget'](
            columns={ 'cofinancing_inkind_source' : SelectColumn("Source", vocabulary="getDonorTypesVocabulary"), 'cofinancing_inkind_donor_name' : Column("Name of donor"), 'cofinancing_inkind_planned_amount' : Column("Planned Amount"), 'cofinancing_inkind_actual_amount' : Column("Actual Amount") },
            label="Cofinancing: In Kind",
            label_msgid='ProjectDatabase_label_CoFinancingInKind',
            i18n_domain='ProjectDatabase',
        ),
        columns=("cofinancing_inkind_source", "cofinancing_inkind_donor_name", "cofinancing_inkind_planned_amount", "cofinancing_inkind_actual_amount"),
    ),
    ComputedField(
        name='SumCoFinCashPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: Cash (Planned)",
            label_msgid='ProjectDatabase_label_SumCoFinCashPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='SumCoFinCashActual',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: Cash (Actual)",
            label_msgid='ProjectDatabase_label_SumCoFinCashActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='SumCoFinInKindPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: In Kind (Planned)",
            label_msgid='ProjectDatabase_label_SumCoFinInKindPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='SumCoFinInKindActual',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: In Kind (Actual)",
            label_msgid='ProjectDatabase_label_SumCoFinInKindActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCoFinOfFinanceObjectPlanned',
        widget=ComputedField._properties['widget'](
            label='Totalcofinoffinanceobjectplanned',
            label_msgid='ProjectDatabase_label_TotalCoFinOfFinanceObjectPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCoFinOfFinanceObjectActual',
        widget=ComputedField._properties['widget'](
            label='Totalcofinoffinanceobjectactual',
            label_msgid='ProjectDatabase_label_TotalCoFinOfFinanceObjectActual',
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
    ComputedField(
        name='TotalCostOfFinanceObjectVariance',
        widget=ComputedField._properties['widget'](
            label='Totalcostoffinanceobjectvariance',
            label_msgid='ProjectDatabase_label_TotalCostOfFinanceObjectVariance',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='EvaluationFunds',
        widget=DataGridField._properties['widget'](
            columns= { 'EvaluationType':SelectColumn("EvaluationType", vocabulary="getEvaluationTypeVocabulary"), 'Amount':Column('Amount'), 'BAC':Column('BAC') },
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
            columns={ 'year' : Column("Year"), 'amount' : Column("Amount") },
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
        name='ExpectedCompletionDate',
        widget=CalendarWidget(
            label="Expected Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_ExpectedCompletionDate',
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
            columns={ 'report_type' : SelectColumn("Report Type", vocabulary="getReportTypesVocabulary"), 'report_period' : Column("Report Period"), 'report_received_date' : CalendarColumn("Report Received Date"), 'amount' : Column("Amount") },
            label="Reports",
            label_msgid='ProjectDatabase_label_Reports',
            i18n_domain='ProjectDatabase',
        ),
        columns=("report_type", "report_period", "report_received_date", "amount"),
    ),
    DataGridField(
        name='FundManagementOfficer',
        widget=DataGridField._properties['widget'](
            columns= { 'FMO_Name': Column("Name"), "FMO_Type":SelectColumn("Type", vocabulary="getTMCategoryVocabulary"), "FMO_Period":Column('Period')},
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
        columns=("revision_number", "revision_type","revision_date"),
    ),
    TextField(
        name='FinanceObjectPreparationResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Finance Object Preparation Results",
            label_msgid='ProjectDatabase_label_FinanceObjectPreparationResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
    ),
    DataGridField(
        name='ExecutingAgencyRiskRating',
        widget=DataGridField._properties['widget'](
            columns= {'Risk_Level':SelectColumn("Risk Level", vocabulary="getRiskLevelVocabulary"), "Assessment_Date":CalendarColumn("Assessment Date"), 'Remarks':Column("Remarks")},
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
    schema.copy()

##code-section after-schema #fill in your manual code here
Financials_schema['title'].widget.visible = {'edit':'hidden', 'view':'invisible'}
Financials_schema['FinanceCategory'].widget.visible = {'edit':'hidden', 'view':'invisible'}
##/code-section after-schema

class Financials(BaseFolder, CurrencyMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IFinancials)

    meta_type = 'Financials'
    _at_rename_after_creation = True

    schema = Financials_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    security.declarePublic('getDonorTypesVocabulary')
    def getDonorTypesVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('DonorType')
        return vocab.getDisplayList(self)

    security.declarePublic('getRiskLevelVocabulary')
    def getRiskLevelVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('RiskLevel')
        return vocab.getDisplayList(self)

    security.declarePublic('getReportTypesVocabulary')
    def getReportTypesVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('ReportType')
        return vocab.getDisplayList(self)

    security.declarePublic('getRevisionTypeVocabulary')
    def getRevisionTypeVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('ProjectRevisionType')
        return vocab.getDisplayList(self)

    security.declarePublic('getTrustFundVocabulary')
    def getTrustFundVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('TrustFund')
        return vocab.getDisplayList(self)

    security.declarePublic('getEvaluationTypeVocabulary')
    def getEvaluationTypeVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('EvaluationType')
        return vocab.getDisplayList(self)

    security.declarePublic('getTMCategoryVocabulary')
    def getTMCategoryVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('TMCategory')
        return vocab.getDisplayList(self)

    security.declarePublic('_computeDataGridAmount')
    def _computeDataGridAmount(self,column):
        """
        """
        amount = self.getZeroMoneyInstance()
        for v in column:
            if v:
                amount += v
        return amount

    security.declarePublic('getSumCoFinCashPlanned')
    def getSumCoFinCashPlanned(self):
        """
        """
        values = self.getCoFinancingCash()
        return self._computeDataGridAmount( \
            [v['cofinancing_cash_planned_amount']  \
                for v in values if v['cofinancing_cash_planned_amount']])
    security.declarePublic('getSumCoFinCashActual')
    def getSumCoFinCashActual(self):
        """
        """
        values = self.getCoFinancingCash()
        return self._computeDataGridAmount( \
            [v['cofinancing_cash_actual_amount'] \
                for v in values if v['cofinancing_cash_actual_amount']])
    security.declarePublic('getSumCoFinInKindPlanned')
    def getSumCoFinInKindPlanned(self):
        """
        """
        values = self.getCoFinancingInKind()
        return self._computeDataGridAmount( \
            [v['cofinancing_inkind_planned_amount'] \
                for v in values if v['cofinancing_inkind_planned_amount']])
    security.declarePublic('getSumCoFinInKindActual')
    def getSumCoFinInKindActual(self):
        """
        """
        values = self.getCoFinancingInKind()
        return self._computeDataGridAmount( \
            [v['cofinancing_inkind_actual_amount'] \
                for v in values if v['cofinancing_inkind_actual_amount']])
    security.declarePublic('getSumCashDisbursements')
    def getSumCashDisbursements(self):
        """
        """
        values = self.getCashDisbursements()
        return self._computeDataGridAmount( \
            [v['cash_disbursements_amount'] \
                for v in values if v['cash_disbursements_amount']])
    security.declarePublic('getDifference')
    def getDifference(self):
        """ calculate the difference between the committed and allocated GEF grant
        """
        totalGrant = self.getSumFinanceObjectAmount()
        committedGEFGrant = self.getCommittedGEFGrant()
        return totalGrant - committedGEFGrant

    def getSumFinanceObjectAmount(self):
        """
        """
        values = self.getFinanceObjectAmount()
        unep_alloc = self._computeDataGridAmount(
          [v['grant_to_unep'] for v in values if v['grant_to_unep']])
        return unep_alloc

    def getTotalFinanceObject(self):
        """
        """
        return self.getSumFinanceObjectAmount() + self.getFinanceObjectFee()

    def getSumYearlyExpenditures(self):
        """
        """
        values = self.getYearlyExpenditures()
        return self._computeDataGridAmount( \
            [v['amount'] for v in values if v['amount']])
    def getGEFid(self):
        """
        """
        return self.getAProject()['project_general_info'].getGEFid()

    def getLeadExecutingAgency(self):
        """
        """
        return self.getAProject()['project_general_info'].getLeadAgency()

    def getOtherLeadExecutingAgency(self):
        """
        """
        agencies = self.getAProject()['project_general_info'].getOtherImplementingAgency()
        if agencies:
            return agencies[0]

    def getTotalCoFinOfFinanceObjectPlanned(self):
        """
        """
        total = self.getZeroMoneyInstance()
        if self.getSumCoFinCashPlanned():
            total += self.getSumCoFinCashPlanned()
        if self.getSumCoFinInKindPlanned():
            total += self.getSumCoFinInKindPlanned()
        return total

    def getTotalCoFinOfFinanceObjectActual(self):
        """
        """
        total = self.getZeroMoneyInstance()
        if self.getSumCoFinCashActual():
            total += self.getSumCoFinCashActual()
        if self.getSumCoFinInKindActual():
            total += self.getSumCoFinInKindActual()
        return total

    def getTotalCostOfFinanceObjectPlanned(self):
        """
        """
        total = self.getSumFinanceObjectAmount()
        if self.getSumCoFinCashPlanned():
            total += self.getSumCoFinCashPlanned()
        if self.getSumCoFinInKindPlanned():
            total += self.getSumCoFinInKindPlanned()
        return total

    def getTotalCostOfFinanceObjectActual(self):
        """
        """
        total = self.getSumYearlyExpenditures()
        if self.getSumCoFinCashActual():
            total += self.getSumCoFinCashActual()
        if self.getSumCoFinInKindActual():
            total += self.getSumCoFinInKindActual()
        return total

    def getTotalCostOfFinanceObjectVariance(self):
        return self.getTotalCostOfFinanceObjectActual() - self.getTotalCostOfFinanceObjectPlanned()

    def getLastestRevisionDate(self):
        values = self.getProjectRevision()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['revision_date']:
                    if date < v['revision_date']:
                        date = v['revision_date']
            if date != DateTime('1900/01/01'):
                return date

    def getAmountReceivable(self):
        return self.getSumCashDisbursements() - self.getSumYearlyExpenditures()

    def getLatestReportData(self, report, field):
        values = self.getReports()
        result = ''
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['report_received_date'] and v['report_type'] == report:
                    if date < v['report_received_date']:
                        date = v['report_received_date']
                        result = v[field]
            if date != DateTime('1900/01/01'):
                return result
        return 'Unspecified'

    def getSubProjectsTotalCashDisbursed(self):
        result = self.getZeroMoneyInstance()
        subs = self.getFolderContents(full_objects=True)
        for sub in subs:
            result += sub.getSumCashDisbursements()
        return result

    def getSubProjectsTotalExpenditures(self):
        result = self.getZeroMoneyInstance()
        subs = self.getFolderContents(full_objects=True)
        for sub in subs:
            result += sub.getSumYearlyExpenditures()
        return result

    def getSubProjectsTotalReceivable(self):
        result = self.getZeroMoneyInstance()
        subs = self.getFolderContents(full_objects=True)
        for sub in subs:
            result += sub.getAmountReceivable()
        return result

    def getLatestEARiskRating(self):
        values = self.getExecutingAgencyRiskRating()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['Assessment_Date']:
                    if date < v['Assessment_Date']:
                        date = v['Assessment_Date']
                        rating = self.getSelectedVocabularyValue( \
                            v['Risk_Level'],
                            'RiskLevel')
            if date != DateTime('1900/01/01'):
                return rating
        return None

    def getSelectedVocabularyValue(self, selection, vocabName):
        if selection:
            atvm = getToolByName(self, 'portal_vocabularies')
            vocab = atvm.getVocabularyByName(vocabName)
            dict = vocab.getVocabularyDict(self)
            return dict[selection][0]
        return None

    def getCurrentFMO(self):
        values = self.getFundManagementOfficer()
        if values:
            date = '1900'
            for v in values:
                if v['FMO_Period'] and v['FMO_Name'] and v['FMO_Type'] == 'Principal':
                    if date < v['FMO_Period']:
                        date = v['FMO_Period']
                        name = v['FMO_Name']
            if date != '1900':
                return name
        return None


registerType(Financials, PROJECTNAME)
# end of class Financials

##code-section module-footer #fill in your manual code here
##/code-section module-footer



