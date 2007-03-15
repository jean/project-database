"""
This file is used to initialize the package
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2006/09/29 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"


from Globals import package_home

# CMFCore imports - we will use the imported classes during the registration process
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore import CMFCorePermissions


# Archetypes imports
# listTypes - return all registered types
# process_types - return all content types, constructors and factory type information objects
from Products.Archetypes.public import process_types, listTypes

# import constants from the config.py file
from config import SKINS_DIR, GLOBALS, PROJECTNAME
from config import ADD_CONTENT_PERMISSION
# from config import VIEW_CONTENTS_PERMISSION
import config


# make our product's skins directory available to Zope
registerDirectory(SKINS_DIR, GLOBALS)

def initialize(context):
# Import types here to register them	
    import ProjectDatabase
    import Project
    import FinancialManagementInformation
    import ProjectImplementation
    import MilestoneDates
    import SubProject
    import ProjectWorkflow
    import FmiWorkflow
    import MilestoneWorkflow
    
# put together the information that needs to be passed to ContentInit

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)
        
# register the content types (will now be available in the ZMI add menu)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    
    
