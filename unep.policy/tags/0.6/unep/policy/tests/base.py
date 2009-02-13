from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_unep_policy():
    """Set up the additional products required for the UNEP site policy
    """
    # Load zcml configuration for the for the unep.policy package
    fiveconfigure.debug_mode = True

    import unep.policy
    zcml.load_config('configure.zcml', unep.policy)
    fiveconfigure.debug_mode = False

    ztc.installPackage('unep.policy')


setup_unep_policy()
ptc.setupPloneSite(products=['unep.policy'])

class UnepPolicyTestCase(ptc.PloneTestCase):
    """Base class for all tests in the package"""
