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

__author__ = """Mike Metcalfe <mikejmets@gmail.com>, Jurgen Blignaut
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
from Products.FinanceFields.Money import Money
from Products.ProjectDatabase.utils import getYearVocabulary
from Products.CMFCore.utils import getToolByName
from Products.DataGridField import MoneyColumn, ReferenceColumn
from Products.ProjectDatabase.content.ProjectDatabase import CSVImporter
from Products.ProjectDatabase.content.interfaces import IProject
from Products.ProjectDatabase.widgets.UNEPSelectionWidget import UNEPSelectionWidget

datagrid_schema = Schema((
    MoneyField(
        name='grant_to_unep',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),

    MoneyField(
        name='cofinancing_cash_planned_amount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),

    MoneyField(
        name='cofinancing_cash_actual_amount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),

    MoneyField(
        name='cofinancing_inkind_planned_amount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),

    MoneyField(
        name='cofinancing_inkind_actual_amount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),

    MoneyField(
        name='Amount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),

    MoneyField(
        name='cash_disbursements_amount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),

    MoneyField(
        name='amount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='Financials',
        ),
    ),
))
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
        write_permission="FMO",
    ),
    StringField(
        name='TrusteeID',
        widget=StringField._properties['widget'](
            label="Trustee ID",
            label_msgid='ProjectDatabase_label_TrusteeID',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    StringField(
        name='PMSNumber',
        widget=StringField._properties['widget'](
            label="PMS Number",
            label_msgid='ProjectDatabase_label_PMSNumber',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    StringField(
        name='IMISNumber',
        widget=StringField._properties['widget'](
            label="IMIS Number",
            label_msgid='ProjectDatabase_label_IMISNumber',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='LeadExecutingAgency',
        widget=ComputedField._properties['widget'](
            label="Lead Executing Agency",
            label_msgid='ProjectDatabase_label_LeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
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
        write_permission="FMO",
    ),
    StringField(
        name='OtherLeadExecutingAgency',
        widget=StringField._properties['widget'](
            label="Other Lead Executing Agency",
            label_msgid='ProjectDatabase_label_OtherLeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='FundManagementOfficer',
        widget=DataGridField._properties['widget'](
            columns= {"FMO_Name":
                         ReferenceColumn("Name",
                         fieldname='FMOname'),
                      "FMO_Type":
                         SelectColumn("Type",
                         vocabulary="getTMCategoryVocabulary"),
                      "FMO_Period":
                         Column('Period')},
            label="Fund Management Officer",
            label_msgid='ProjectDatabase_label_FundManagementOfficer',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns= ("FMO_Name", "FMO_Type", "FMO_Period"),
    ),
    DateTimeField(
        name='ExpectedCompletionDate',
        widget=CalendarWidget(
            label="Expected Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_ExpectedCompletionDate',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    StringField(
        name='Status',
        widget=UNEPSelectionWidget(
            label="Project Status",
            label_msgid='ProjectDatabase_label_Status',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        vocabulary=NamedVocabulary("""Status"""),
    ),
    TextField(
        name='FinancialStatusRemarks',
        widget=TextAreaWidget(
            label="Project Financial Status - Remarks",
            label_msgid='ProjectDatabase_label_FinancialStatusRemarks',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='FinanceObjectAmount',
        widget=DataGridField._properties['widget'](
            columns={'trust_fund':
                        SelectColumn("Trust Fund",
                        vocabulary="getTrustFundVocabulary"),
                     'grant_to_unep':
                        MoneyColumn("Grant to UNEP",
                        field=datagrid_schema['grant_to_unep'])},
            label="Finance Object Amount",
            label_msgid='ProjectDatabase_label_FinanceObjectAmount',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("trust_fund", "grant_to_unep"),
    ),
    ComputedField(
        name='SumFinanceObjectAmount',
        widget=ComputedField._properties['widget'](
            label='Sum finance object amount',
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
        write_permission="FMO",
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
        write_permission="FMO",
    ),
    ComputedField(
        name='Difference',
        widget=ComputedField._properties['widget'](
            label='Difference',
            label_msgid='ProjectDatabase_label_Difference',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='CoFinancingCash',
        widget=DataGridField._properties['widget'](
            columns={'cofinancing_cash_source' :
                         SelectColumn("Source",
                         vocabulary="getDonorTypesVocabulary"),
                     'cofinancing_cash_donor_name' :
                         Column("Name of donor"),
                     'cofinancing_cash_planned_amount' :
                         MoneyColumn("Planned Amount",
                         field=datagrid_schema['cofinancing_cash_planned_amount']),
                     'cofinancing_cash_actual_amount' :
                         MoneyColumn("Actual Amount",
                         field=datagrid_schema['cofinancing_cash_planned_amount']) },
            label="Cofinancing: Cash",
            label_msgid='ProjectDatabase_label_CoFinancingCash',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("cofinancing_cash_source",
                 "cofinancing_cash_donor_name",
                 "cofinancing_cash_planned_amount",
                 "cofinancing_cash_actual_amount"),
    ),
    DataGridField(
        name='CoFinancingInKind',
        widget=DataGridField._properties['widget'](
            columns={'cofinancing_inkind_source' :
                         SelectColumn("Source",
                         vocabulary="getDonorTypesVocabulary"),
                     'cofinancing_inkind_donor_name' :
                         Column("Name of donor"),
                     'cofinancing_inkind_planned_amount' :
                         MoneyColumn("Planned Amount",
                         field=datagrid_schema['cofinancing_inkind_planned_amount']),
                     'cofinancing_inkind_actual_amount' :
                         MoneyColumn("Actual Amount",
                         field=datagrid_schema['cofinancing_inkind_actual_amount']) },
            label="Cofinancing: In Kind",
            label_msgid='ProjectDatabase_label_CoFinancingInKind',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("cofinancing_inkind_source",
                 "cofinancing_inkind_donor_name",
                 "cofinancing_inkind_planned_amount",
                 "cofinancing_inkind_actual_amount"),
    ),
    ComputedField(
        name='SumCoFinCashPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: Cash (Planned)",
            label_msgid='ProjectDatabase_label_SumCoFinCashPlanned',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='SumCoFinCashActual',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: Cash (Actual)",
            label_msgid='ProjectDatabase_label_SumCoFinCashActual',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='SumCoFinInKindPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: In Kind (Planned)",
            label_msgid='ProjectDatabase_label_SumCoFinInKindPlanned',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='SumCoFinInKindActual',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing: In Kind (Actual)",
            label_msgid='ProjectDatabase_label_SumCoFinInKindActual',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='TotalCoFinOfFinanceObjectPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing (Planned)",
            label_msgid='ProjectDatabase_label_TotalCoFinOfFinanceObjectPlanned',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='TotalCoFinOfFinanceObjectActual',
        widget=ComputedField._properties['widget'](
            label="Total Cofinancing (Actual)",
            label_msgid='ProjectDatabase_label_TotalCoFinOfFinanceObjectActual',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='TotalCostOfFinanceObjectPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Finance Object (Planned)",
            label_msgid='ProjectDatabase_label_TotalCostOfFinanceObjectPlanned',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='TotalCostOfFinanceObjectActual',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Finance Object (Actual)",
            label_msgid='ProjectDatabase_label_TotalCostOfFinanceObjectActual',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='TotalCostOfFinanceObjectVariance',
        widget=ComputedField._properties['widget'](
            label="Total Cost Variance",
            label_msgid='ProjectDatabase_label_TotalCostOfFinanceObjectVariance',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='EvaluationFunds',
        widget=DataGridField._properties['widget'](
            columns= {'EvaluationType':
                          SelectColumn("EvaluationType",
                          vocabulary="getEvaluationTypeVocabulary"),
                      'Amount':
                          MoneyColumn('Amount',
                          field=datagrid_schema['Amount']),
                      'BAC':
                          Column('BAC') },
            label="Evaluation Funds",
            label_msgid='ProjectDatabase_label_EvaluationFunds',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns= ("EvaluationType", "Amount", "BAC"),
    ),
    DataGridField(
        name='CashDisbursements',
        widget=DataGridField._properties['widget'](
            columns={ 'cash_disbursements_date' :
                          CalendarColumn("Date"),
                      'cash_disbursements_amount' :
                          MoneyColumn("Amount",
                          field=datagrid_schema['cash_disbursements_amount']),
                      'cash_disbursements_imis_rcpt_number' :
                          Column("IMIS RCTP Number"),
                      'document':
                          ReferenceColumn('Document',
                          fieldname='CashDisbursementsDocument')},
            label="Cash Disbursements",
            label_msgid='ProjectDatabase_label_CashDisbursements',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("cash_disbursements_date", "cash_disbursements_amount", "cash_disbursements_imis_rcpt_number", "document"),
    ),
    ComputedField(
        name='SumCashDisbursements',
        widget=ComputedField._properties['widget'](
            label="Total Cash Disbursements",
            label_msgid='ProjectDatabase_label_SumCashDisbursements',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='YearlyExpenditures',
        widget=DataGridField._properties['widget'](
            columns={ 'year' :
                          SelectColumn("Year",
                          vocabulary='getFiscalYearVocabulary'),
                      'amount' :
                          MoneyColumn("Amount",
                          field=datagrid_schema['amount']) },
            label="Yearly Expenditures",
            label_msgid='ProjectDatabase_label_YearlyExpenditures',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("year", "amount"),
    ),
    ComputedField(
        name='SumYearlyExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total Yearly Expenditures",
            label_msgid='ProjectDatabase_label_SumYearlyExpenditures',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
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
        write_permission="FMO",
    ),
    TextField(
        name='DelayReason',
        widget=TextAreaWidget(
            label="Reasons for delay",
            label_msgid='ProjectDatabase_label_DelayReason',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='Reports',
        widget=DataGridField._properties['widget'](
            columns={ 'report_type' :
                          SelectColumn("Report Type",
                          vocabulary="getReportTypesVocabulary"),
                      'report_period' :
                          Column("Report Period"),
                      'report_received_date' :
                          CalendarColumn("Report Received Date"),
                      'amount' :
                          MoneyColumn("Amount",
                          field=datagrid_schema['amount']),
                      'document':
                          ReferenceColumn('Document',
                          fieldname='ReportsDocument')},
            label="Report s",
            label_msgid='ProjectDatabase_label_Reports',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("report_type", "report_period", "report_received_date", "amount", "document"),
    ),
    DataGridField(
        name='ProjectRevision',
        widget=DataGridField._properties['widget'](
            columns={"revision_number":
                         Column("Revision Number"),
                     "revision_type":
                         SelectColumn("Revision Type",
                         vocabulary="getRevisionTypeVocabulary"),
                     "revision_date":
                         CalendarColumn("Revision Date"),
                      'document':
                          ReferenceColumn('Document',
                          fieldname='ProjectRevisionDocument')},
            label="Project Revision",
            label_msgid='ProjectDatabase_label_ProjectRevision',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("revision_number", "revision_type","revision_date", "document"),
    ),
    TextField(
        name='FinanceObjectPreparationResults',
        allowable_content_types=('text/plain', 'text/structured',
                                 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Finance Object Results",
            label_msgid='ProjectDatabase_label_FinanceObjectPreparationResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        write_permission="FMO",
    ),
    DataGridField(
        name='ExecutingAgencyRiskRating',
        widget=DataGridField._properties['widget'](
            columns= {'Risk_Level':
                          SelectColumn("Risk Level",
                          vocabulary="getRiskLevelVocabulary"),
                      "Assessment_Date":
                          CalendarColumn("Assessment Date"),
                      'Remarks':
                          Column("Remarks")},
            label="Executing Agency Risk Rating",
            label_msgid='ProjectDatabase_label_ExecutingAgencyRiskRating',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns= ("Risk_Level", "Assessment_Date", "Remarks"),
    ),
    ComputedField(
        name='CurrentPrincipalFMO',
        widget=ComputedField._properties['widget'](
            visible={'edit':'hidden', 'view':'invisible'},
            label='Current principal fmo',
            label_msgid='ProjectDatabase_label_CurrentPrincipalFMO',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='CurrentBackupFMO',
        widget=ComputedField._properties['widget'](
            visible={'edit':'hidden', 'view':'invisible'},
            label='Currentbackupfmo',
            label_msgid='ProjectDatabase_label_CurrentBackupFMO',
            i18n_domain='ProjectDatabase',
        ),
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

Financials_schema = Financials_schema.copy()  + Schema((

    ReferenceField("ReportsDocument",
            widget = ReferenceBrowserWidget(
                visible=False,
                startup_directory_method='getProjectDocumentsFolder',
            ),
            allowed_types=('File',),
            relationship='reports_document_fake',
            multiValued=1,
        ),
    ReferenceField("ProjectRevisionDocument",
            widget = ReferenceBrowserWidget(
                visible=False,
                startup_directory_method='getProjectDocumentsFolder',
            ),
            allowed_types=('File',),
            relationship='projectrevision_document_fake',
            multiValued=1,
        ),
    ReferenceField("CashDisbursementsDocument",
            widget = ReferenceBrowserWidget(
                visible=False,
                startup_directory_method='getProjectDocumentsFolder',
            ),
            allowed_types=('File',),
            relationship='cashdisbursements_document_fake',
            multiValued=1,
        ),
    ReferenceField("FMOname",
            widget = ReferenceBrowserWidget(
                label="Name",
                visible=False,
                startup_directory='/contacts',
            ),
            allowed_types=('Person',),
            relationship='fmi_fmo_fake',
            multiValued=1,
        ),

    ))
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

    def getAProject(self):
        parent = getattr(self, 'aq_parent', None)
        while parent is not None:
            if IProject.providedBy(parent):
                return parent
            parent = getattr(parent, 'aq_parent', None)
        return None

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
    security.declarePublic('getSumCashDisbursementsToDate')
    def getSumCashDisbursementsToDate(self, to_date):
        """
        """
        values = self.getCashDisbursements()
        return self._computeDataGridAmount( \
            [v['cash_disbursements_amount'] \
                for v in values \
                  if v['cash_disbursements_amount'] and \
                     v['cash_disbursements_date'] and \
                     v['cash_disbursements_date'] <= to_date])
    security.declarePublic('getDifference')
    def getDifference(self):
        """ calculate the difference between the committed and allocated GEF grant
        """
        totalGrant = self.getSumFinanceObjectAmount()
        committedGEFGrant = self.getCommittedGEFGrant()
        return totalGrant - committedGEFGrant

    def getSumFinanceObjectAmount(self):
        """
        UNEP GEF Amount
        """
        values = self.getFinanceObjectAmount()
        unep_alloc = self._computeDataGridAmount(
          [v['grant_to_unep'] for v in values if v['grant_to_unep']])
        return unep_alloc

    def getTotalFinanceObject(self):
        """
        Total GEF Amount
        """
        sum_fin_object = self.getSumFinanceObjectAmount()
        if sum_fin_object is None:
            sum_fin_object = 0

        fin_object_fee = self.getFinanceObjectFee()
        if fin_object_fee is None:
            fin_object_fee = 0

        return sum_fin_object + fin_object_fee

    def getSumYearlyExpenditures(self):
        """
        """
        values = self.getYearlyExpenditures()
        returnValue = self._computeDataGridAmount( \
            [v['amount'] for v in values if v['amount']])
        return returnValue

    def getGEFid(self):
        """
        """
        project = self.getAProject()
        return project and project['project_general_info'].getGEFid() or ''

    def getLeadExecutingAgency(self):
        """
        """
        project = self.getAProject()
        return project and \
            project['project_general_info'].getLeadExecutingAgencyNames() or []

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

    def getLastestRevisionDate(self, type=None):
        values = self.getProjectRevision()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                revision_date = v.get('revision_date', None)
                revision_type = v.get('revision_type', None)
                if revision_date and revision_type:
                    if type is None or revision_type == type:
                        if date < revision_date:
                            date = revision_date
            if date != DateTime('1900/01/01'):
                return date

    def getNumberOfRevisions(self):
        return len(self.getProjectRevision())

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

    def getEARiskRatings(self):
        values = self.getExecutingAgencyRiskRating()
        results = []
        if values:
            for v in values:
                if v['Assessment_Date'] and v['Risk_Level']:
                    rating = self.getSelectedVocabularyValue( \
                        v['Risk_Level'],
                        'RiskLevel')
                    year = v['Assessment_Date'].year()
                    results.append((year, rating))
        return results

    def getEARiskRatingsAndDates(self):
        values = self.getExecutingAgencyRiskRating()
        results = []
        if values:
            for v in values:
                if v['Assessment_Date'] and v['Risk_Level']:
                    rating = v['Risk_Level']
                    date = v['Assessment_Date']
                    results.append((rating, date))
        return results

    def getSelectedVocabularyValue(self, selection, vocabName):
        if selection:
            atvm = getToolByName(self, 'portal_vocabularies')
            vocab = atvm.getVocabularyByName(vocabName)
            dict = vocab.getVocabularyDict(self)
            return dict[selection][0]
        return None

    def getCurrentFMOPerson(self, fmo_type='Principal'):
        person = None
        values = self.getFundManagementOfficer()
        if values:
            refcat = getToolByName(self, 'reference_catalog')
            date = '1900'
            for v in values:
                if v['FMO_Period'] and v['FMO_Name'] and v['FMO_Type'] == fmo_type:
                    if date < v['FMO_Period']:
                        date = v['FMO_Period']
                        officer = refcat.lookupObject(v['FMO_Name'])
                        if officer is not None:
                            person = officer
        return person

    def getCurrentFMODetails(self, fmo_type='Principal'):
        person = self.getCurrentFMOPerson(fmo_type)
        if person:
            return person.getFullname(), \
                  person.getEmail(), \
                  person.getBusinessPhone()
        return '', '', ''

    def getCurrentFMOSortable(self, fmo_type='Principal'):
        person = self.getCurrentFMOPerson(fmo_type)
        if person:
            return person.getLastName() + ', ' + person.getFirstName()
        return ''

    def getCurrentPrincipalFMO(self):
        fullname, email, phone = self.getCurrentFMODetails('Principal')
        return fullname

    def getCurrentBackupFMO(self):
        fullname, email, phone = self.getCurrentFMODetails('Backup')
        return fullname

    def getEvaluationAmount(self, type):
        """
        Sum the evaluation funds for the given field
        """
        values = self.getEvaluationFunds()
        amount = self._computeDataGridAmount(
          [v['Amount'] for v in values \
            if v['Amount'] and v['EvaluationType'] == type])
        return amount

    def getFiscalYearVocabulary(self):
        return getYearVocabulary(fiscal=False)

    def getDonorPledges(self):
        result = []
        cofincash = self.getCoFinancingCash()
        if cofincash:
            for v in cofincash:
                vtype = v['cofinancing_cash_source']
                vdonor = v['cofinancing_cash_donor_name']
                vamount = v['cofinancing_cash_planned_amount']
                for item in result:
                    if item['type'] == vtype and \
                       item['name'].lower() == vdonor.lower():
                        item['amount'] += vamount
                        break
                else:
                    result.append({'type':vtype, 'name':vdonor, 'amount':vamount})
        cofininkind = self.getCoFinancingInKind()
        if cofininkind:
            for v in cofininkind:
                vtype = v['cofinancing_inkind_source']
                vdonor = v['cofinancing_inkind_donor_name']
                vamount = v['cofinancing_inkind_planned_amount']
                for item in result:
                    if item['type'] == vtype and \
                       item['name'].lower() == vdonor.lower():
                        item['amount'] += vamount
                        break
                else:
                    result.append({'type':vtype, 'name':vdonor, 'amount':vamount})
        return result

    def getLastDisbursement(self):
        values = self.getCashDisbursements()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                disbursements_date = v.get('cash_disbursements_date', None)
                disbursements_amount = v.get('cash_disbursements_amount', None)
                if disbursements_date and disbursements_amount:
                    if date < disbursements_date:
                        date = disbursements_date
                        amount = disbursements_amount
            if date != DateTime('1900/01/01'):
                return date, amount
        return None, None

    def hasDelayedFinancialReports(self):
        exp_date = self.getLatestReportData('expenditure', 'report_received_date')
        now = DateTime()
        return not (exp_date != 'Unspecified' and (now - exp_date) < 300)

    def hasDelayedSubstantiveReports(self):
        prog_date = self.getLatestReportData('progress', 'report_received_date')
        now = DateTime()
        return not (prog_date != 'Unspecified' and (now - prog_date) < 300)

    security.declarePublic('getProjectDocumentsFolder')
    def getProjectDocumentsFolder(self):
        purl = getToolByName(self, 'portal_url'). \
                getPortalObject().absolute_url()
        folder = self.getAProject().get('documents', None)
        if not folder:
            folder = self.getAProject()
        curl = folder.absolute_url()
        return curl[len(purl)+1:]

registerType(Financials, PROJECTNAME)
# end of class Financials

##code-section module-footer #fill in your manual code here
import logging
from DateTime import DateTime

import transaction
from zope import event
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.event import ObjectInitializedEvent

from Products.ProjectDatabase.content.ProjectDatabase import CSVImporter

class Financial_CSVImporter(CSVImporter):
    def __init__(self, context, csvfile, coding, debug):
        CSVImporter.__init__(self, context, csvfile, coding, debug)
        self.LOGGER = logging.getLogger('[Financial import]')
        self._required_fields.extend(['FinanceCategory',])
        self._fmis_created     = 0
        self._fmis_not_created = 0

    def importCSV(self):
        dict_reader = self.getDictReader()
        rows = [row for row in dict_reader]
        # We cannot import subproject financials as top-level data
        if 'SubProjectId' in rows[0].keys():
            raise 'Aborting process. This is a subproject Financials file!'
        del dict_reader
        self.writeProgressTemplate(len(rows))
        for row in rows:
            gef_id = row.get('GEFid', None)
            self.writeMessage('Searching for project:GEFid=%s' %gef_id)
            project = self.getProjectByGefId(gef_id)
            if not project:
                self._fmis_not_created += 1
                self.writeMessage('No project found for GEFid:%s' % gef_id)
                continue

            fmi = self.getFMI(project, row)
            if not fmi:
                self._fmis_not_created += 1
                self.writeMessage(
                        'FMI for GEFid:%s could not be found or created.' \
                        % gef_id)
                continue
            self.writeMessage('Updating FMI fields')
            self.updateFields(fmi, row)
            transaction.commit()
            fmi.reindexObject()
            self.writeMessage('Done updating fields.')
            count = self._fmis_created + self._fmis_not_created
            self.writeProgressLine(count)

        msg = "Financials created:%s" % self._fmis_created
        self._result_lines.append(msg)
        msg = "Financials NOT created:%s" % self._fmis_not_created
        self._result_lines.append(msg)
        self.writeRedirectUrl()

    def createFMI(self, container, category, title):
        container.invokeFactory(id=category, type_name='Financials')
        new_fmi = container[category]
        new_fmi.edit(title=title, FinanceCategory=category)
        transaction.commit()
        self._fmis_created += 1
        return new_fmi

    def getFMI(self, project, data_dict):
        try:
            category = data_dict['FinanceCategory'].lower()
            title = data_dict.get('title', category.upper())
            container = project['fmi_folder']
            query = {'portal_type' : 'Financials',
                     'getFinanceCategory': category,
                     'path' : {'query' : '/'.join(project.getPhysicalPath())},
                    }
            brains = self._pc(**query)
            if len(brains):
                return brains[0].getObject()
            else:
                return self.createFMI(container, category, title)
        except KeyError:
            self.writeMessage('Essential Financial information is not in CSV:%s.') \
                % self._csvfile
            return None

class Expenditure_CSVImporter(CSVImporter):
    def __init__(self, context, csvfile, coding, debug):
        CSVImporter.__init__(self, context, csvfile, coding, debug)
        self.LOGGER = logging.getLogger('[Financial Expenditure import]')
        self._required_fields.extend(['IMISNumber',])
        self._expenditures_created     = 0
        self._expenditures_not_created = 0

    def importCSV(self):
        dict_reader = self.getDictReader()
        rows = [row for row in dict_reader]
        del dict_reader
        self.writeProgressTemplate(len(rows))
        for row in rows:
            gef_id = row.get('GEFid', None)
            gef_id = row['GEFid'].strip()
            if not gef_id:
                self.writeMessage('The GEFId is empty!')
                continue 
            self.writeMessage('Searching for project:GEFid=%s' %gef_id)
            project = self.getProjectByGefId(gef_id)
            if not project:
                self._expenditures_not_created += 1
                self.writeMessage('No project found for GEFid:%s' % gef_id)
                continue
            imis_num = row['IMISNumber']
            fmi = self.getFMIbyIMISnumber(project, imis_num)
            if not fmi:
                self._expenditures_not_created += 1
                self.writeMessage('No FMI found for IMIS:%s' % imis_num)
                continue
            self.writeMessage('Updating FMI expenditures.')
            self.updateFields(fmi, row)
            transaction.commit()
            self.writeMessage('Done updating FMI expenditures.')
            count = self._expenditures_created + self._expenditures_not_created
            self.writeProgressLine(count)

        msg = "FMI expenditures created:%s" % self._expenditures_created
        self._result_lines.append(msg)
        msg = "FMI expenditures NOT created:%s" % self._expenditures_not_created
        self._result_lines.append(msg)
        self.writeRedirectUrl()

    def getFMIbyIMISnumber(self, project, imis_num):
        container = project['fmi_folder']
        query = {'portal_type' : 'Financials',
                 'IMISNumber': imis_num,
                 'path' : {'query' : '/'.join(container.getPhysicalPath())},
                }
        brains = self._pc(**query)
        if len(brains):
            return brains[0].getObject()
##/code-section module-footer
