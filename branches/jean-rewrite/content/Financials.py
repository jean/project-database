# -*- coding: utf-8 -*-
#
# File: Financials.py
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
import zope
from Products.ProjectDatabase.CurrencyMixin import CurrencyMixin
from Products.ProjectDatabase.content.FinancialsMixin import FinancialsMixin
from Products.ProjectDatabase.interfaces.IFinancials import IFinancials
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.ProjectDatabase.widgets.SelectedLinesField import SelectedLinesField
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

    MoneyField(
        name='GEFTrustFund',
        widget=MoneyField._properties['widget'](
            label="GEF Trust Fund",
            label_msgid='ProjectDatabase_label_GEFTrustFund',
            i18n_domain='ProjectDatabase',
        ),
        schemata="SupplementalFinance"
    ),

    MoneyField(
        name='IDCFundAllocation',
        widget=MoneyField._properties['widget'](
            label="IDC Fund Allocation",
            label_msgid='ProjectDatabase_label_IDCFundAllocation',
            i18n_domain='ProjectDatabase',
        ),
        schemata="SupplementalFinance"
    ),

    MoneyField(
        name='SCCFAllocation',
        widget=MoneyField._properties['widget'](
            label="SCCF Allocation",
            label_msgid='ProjectDatabase_label_SCCFAllocation',
            i18n_domain='ProjectDatabase',
        ),
        schemata="SupplementalFinance"
    ),

    MoneyField(
        name='StrategicPartnership',
        widget=MoneyField._properties['widget'](
            label="Strategic Partnership",
            label_msgid='ProjectDatabase_label_StrategicPartnership',
            i18n_domain='ProjectDatabase',
        ),
        schemata="SupplementalFinance"
    ),

    MoneyField(
        name='AdaptationTrustFund',
        widget=MoneyField._properties['widget'](
            label="Adaptation Trust Fund",
            label_msgid='ProjectDatabase_label_AdaptationTrustFund',
            i18n_domain='ProjectDatabase',
        ),
        schemata="SupplementalFinance"
    ),

    MoneyField(
        name='SupplementaryUNEPAllocation',
        widget=MoneyField._properties['widget'](
            label="Supplementary UNEP Allocation",
            label_msgid='ProjectDatabase_label_SupplementaryUNEPAllocation',
            i18n_domain='ProjectDatabase',
        ),
        schemata="SupplementalFinance"
    ),

    TextField(
        name='SupplementaryUNEPAllocationRemark',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Supplementary UNEP Allocation: remark",
            label_msgid='ProjectDatabase_label_SupplementaryUNEPAllocationRemark',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        schemata="SupplementalFinance"
    ),

    ReferenceField(
        name='LeadExecutingAgency',
        widget=ReferenceField._properties['widget'](
            label="Lead Executing Agency",
            label_msgid='ProjectDatabase_label_LeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Agency',),
        schemata="Agency",
        multiValued=0,
        relationship="Financials_LeadExecutingAgency"
    ),

    ReferenceField(
        name='OtherLeadExecutingAgency',
        widget=ReferenceField._properties['widget'](
            label="Lead Executing Agency (other)",
            label_msgid='ProjectDatabase_label_OtherLeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Agency',),
        schemata="Agency",
        multiValued=0,
        relationship="Financials_OtherLeadExecutingAgency"
    ),

    ReferenceField(
        name='FundManagementOfficer',
        widget=ReferenceField._properties['widget'](
            label="Fund Management Officer",
            label_msgid='ProjectDatabase_label_FundManagementOfficer',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        schemata="Final",
        multiValued=0,
        relationship="Financials_FundManagementOfficer"
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
        schemata="Final"
    ),

    ComputedField(
        name='CashUNEPAllocation',
        widget=ComputedField._properties['widget'](
            label="UNEP Allocation (Cash)",
            label_msgid='ProjectDatabase_label_CashUNEPAllocation',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Financials_schema = BaseSchema.copy() + \
    getattr(FinancialsMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Financials(BaseContent, CurrencyMixin, FinancialsMixin):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),) + (getattr(CurrencyMixin,'__implements__',()),) + (getattr(FinancialsMixin,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IFinancials)

    # This name appears in the 'add' box
    archetype_name = 'Project Financial Information'

    meta_type = 'Financials'
    portal_type = 'Financials'
    allowed_content_types = [] + list(getattr(FinancialsMixin, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Financials.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Project Financial Information"
    typeDescMsgId = 'description_edit_financials'

    _at_rename_after_creation = True

    schema = Financials_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getCashUNEPAllocation')
    def getCashUNEPAllocation(self):
        """
        """
        return 0
        return self.getGEFTrustFund() + self.getIDCFundAllocation() + self.getSCCFAllocation() + self.getStrategicPartnership() + self.getAdaptationTrustFund()


registerType(Financials, PROJECTNAME)
# end of class Financials

##code-section module-footer #fill in your manual code here
##/code-section module-footer



