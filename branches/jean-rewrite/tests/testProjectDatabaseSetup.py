# -*- coding: utf-8 -*-
#
# File: testProjectDatabaseSetup.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.5.1-svn
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
# Setup tests
#

import os, sys
from Testing import ZopeTestCase

class testProjectDatabaseSetup:
    """Test cases for the generic setup of the product."""

    ##code-section class-header_testProjectDatabaseSetup #fill in your manual code here
    ##/code-section class-header_testProjectDatabaseSetup

    def afterSetUp(self):
        ids = self.portal.objectIds()

    def test_tools(self):
        ids = self.portal.objectIds()
        self.failUnless('archetype_tool' in ids)

    def test_types(self):
        ids = self.portal.portal_types.objectIds()
        self.failUnless('Document' in ids)

    def test_skins(self):
        ids = self.portal.portal_skins.objectIds()
        self.failUnless('plone_templates' in ids)

    def test_workflows(self):
        ids = self.portal.portal_workflow.objectIds()
        self.failUnless('plone_workflow' in ids)

    def test_workflowChains(self):
        getChain = self.portal.portal_workflow.getChainForPortalType
        self.failUnless('plone_workflow' in getChain('Document'))

    # Manually created methods


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testProjectDatabaseSetup))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


