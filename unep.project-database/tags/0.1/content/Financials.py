# -*- coding: utf-8 -*-
#
# File: Financials.py
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
    ComputedField(
        name='CashUNEPAllocation',
        widget=ComputedField._properties['widget'](
            label="GEF Allocation to UNEP",
            label_msgid='ProjectDatabase_label_CashUNEPAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='GEFTrustFund',
        widget=MoneyField._properties['widget'](
            label="GEF Trust Fund",
            label_msgid='ProjectDatabase_label_GEFTrustFund',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='LDCFundAllocation',
        widget=MoneyField._properties['widget'](
            label="LDC Fund Allocation",
            label_msgid='ProjectDatabase_label_LDCFundAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='SCCFAllocation',
        widget=MoneyField._properties['widget'](
            label="SCCF Allocation",
            label_msgid='ProjectDatabase_label_SCCFAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='StrategicPartnership',
        widget=MoneyField._properties['widget'](
            label="Strategic Partnership",
            label_msgid='ProjectDatabase_label_StrategicPartnership',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='AdaptationTrustFund',
        widget=MoneyField._properties['widget'](
            label="Adaptation Trust Fund",
            label_msgid='ProjectDatabase_label_AdaptationTrustFund',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='SupplementaryUNEPAllocation',
        widget=MoneyField._properties['widget'](
            label="Supplementary Allocation to UNEP",
            label_msgid='ProjectDatabase_label_SupplementaryUNEPAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='SupplementaryUNEPAllocationRemark',
        widget=TextAreaWidget(
            label="Supplementary Allocation to UNEP: remark",
            label_msgid='ProjectDatabase_label_SupplementaryUNEPAllocationRemark',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='ActualTotalExpenditures',
        widget=MoneyField._properties['widget'](
            label="Actual Total Expenditures",
            description="The total actual expenditures against the GEF trust fund once project is completed",
            label_msgid='ProjectDatabase_label_ActualTotalExpenditures',
            description_msgid='ProjectDatabase_help_ActualTotalExpenditures',
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
    ReferenceField(
        name='FundManagementOfficer',
        widget=ReferenceBrowserWidget(
            label="Fund Management Officer",
            label_msgid='ProjectDatabase_label_FundManagementOfficer',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=0,
        relationship="Financials_FundManagementOfficer",
        allowed_types=('Person',),
    ),
    TextField(
        name='PDFResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="PDF Results",
            label_msgid='ProjectDatabase_label_PDFResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
    ),
    MoneyField(
        name='TerminalEvaluationBudget',
        widget=MoneyField._properties['widget'](
            label="Project Terminal Evaluation Budget",
            label_msgid='ProjectDatabase_label_TerminalEvaluationBudget',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='MidTermEvaluationBudget',
        widget=MoneyField._properties['widget'](
            label="Project Mid-term Review Budget",
            label_msgid='ProjectDatabase_label_MidTermEvaluationBudget',
            i18n_domain='ProjectDatabase',
        ),
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



