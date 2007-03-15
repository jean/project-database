"""
permissions: Permissions used in the Project Database
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2006/09/29 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"


# Import function that wiil allow us to set roles for the permissions we define
from Products.CMFCore.CMFCorePermissions import setDefaultRoles

# define add and edit permissions for all the ProjectDatabase types 
AddProject = 'Add projects'
EditProject = 'Edit projects'
AddSubProject = 'Add sub projects'
EditSubProject = 'Edit sub projects'
AddProjectImplementation = 'Add project implementation'
EditProjectImplementation = 'Edit project implementation'
AddFinancialManagementInformation = 'Add fmi'
EditFinancialManagementInformation = 'Edit fmi'
AddMilestoneDates = 'Add milestone dates'
EditMilestoneDates = 'Edit milestone dates'
ViewProjects = 'Projects-View'

# Set up default roles for the permissions defined above
setDefaultRoles(AddProject, ('ProjectEdit', 'PortfolioManager'))
setDefaultRoles(EditProject, ('ProjectEdit', 'PortfolioManager',))
setDefaultRoles(AddSubProject, ('ProjectEdit', 'PortfolioManager'))
setDefaultRoles(EditSubProject, ('ProjectEdit', 'PortfolioManager'))
setDefaultRoles(AddProjectImplementation, ('ProjectEdit', 'PortfolioManager'))
setDefaultRoles(EditProjectImplementation, ('ProjectEdit', 'PortfolioManager'))
setDefaultRoles(AddFinancialManagementInformation, ('ProjectEdit', 'PortfolioManager', 'FmiEdit'))
setDefaultRoles(EditFinancialManagementInformation, ('ProjectEdit', 'PortfolioManager', 'FmiEdit'))
setDefaultRoles(AddMilestoneDates, ('MilestoneEdit', 'PortfolioManager'))
setDefaultRoles(EditMilestoneDates, ('MilestoneEdit', 'PortfolioManager'))
setDefaultRoles(ViewProjects, ('ProjectEdit','FmiEdit','MilestoneEdit', 'PortfolioManager'))
