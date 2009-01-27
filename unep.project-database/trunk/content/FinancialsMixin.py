# -*- coding: utf-8 -*-
#
# File: FinancialsMixin.py
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
        amount = self.getMoneyFieldDefault()
        for v in column:
            if v:
                amount += v
        return amount

    security.declarePublic('getMoneyFieldDefault')
    def getMoneyFieldDefault(self):
        """
        """
        properties = getToolByName(self, 'portal_properties')
        default_currency = properties.financial_properties.default_currency
        return Money(0, default_currency)
        #return self.getZeroMoneyInstance()

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
            # total = self.getZeroMoneyInstance()
            total = self.getMoneyFieldDefault()
            if self.getSumCofinCashPlanned():
                total += self.getSumCofinCashPlanned()
            if self.getSumCofinInKindPlanned():
                total += self.getSumCofinInKindPlanned()

        else:
            # return self.getZeroMoneyInstance()
            return self.getMoneyFieldDefault()

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
            # total = self.getZeroMoneyInstance()
            total = self.getMoneyFieldDefault()
            if self.getSumCofinCashActual():
                total += self.getSumCofinCashActual()
            if self.getSumCofinInKindActual():
                total += self.getSumCofinInKindActual()
            return total
        else:
            # return self.getZeroMoneyInstance()
            return self.getMoneyFieldDefault()

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
        revAllocUNEP = self.getRevisedAllocationToUNEP()
        committedGEFgrant = self.getCommittedGEFGrant()
        if (revAllocUNEP is not None) and (committedGEFgrant is not None):
            return revAllocUNEP - committedGEFgrant
        return self.getMoneyFieldDefault()

    # Manually created methods

    security.declarePublic('validate_CashDisbursements')
    def validate_CashDisbursements(self, value):
        """
        """
        request = self.REQUEST
        total_cost = self.computeDataGridAmount([v['cash_disbursements_amount'] for v in value if v['cash_disbursements_amount']])
        # total = self.getZeroMoneyInstance()
        total = self.getMoneyFieldDefault()
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



