# -*- coding: utf-8 -*-
#
# File: BlankCoreMixin.py
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

schema = Schema((

    TextField(
        name='SummaryDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Project Description",
            label_msgid='ProjectDatabase_label_SummaryDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='UNEPComponentDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="UNEP Component Description",
            label_msgid='ProjectDatabase_label_UNEPComponentDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
    ),
    MoneyField(
        name='ImplementingAgencyFee',
        widget=MoneyField._properties['widget'](
            label="Implementing Agency Fee",
            label_msgid='ProjectDatabase_label_ImplementingAgencyFee',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='UNEPImplementingAgencyFee',
        widget=MoneyField._properties['widget'](
            label="UNEP Implementing Agency Fee",
            label_msgid='ProjectDatabase_label_UNEPImplementingAgencyFee',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='ImplementationStatus',
        widget=SelectionWidget(
            label="Implementation Status",
            label_msgid='ProjectDatabase_label_ImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationStatus"""),
    ),
    StringField(
        name='ImplementationMode',
        widget=SelectionWidget(
            label="Implementation Mode",
            label_msgid='ProjectDatabase_label_ImplementationMode',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationMode"""),
    ),
    StringField(
        name='Office',
        widget=StringField._properties['widget'](
            label='Office',
            label_msgid='ProjectDatabase_label_Office',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='MidtermReviewReportDate',
        widget=DateTimeField._properties['widget'](
            label="Mid-term Review Report Date",
            label_msgid='ProjectDatabase_label_MidtermReviewReportDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='TerminalEvaluationReportDate',
        widget=DateTimeField._properties['widget'](
            label="Terminal Evaluation Report Date",
            label_msgid='ProjectDatabase_label_TerminalEvaluationReportDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='ProjectResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Actual Overall Project Results",
            label_msgid='ProjectDatabase_label_ProjectResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
    ),
    MoneyField(
        name='LeveragedFinancingAmount',
        widget=MoneyField._properties['widget'](
            label="Leveraged Financing Amount",
            label_msgid='ProjectDatabase_label_LeveragedFinancingAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalGEFAllocation',
        widget=ComputedField._properties['widget'](
            label="Total GEF Allocation",
            label_msgid='ProjectDatabase_label_TotalGEFAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalUNEPAllocation',
        widget=ComputedField._properties['widget'](
            label="Total UNEP Allocation",
            label_msgid='ProjectDatabase_label_TotalUNEPAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCofinancingPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing Planned",
            label_msgid='ProjectDatabase_label_TotalCofinancingPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCofinancingActual',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing Actual",
            label_msgid='ProjectDatabase_label_TotalCofinancingActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='TotalProjectCostPlanned',
        widget=MoneyField._properties['widget'](
            label="Total Project Cost Planned",
            label_msgid='ProjectDatabase_label_TotalProjectCostPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='TotalProjectCostActual',
        widget=MoneyField._properties['widget'](
            label="Total Project Cost Actual",
            label_msgid='ProjectDatabase_label_TotalProjectCostActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='ApprovedUNEPBudget',
        widget=MoneyField._properties['widget'](
            label="Approved UNEP Budget",
            label_msgid='ProjectDatabase_label_ApprovedUNEPBudget',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='CashDisbursement',
        widget=DataGridField._properties['widget'](
            columns={ 'cash_disbursements_date' : Column("Date"), 'cash_disbursements_amount' : Column("Amount"), 'cash_disbursements_bank_ref_number' : Column("Bank Reference Number") },
            label="Cash Disbursement",
            label_msgid='ProjectDatabase_label_CashDisbursement',
            i18n_domain='ProjectDatabase',
        ),
        columns=("cash_disbursements_date", "cash_disbursements_amount", "cash_disbursements_bank_ref_number"),
    ),
    MoneyField(
        name='TotalDisbursement',
        widget=MoneyField._properties['widget'](
            label="Total Disbursement",
            label_msgid='ProjectDatabase_label_TotalDisbursement',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='TotalIMISExpenditures',
        widget=MoneyField._properties['widget'](
            label="Total IMIS Expenditures",
            label_msgid='ProjectDatabase_label_TotalIMISExpenditures',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='Status',
        widget=SelectionWidget(
            label='Status',
            label_msgid='ProjectDatabase_label_Status',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Status"""),
    ),
    ComputedField(
        name='SumIMISExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total IMIS Expenditures",
            label_msgid='ProjectDatabase_label_SumIMISExpenditures',
            i18n_domain='ProjectDatabase',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BlankCoreMixin_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BlankCoreMixin(BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IBlankCoreMixin)

    meta_type = 'BlankCoreMixin'
    _at_rename_after_creation = True

    schema = BlankCoreMixin_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getTotalGEFAllocation')
    def getTotalGEFAllocation(self):
        """
        """
        pass

    security.declarePublic('getTotalUNEPAllocation')
    def getTotalUNEPAllocation(self):
        """
        """
        pass

    security.declarePublic('getTotalCofinancingPlanned')
    def getTotalCofinancingPlanned(self):
        """
        """
        pass

    security.declarePublic('getTotalCofinancingActual')
    def getTotalCofinancingActual(self):
        """
        """
        pass

    security.declarePublic('getSumIMISExpenditures')
    def getSumIMISExpenditures(self):
        """
        """
        pass


# end of class BlankCoreMixin

##code-section module-footer #fill in your manual code here
##/code-section module-footer



