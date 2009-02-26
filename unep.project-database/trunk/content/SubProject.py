# -*- coding: utf-8 -*-
#
# File: SubProject.py
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
import ProjectGeneralInformation
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
from DateTime import DateTime
from Products.FinanceFields.Money import Money
from Products.ProjectDatabase.utils import getYearVocabulary as getAnnualVocabulary
from Products.DataGridField import MoneyColumn, ReferenceColumn

datagrid_schema = Schema((

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
        name='FinanceCategory',
        widget=ComputedField._properties['widget'](
            label="Financial Category",
            label_msgid='ProjectDatabase_label_FinanceCategory',
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
    DataGridField(
        name='SubProjectExecutingAgency',
        widget=DataGridField._properties['widget'](
            columns={'executing_agency':ReferenceColumn('Executing Agency', fieldname='ExecutingAgencyName'),'executing_agency_category':SelectColumn('Category', vocabulary='getCategoryVocabulary')},
            label="Lead Executing Agency",
            label_msgid='ProjectDatabase_label_SubProjectExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=('executing_agency','executing_agency_category'),
    ),
    MoneyField(
        name='CommittedGrant',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="Committed Grant",
            label_msgid='ProjectDatabase_label_CommittedGrant',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='CoFinancingCash',
        widget=DataGridField._properties['widget'](
            columns={ 'cofinancing_cash_source' : SelectColumn("Source", vocabulary="getDonorTypesVocabulary"), 'cofinancing_cash_donor_name' : Column("Name of donor"), 'cofinancing_cash_planned_amount' : MoneyColumn("Planned Amount", field=datagrid_schema['cofinancing_cash_planned_amount']), 'cofinancing_cash_actual_amount' : MoneyColumn("Actual Amount", field=datagrid_schema['cofinancing_cash_actual_amount']) },
            label="Cofinancing: Cash",
            label_msgid='ProjectDatabase_label_CoFinancingCash',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("cofinancing_cash_source", "cofinancing_cash_donor_name", "cofinancing_cash_planned_amount", "cofinancing_cash_actual_amount"),
    ),
    DataGridField(
        name='CoFinancingInKind',
        widget=DataGridField._properties['widget'](
            columns={ 'cofinancing_inkind_source' : SelectColumn("Source", vocabulary="getDonorTypesVocabulary"), 'cofinancing_inkind_donor_name' : Column("Name of donor"), 'cofinancing_inkind_planned_amount' : MoneyColumn("Planned Amount", field=datagrid_schema['cofinancing_inkind_planned_amount']), 'cofinancing_inkind_actual_amount' : MoneyColumn("Actual Amount", field=datagrid_schema['cofinancing_inkind_actual_amount']) },
            label="Cofinancing: In Kind",
            label_msgid='ProjectDatabase_label_CoFinancingInKind',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("cofinancing_inkind_source", "cofinancing_inkind_donor_name", "cofinancing_inkind_planned_amount", "cofinancing_inkind_actual_amount"),
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
        name='TotalCostOfSubProjectPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Sub Project (Planned)",
            label_msgid='ProjectDatabase_label_TotalCostOfSubProjectPlanned',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    ComputedField(
        name='TotalCostOfSubProjectActual',
        widget=ComputedField._properties['widget'](
            label="Total Cost of Sub Project (Actual)",
            label_msgid='ProjectDatabase_label_TotalCostOfSubProjectActual',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='CashDisbursements',
        widget=DataGridField._properties['widget'](
            columns={ 'cash_disbursements_date' : CalendarColumn("Date"), 'cash_disbursements_amount' : MoneyColumn("Amount", field=datagrid_schema['cash_disbursements_amount']), 'cash_disbursements_imis_rcpt_number' : Column("IMIS RCPT Number") },
            label="Cash Disbursements",
            label_msgid='ProjectDatabase_label_CashDisbursements',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("cash_disbursements_date", "cash_disbursements_amount", "cash_disbursements_imis_rcpt_number"),
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
            columns={ 'year' : SelectColumn("Year", vocabulary='getYearVocabulary'), 'amount' : MoneyColumn("Amount", field=datagrid_schema['amount']) },
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
            label="Total Sub-Project Expenditures",
            label_msgid='ProjectDatabase_label_SumYearlyExpenditures',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    StringField(
        name='Status',
        widget=SelectionWidget(
            label="Sub Project Status",
            label_msgid='ProjectDatabase_label_Status',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        vocabulary=NamedVocabulary("""Status"""),
    ),
    TextField(
        name='FinancialStatusRemarks',
        widget=TextAreaWidget(
            label="Sub Project Financial Status – Remarks",
            label_msgid='ProjectDatabase_label_FinancialStatusRemarks',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    IntegerField(
        name='PlannedDuration',
        widget=IntegerField._properties['widget'](
            label="Planned Duration",
            label_msgid='ProjectDatabase_label_PlannedDuration',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DateTimeField(
        name='InitialCompletionDate',
        widget=DateTimeField._properties['widget'](
            label="Initial Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_InitialCompletionDate',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DateTimeField(
        name='RevisedCompletionDate',
        widget=DateTimeField._properties['widget'](
            label="Revised Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_RevisedCompletionDate',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    TextField(
        name='DelayReason',
        widget=TextAreaWidget(
            label="Reasons for Delay",
            label_msgid='ProjectDatabase_label_DelayReason',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
    ),
    DataGridField(
        name='Reports',
        widget=DataGridField._properties['widget'](
            columns={ 'report_type' : SelectColumn("Report Type", vocabulary="getReportTypesVocabulary"), 'report_period' : SelectColumn("Report Period", vocabulary="getYearVocabulary"), 'report_received_date' : CalendarColumn("Report Received Date"), 'amount' : MoneyColumn("Amount", field=datagrid_schema['amount']) },
            label='Reports',
            label_msgid='ProjectDatabase_label_Reports',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("report_type", "report_period", "report_received_date", "amount"),
    ),
    DataGridField(
        name='SubProjectRevision',
        widget=DataGridField._properties['widget'](
            columns={"revision_number":Column("Revision Number"), "revision_type":SelectColumn("Revision Type", vocabulary="getRevisionTypeVocabulary"),"revision_date":CalendarColumn("Revision Date")},
            label="Sub Project Revision",
            label_msgid='ProjectDatabase_label_SubProjectRevision',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns=("revision_number", "revision_type","revision_date"),
    ),
    DataGridField(
        name='ExecutingAgencyRiskRating',
        widget=DataGridField._properties['widget'](
            columns= {'Risk_Level':SelectColumn("Risk Level", vocabulary='getRiskLevelVocabulary'), "Assessment_Date":CalendarColumn("Assessment Date"), 'Remarks':Column("Remarks")},
            label="Agency Risk Rating",
            label_msgid='ProjectDatabase_label_ExecutingAgencyRiskRating',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="FMO",
        columns= ("Risk_Level", "Assessment_Date", "Remarks"),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

SubProject_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
SubProject_schema['title'].widget.label = 'Sub-Project Title'

SubProject_schema = SubProject_schema.copy()  + Schema((

    ReferenceField("fakeExecutingAgencyName",
            widget = ReferenceBrowserWidget(
                label="Executing Agency",
                visible={'edit':'hidden', 'view':'invisible'},
                startup_directory='/contacts',
            ),
            allowed_types=('Organisation',),
            relationship='subproj_executingagency_fake',
            multiValued=0,
        ),
    ))
##/code-section after-schema

class SubProject(BaseContent, CurrencyMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ISubProject)

    meta_type = 'SubProject'
    _at_rename_after_creation = True

    schema = SubProject_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    security.declarePublic('getCategoryVocabulary')
    def getCategoryVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('Category')
        return vocab.getDisplayList(self)

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

    security.declarePublic('getRevisionTypeVocabulary')
    def getRevisionTypeVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('ProjectRevisionType')
        return vocab.getDisplayList(self)

    security.declarePublic('getRiskLevelVocabulary')
    def getRiskLevelVocabulary(self):
        """
        """
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName('RiskLevel')
        return vocab.getDisplayList(self)

    security.declarePublic('getFinanceCategory')
    def getFinanceCategory(self):
        return self.aq_parent.getFinanceCategory()

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
    def getSumYearlyExpenditures(self):
        """
        """
        values = self.getYearlyExpenditures()
        return self._computeDataGridAmount( \
            [v['amount'] for v in values if v['amount']])
    def getTotalCostOfSubProjectPlanned(self):
        """
        """
        total = self.getCommittedGrant()
        if self.getSumCoFinCashPlanned():
            total += self.getSumCoFinCashPlanned()
        if self.getSumCoFinInKindPlanned():
            total += self.getSumCoFinInKindPlanned()
        return total

    def getTotalCostOfSubProjectActual(self):
        """
        """
        total = self.getSumYearlyExpenditures()
        if self.getSumCoFinCashActual():
            total += self.getSumCoFinCashActual()
        if self.getSumCoFinInKindActual():
            total += self.getSumCoFinInKindActual()
        return total

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

    def getLeadExecutingAgencyNames(self):
        lead = self.getSubProjectExecutingAgency()
        result = ''
        if lead:
            for v in lead:
                if v['executing_agency']:
                    result += v['executing_agency'] + ', '
            return result[:-2]
        return 'Unspecified'

    def getYearVocabulary(self):
        return getAnnualVocabulary()



registerType(SubProject, PROJECTNAME)
# end of class SubProject

##code-section module-footer #fill in your manual code here
##/code-section module-footer



