# -*- coding: utf-8 -*-
#
# File: testAgency.py
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

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) 
#

from Testing import ZopeTestCase
from Products.ProjectDatabase.config import *
from Products.ProjectDatabase.tests.testPortalDatabase import testPortalDatabase

# Import the tested classes
from Products.ProjectDatabase.content.Agency import Agency

##code-section module-beforeclass #fill in your manual code here
##/code-section module-beforeclass


class testAgency(testPortalDatabase):
    """Test-cases for class(es) ."""

    ##code-section class-header_testAgency #fill in your manual code here
    ##/code-section class-header_testAgency

    def afterSetUp(self):
        pass

    # Manually created methods


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testAgency))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


