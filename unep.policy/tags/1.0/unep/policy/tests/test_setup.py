import unittest
from unep.policy.tests.base import UnepPolicyTestCase

class TestSetup(UnepPolicyTestCase):

    def test_portal_title(self):
        self.assertEquals('UNEP Project Database', self.portal.getProperty('title'))

    def test_portal_description(self):
        self.assertEquals('Welcome to the UNEP Project Database.', self.portal.getProperty('description'))

    def test_portal_mail_from(self):
        self.assertEquals('jurgen@upfrontsystems.co.za', self.portal.getProperty('email_from_address'))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
