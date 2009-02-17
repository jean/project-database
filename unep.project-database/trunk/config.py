# -*- coding: utf-8 -*-
#
# File: ProjectDatabase.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Jean Jordaan <jean.jordaan@gmail.com>, Jurgen Blignaut
<jurgen.blignaut@gmail.com>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "ProjectDatabase"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))
ADD_CONTENT_PERMISSIONS = {
    'Project': 'ProjectDatabase: Add Project',
    'Milestone': 'ProjectDatabase: Add Milestone',
    'ProjectGeneralInformation': 'ProjectDatabase: Add ProjectGeneralInformation',
    'SubProject': 'ProjectDatabase: Add SubProject',
    'Financials': 'ProjectDatabase: Add Financials',
    'FMIFolder': 'ProjectDatabase: Add FMIFolder',
    'MOU': 'ProjectDatabase: Add MOU',
    'ProjectDatabase': 'ProjectDatabase: Add ProjectDatabase',
    'ProgrammeFramework': 'ProjectDatabase: Add ProgrammeFramework',
    'MonitoringAndEvaluation': 'ProjectDatabase: Add MonitoringAndEvaluation',
    'MandEfolder': 'ProjectDatabase: Add MandEfolder',
}

setDefaultRoles('ProjectDatabase: Add Project', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add Milestone', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add ProjectGeneralInformation', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add SubProject', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add Financials', ('Manager','Owner','FMO'))
setDefaultRoles('ProjectDatabase: Add FMIFolder', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add MOU', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add ProjectDatabase', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add ProgrammeFramework', ('Manager','Owner'))
setDefaultRoles('ProjectDatabase: Add MonitoringAndEvaluation', ('Manager','Owner','MO','EO'))
setDefaultRoles('ProjectDatabase: Add MandEfolder', ('Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from Products.ProjectDatabase.AppConfig import *
except ImportError:
    pass
