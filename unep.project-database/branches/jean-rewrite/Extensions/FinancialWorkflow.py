# -*- coding: utf-8 -*-
#
# File: ProjectDatabase.py
#
# Copyright (c) 2006 by []
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

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowTool import addWorkflowFactory
from Products.DCWorkflow.DCWorkflow import DCWorkflowDefinition
from Products.ExternalMethod.ExternalMethod import ExternalMethod
from Products.ProjectDatabase.config import *

##code-section create-workflow-module-header #fill in your manual code here
##/code-section create-workflow-module-header


productname = 'ProjectDatabase'

def setupFinancialWorkflow(self, workflow):
    """Define the FinancialWorkflow workflow.
    """
    # Add additional roles to portal
    portal = getToolByName(self,'portal_url').getPortalObject()
    data = list(portal.__ac_roles__)
    for role in ['FmiEdit', 'ProjectEdit', 'PortfolioManager\nFmiEdit', 'PortfolioManager', 'ProjectEdit\nAnonymous']:
        if not role in data:
            data.append(role)
    portal.__ac_roles__ = tuple(data)

    workflow.setProperties(title='FinancialWorkflow')

    ##code-section create-workflow-setup-method-header #fill in your manual code here
    ##/code-section create-workflow-setup-method-header


    for s in ['pending', 'published', 'private', 'visible']:
        workflow.states.addState(s)

    for t in ['hide', 'submit', 'reject', 'retract', 'show', 'publish']:
        workflow.transitions.addTransition(t)

    for v in ['review_history', 'comments', 'time', 'actor', 'action']:
        workflow.variables.addVariable(v)

    workflow.addManagedPermission('Access contents information')
    workflow.addManagedPermission('Modify portal content')
    workflow.addManagedPermission('Change portal events')
    workflow.addManagedPermission('View')

    for l in []:
        if not l in workflow.worklists.objectValues():
            workflow.worklists.addWorklist(l)

    ## Initial State

    workflow.states.setInitialState('visible')

    ## States initialization

    stateDef = workflow.states['pending']
    stateDef.setProperties(title="""pending""",
                           description="""""",
                           transitions=['hide', 'publish', 'reject', 'retract'])
    stateDef.setPermission('Access contents information',
                           0,
                           ['FmiEdit', 'PortfolioManager\nFmiEdit', 'PortfolioManager'])
    stateDef.setPermission('Modify portal content',
                           0,
                           ['FmiEdit', 'PortfolioManager'])
    stateDef.setPermission('Change portal events',
                           0,
                           ['FmiEdit', 'PortfolioManager'])

    stateDef = workflow.states['published']
    stateDef.setProperties(title="""published""",
                           description="""""",
                           transitions=['reject', 'retract'])
    stateDef.setPermission('Access contents information',
                           0,
                           ['Anonymous', 'Manager', 'FmiEdit', 'PortfolioManager'])
    stateDef.setPermission('Modify portal content',
                           0,
                           ['Manager', 'FmiEdit', 'PortfolioManager'])
    stateDef.setPermission('View',
                           0,
                           ['Anonymous', 'Manager', 'FmiEdit', 'PortfolioManager'])
    stateDef.setPermission('Change portal events',
                           0,
                           ['Manager', 'FmiEdit', 'PortfolioManager'])

    stateDef = workflow.states['private']
    stateDef.setProperties(title="""private""",
                           description="""""",
                           transitions=['show'])
    stateDef.setPermission('Access contents information',
                           0,
                           ['Manager', 'Owner', 'FmiEdit', 'PortfolioManager'])
    stateDef.setPermission('Modify portal content',
                           0,
                           ['Manager', 'Owner', 'FmiEdit', 'PortfolioManager'])
    stateDef.setPermission('View',
                           0,
                           ['Manager', 'Owner', 'FmiEdit', 'PortfolioManager'])
    stateDef.setPermission('Change portal events',
                           0,
                           ['Manager', 'Owner', 'FmiEdit', 'PortfolioManager'])

    stateDef = workflow.states['visible']
    stateDef.setProperties(title="""visible""",
                           description="""""",
                           transitions=['submit', 'publish'])
    stateDef.setPermission('Access contents information',
                           0,
                           ['Anonymous', 'Manager', 'Reviewer', 'FmiEdit', 'PortfolioManager', 'ProjectEdit\nAnonymous', 'Manager', 'Reviewer', 'FmiEdit', 'PortfolioManager', 'ProjectEdit'])
    stateDef.setPermission('Modify portal content',
                           0,
                           ['Manager', 'Owner', 'FmiEdit', 'PortfolioManager', 'ProjectEdit'])
    stateDef.setPermission('Change portal events',
                           0,
                           ['Manager', 'Owner', 'FmiEdit', 'PortfolioManager', 'ProjectEdit'])

    ## Transitions initialization

    transitionDef = workflow.transitions['hide']
    transitionDef.setProperties(title="""hide""",
                                new_state_id="""private""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""hide""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={'guard_roles': 'FmiEdit'},
                                )

    transitionDef = workflow.transitions['submit']
    transitionDef.setProperties(title="""submit""",
                                new_state_id="""pending""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""submit""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={'guard_roles': 'FmiEdit; ProjectEdit'},
                                )

    transitionDef = workflow.transitions['reject']
    transitionDef.setProperties(title="""reject""",
                                new_state_id="""visible""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""reject""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={},
                                )

    transitionDef = workflow.transitions['retract']
    transitionDef.setProperties(title="""retract""",
                                new_state_id="""visible""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""retract""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={},
                                )

    transitionDef = workflow.transitions['show']
    transitionDef.setProperties(title="""show""",
                                new_state_id="""pending""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""show""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={'guard_roles': 'FmiEdit'},
                                )

    transitionDef = workflow.transitions['publish']
    transitionDef.setProperties(title="""publish""",
                                new_state_id="""published""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""publish""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={'guard_permissions': 'Review portal content', 'guard_roles': 'FmiEdit'},
                                )

    ## State Variable
    workflow.variables.setStateVar('review_state')

    ## Variables initialization
    variableDef = workflow.variables['review_history']
    variableDef.setProperties(description="""Provides access to workflow history""",
                              default_value="""""",
                              default_expr="""state_change/getHistory""",
                              for_catalog=0,
                              for_status=0,
                              update_always=0,
                              props={'guard_permissions': 'Request review; Review portal content'})

    variableDef = workflow.variables['comments']
    variableDef.setProperties(description="""Comments about the last transition""",
                              default_value="""""",
                              default_expr="""python:state_change.kwargs.get('comment', '')""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    variableDef = workflow.variables['time']
    variableDef.setProperties(description="""Time of the last transition""",
                              default_value="""""",
                              default_expr="""state_change/getDateTime""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    variableDef = workflow.variables['actor']
    variableDef.setProperties(description="""The ID of the user who performed the last transition""",
                              default_value="""""",
                              default_expr="""user/getId""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    variableDef = workflow.variables['action']
    variableDef.setProperties(description="""The last transition""",
                              default_value="""""",
                              default_expr="""transition/getId|nothing""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    ## Worklists Initialization


    # WARNING: below protected section is deprecated.
    # Add a tagged value 'worklist' with the worklist name to your state(s) instead.

    ##code-section create-workflow-setup-method-footer #fill in your manual code here
    ##/code-section create-workflow-setup-method-footer



def createFinancialWorkflow(self, id):
    """Create the workflow for ProjectDatabase.
    """

    ob = DCWorkflowDefinition(id)
    setupFinancialWorkflow(self, ob)
    return ob

addWorkflowFactory(createFinancialWorkflow,
                   id='FinancialWorkflow',
                   title='FinancialWorkflow')

##code-section create-workflow-module-footer #fill in your manual code here
##/code-section create-workflow-module-footer

