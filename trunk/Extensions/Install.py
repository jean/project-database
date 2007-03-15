"""
plone installer script
This installs the product including the product types, skins, workflows and roles
"""


__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2006/09/29 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"


from StringIO import StringIO

# import permissions for the ProjectDatabase object
from Products.CMFCore import permissions
from Products.CMFCore import CMFCorePermissions
from Products.ProjectDatabase import permissions as pjpermissions
from Products.ProjectDatabase.config import *
# from Products.ProjectDatabase.config import VIEW_CONTENTS_PERMISSION
# from Products.ProjectDatabase.config import VIEW_CONTENTS_PERMISSION as viewpermissions


# import permissions for the ProjectDatabase object
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowTool import addWorkflowFactory

# import the workflows for the ProjectDatabase object
from Products.ProjectDatabase.ProjectWorkflow import *
from Products.ProjectDatabase.FmiWorkflow import *
from Products.ProjectDatabase.MilestoneWorkflow import *


from Products.Archetypes.public import listTypes

# these two functions handle the install process
from Products.Archetypes.Extensions.utils \
     import installTypes, install_subskin

# install the other products needed
def install_dependencies(self, out):
    qi=getToolByName(self, 'portal_quickinstaller')
    qi.installProduct('ATExtensions',)
    qi.installProduct('DataGridField',)
    qi.installProduct('mxmContacts',)
    out.write("Installed other products needed.\n")


def install(self):
    out = StringIO()
    portal = getToolByName(self, 'portal_url').getPortalObject()
    
    # Add ProjectDatabase Roles to default plone site
    
    self.__ac_roles__ = ['ProjectEdit', 'PortfolioManager', 'FmiEdit', 'MilestoneEdit']
    
                        
    # Assign permissions to the relevant roles
    self.manage_permission(permissions.ModifyPortalContent, 
                          ('ProjectEdit', 'PortfolioManager','FmiEdit','MilestoneEdit'), 
                          acquire=1)
    self.manage_permission(pjpermissions.AddProject,
                          ('ProjectEdit', 'PortfolioManager'),
                          acquire=1)
    self.manage_permission(pjpermissions.EditProject,
			  ('ProjectEdit', 'PortfolioManager'),
			  acquire=1)
    self.manage_permission(pjpermissions.AddProjectImplementation,
		          ('ProjectEdit', 'PortfolioManager'),
		          acquire=1)
    self.manage_permission(pjpermissions.EditProjectImplementation,
                          ('ProjectEdit', 'PortfolioManager'),
                          acquire=1)
    self.manage_permission(pjpermissions.AddSubProject,
		          ('ProjectEdit', 'PortfolioManager'),
			  acquire=1)
    self.manage_permission(pjpermissions.EditSubProject,
		          ('ProjectEdit', 'PortfolioManager'),
			  acquire=1)
    self.manage_permission(pjpermissions.AddFinancialManagementInformation,
                          ('ProjectEdit', 'PortfolioManager', 'FmiEdit'),
                          acquire=1)
    self.manage_permission(pjpermissions.EditFinancialManagementInformation,
                          ('ProjectEdit', 'PortfolioManager', 'FmiEdit'),
                          acquire=1)
    self.manage_permission(pjpermissions.AddMilestoneDates,
                          ('ProjectEdit', 'PortfolioManager', 'MilestoneEdit'),
                          acquire=1)
    self.manage_permission(pjpermissions.EditMilestoneDates,
                          ('ProjectEdit', 'PortfolioManager', 'MilestoneEdit'),
                          acquire=1)
    self.manage_permission(pjpermissions.ViewProjects,
                          ('ProjectEdit', 'PortfolioManager', 'FmiEdit', 'MilestoneEdit'),
                          acquire=1)
        

    
    
    

     
    # Install dependencies
    install_dependencies(self, out)
    
    # Install types
    installTypes(self, out,
                 listTypes(PROJECTNAME),
                 PROJECTNAME)
    print >> out, "Successfully installed %s's content types." % PROJECTNAME
    
    # Install skins
    install_subskin(self, out, GLOBALS)
    
    # Add workflows
    wtool = self.portal_workflow
    project_workflow_id = 'ProjectWorkflow'
    project_workflow = 'ProjectWorkflow (Project Workflow)'
    fmi_workflow_id = 'FmiWorkflow'
    fmi_workflow = 'FmiWorkflow (FMI Workflow)'
    milestone_workflow_id = 'MilestoneWorkflow'
    milestone_workflow = 'MilestoneWorkflow (Milestone Workflow)'
	
    
    if project_workflow_id in wtool.objectIds():
        wtool._delObject(project_workflow_id)

    if fmi_workflow_id in wtool.objectIds():
	wtool._delObject(fmi_workflow_id)

    if milestone_workflow_id in wtool.objectIds():
        wtool._delObject(milestone_workflow_id)
		    

    wtool.manage_addWorkflow(id=project_workflow_id, workflow_type=project_workflow)
    wtool.setChainForPortalTypes(('Project',), project_workflow_id)
    wtool.setChainForPortalTypes(('ProjectImplementation',), project_workflow_id)
    wtool.setChainForPortalTypes(('SubProject',), project_workflow_id)
    wtool.manage_addWorkflow(id=fmi_workflow_id, workflow_type=fmi_workflow)
    wtool.setChainForPortalTypes(('FinancialManagementInformation',), fmi_workflow_id)
    wtool.manage_addWorkflow(id=milestone_workflow_id, workflow_type=milestone_workflow)
    wtool.setChainForPortalTypes(('MilestoneDates',), milestone_workflow_id)
    print >> out, "Successfully installed %s's workflows." % PROJECTNAME
    
	
        
    print >> out, "\nSuccessfully installed %s." % PROJECTNAME
    return out.getvalue()
