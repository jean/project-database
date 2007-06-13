# -*- coding: utf-8 -*-
#
# File: BlankCoreMixin.py
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
        default_output_type='text/html'
    ),

    TextField(
        name='UNEPComponentDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="UNEP Component Description",
            label_msgid='ProjectDatabase_label_UNEPComponentDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

    MoneyField(
        name='ImplementingAgencyFee',
        widget=MoneyField._properties['widget'](
            label='Implementingagencyfee',
            label_msgid='ProjectDatabase_label_ImplementingAgencyFee',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='UNEPImplementingAgencyFee',
        widget=MoneyField._properties['widget'](
            label='Unepimplementingagencyfee',
            label_msgid='ProjectDatabase_label_UNEPImplementingAgencyFee',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='ImplementationStatus',
        widget=SelectionWidget(
            label="Implementation Status",
            label_msgid='ProjectDatabase_label_ImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationStatus""")
    ),

    StringField(
        name='ImplementationMode',
        widget=SelectionWidget(
            label="Implementation Mode",
            label_msgid='ProjectDatabase_label_ImplementationMode',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationMode""")
    ),

    StringField(
        name='Office',
        widget=StringWidget(
            label='Office',
            label_msgid='ProjectDatabase_label_Office',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='MidtermReviewReportDate',
        widget=CalendarWidget(
            label="Mid-term Review Report Date",
            label_msgid='ProjectDatabase_label_MidtermReviewReportDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='TerminalEvaluationReportDate',
        widget=CalendarWidget(
            label="Terminal Evaluation Report Date",
            label_msgid='ProjectDatabase_label_TerminalEvaluationReportDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    TextField(
        name='ProjectResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Actual Overall Project Results",
            label_msgid='ProjectDatabase_label_ProjectResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

    MoneyField(
        name='LeveragedFinancingAmount',
        widget=MoneyField._properties['widget'](
            label="Leveraged Financing Amount",
            label_msgid='ProjectDatabase_label_LeveragedFinancingAmount',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalGEFAllocation',
        widget=ComputedField._properties['widget'](
            label="Total GEF Allocation",
            label_msgid='ProjectDatabase_label_TotalGEFAllocation',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalUNEPAllocation',
        widget=ComputedField._properties['widget'](
            label="Total UNEP Allocation",
            label_msgid='ProjectDatabase_label_TotalUNEPAllocation',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalCofinancingPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing Planned",
            label_msgid='ProjectDatabase_label_TotalCofinancingPlanned',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalCofinancingActual',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing Actual",
            label_msgid='ProjectDatabase_label_TotalCofinancingActual',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='TotalProjectCostPlanned',
        widget=MoneyField._properties['widget'](
            label="Total Project Cost Planned",
            label_msgid='ProjectDatabase_label_TotalProjectCostPlanned',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='TotalProjectCostActual',
        widget=MoneyField._properties['widget'](
            label="Total Project Cost Actual",
            label_msgid='ProjectDatabase_label_TotalProjectCostActual',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='ApprovedUNEPBudget',
        widget=MoneyField._properties['widget'](
            label="Approved UNEP Budget",
            label_msgid='ProjectDatabase_label_ApprovedUNEPBudget',
            i18n_domain='ProjectDatabase',
        )
    ),

    DataGridField(
        name='CashDisbursement',
        widget=DataGridField._properties['widget'](
            columns={ 'cash_disbursements_date' : Column("Date"), 'cash_disbursements_amount' : Column("Amount"), 'cash_disbursements_bank_ref_number' : Column("Bank Reference Number") },
            label="Cash Disbursement",
            label_msgid='ProjectDatabase_label_CashDisbursement',
            i18n_domain='ProjectDatabase',
        ),
        columns=("cash_disbursements_date", "cash_disbursements_amount", "cash_disbursements_bank_ref_number")
    ),

    MoneyField(
        name='TotalDisbursement',
        widget=MoneyField._properties['widget'](
            label="Total Disbursement",
            label_msgid='ProjectDatabase_label_TotalDisbursement',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='TotalIMISExpenditures',
        widget=MoneyField._properties['widget'](
            label="Total IMIS Expenditures",
            label_msgid='ProjectDatabase_label_TotalIMISExpenditures',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='Status',
        widget=SelectionWidget(
            label='Status',
            label_msgid='ProjectDatabase_label_Status',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Status""")
    ),

    ComputedField(
        name='SumIMISExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total IMIS Expenditures",
            label_msgid='ProjectDatabase_label_SumIMISExpenditures',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BlankCoreMixin_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BlankCoreMixin:
    """
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'BlankCoreMixin'

    meta_type = 'BlankCoreMixin'
    portal_type = 'BlankCoreMixin'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'BlankCoreMixin.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "BlankCoreMixin"
    typeDescMsgId = 'description_edit_blankcoremixin'

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



