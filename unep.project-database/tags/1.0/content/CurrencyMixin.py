# -*- coding: utf-8 -*-
#
# File: CurrencyMixin.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

from Products.FinanceFields.Money import Money
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from zope.interface import implements

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary

class CurrencyMixin:
    """
    """

    ##code-section class-header_CurrencyMixin #fill in your manual code here
    ##/code-section class-header_CurrencyMixin

    def getZeroMoneyInstance(self):
        return Money(0, self.getDefaultCurrency())

    def getDefaultCurrency(self):
        pt = getToolByName(self, 'portal_properties')
        # return pt.financial_properties.default_currency
        return 'USD'


##code-section module-footer #fill in your manual code here
##/code-section module-footer

