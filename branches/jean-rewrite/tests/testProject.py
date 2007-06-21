# -*- coding: utf-8 -*-
#
# File: testProject.py
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
# Test-cases for class(es) Project
#

from Testing import ZopeTestCase
from Products.ProjectDatabase.config import *
from Products.ProjectDatabase.tests.PortalDatabaseTestCase import PortalDatabaseTestCase

# Import the tested classes
from Products.ProjectDatabase.content.Project import Project

##code-section module-beforeclass #fill in your manual code here
##/code-section module-beforeclass


class testProject(PortalDatabaseTestCase):
    """Test-cases for class(es) Project."""

    ##code-section class-header_testProject #fill in your manual code here
    ##/code-section class-header_testProject

    def afterSetUp(self):
        pass

    # from class Project:
    def test_getTotalGEFAllocation(self):
        pass

    # from class Project:
    def test_getTotalUNEPAllocation(self):
        pass

    # from class Project:
    def test_getTotalCofinancingPlanned(self):
        pass

    # from class Project:
    def test_getTotalCofinancingActual(self):
        pass

    # from class Project:
    def test_getTotalCashDisbursements(self):
        pass

    # from class Project:
    def test_getTotalIMISExpenditures(self):
        pass

    # from class Project:
    def test_getPDFAStatus(self):
        pass

    # from class Project:
    def test_getPDFBStatus(self):
        pass

    # from class Project:
    def test_getMSPStatus(self):
        pass

    # from class Project:
    def test_getFSPStatus(self):
        pass

    # from class Project:
    def test_getProjectTitle(self):
        pass

    # from class Project:
    def test_Overview(self):
        pass

    # from class Project:
    def test_project_general_information(self):
        pass

    # from class Project:
    def test_validate_TranchedNumber(self):
        pass

    # from class Project:
    def test_validate_PhasedNumber(self):
        pass

    # from class Project:
    def test_fmi_view(self):
        pass

    # from class Project:
    def test_getProject(self):
        pass

    # from class CurrencyMixin:
    def test_getZeroMoneyInstance(self):
        pass

    # from class CurrencyMixin:
    def test_getDefaultCurrency(self):
        pass

    # Manually created methods

    def test___init__(self):
        pass

    def test_project_ratings_disconnect(self):
        pass

    def test_export_project_data(self):
        pass


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testProject))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


