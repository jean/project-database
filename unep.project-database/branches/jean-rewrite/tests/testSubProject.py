# -*- coding: utf-8 -*-
#
# File: testSubProject.py
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

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) SubProject
#

from Testing import ZopeTestCase
from Products.ProjectDatabase.config import *
from Products.ProjectDatabase.tests.PortalDatabaseTestCase import PortalDatabaseTestCase

# Import the tested classes
from Products.ProjectDatabase.content.SubProject import SubProject

##code-section module-beforeclass #fill in your manual code here
##/code-section module-beforeclass


class testSubProject(PortalDatabaseTestCase):
    """Test-cases for class(es) SubProject."""

    ##code-section class-header_testSubProject #fill in your manual code here
    ##/code-section class-header_testSubProject

    def afterSetUp(self):
        pass

    # from class CurrencyMixin:
    def test_getZeroMoneyInstance(self):
        pass

    # from class CurrencyMixin:
    def test_getDefaultCurrency(self):
        pass

    # from class FinancialsMixin:
    def test_getDonorTypesVocabulary(self):
        pass

    # from class FinancialsMixin:
    def test_getReportTypesVocabulary(self):
        pass

    # from class FinancialsMixin:
    def test_computeDataGridAmount(self):
        pass

    # from class FinancialsMixin:
    def test_getMoneyFieldDefault(self):
        pass

    # from class FinancialsMixin:
    def test_getSumCofinCashPlanned(self):
        pass

    # from class FinancialsMixin:
    def test_getSumCofinActual(self):
        pass

    # from class FinancialsMixin:
    def test_getSumCofinInKindPlanned(self):
        pass

    # from class FinancialsMixin:
    def test_getSumCofinInKindActual(self):
        pass

    # from class FinancialsMixin:
    def test_getSumCashDisbursements(self):
        pass

    # from class FinancialsMixin:
    def test_getSumIMISExpenditures(self):
        pass

    # from class FinancialsMixin:
    def test_getTotalCostOfProjectStagePlanned(self):
        pass

    # from class FinancialsMixin:
    def test_getTotalCostOfProjectStageActual(self):
        pass

    # from class FinancialsMixin:
    def test_getRevisionTypeVocabulary(self):
        pass

    # Manually created methods

    def test_getSubProjectCofinCashActual(self):
        pass


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testSubProject))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


