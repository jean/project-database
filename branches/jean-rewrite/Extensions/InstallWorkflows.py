# -*- coding: utf-8 -*-
#
# File: ProjectDatabase.py
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


from Products.CMFCore.utils import getToolByName
from Products.ExternalMethod.ExternalMethod import ExternalMethod

##code-section module-header #fill in your manual code here
##/code-section module-header

def installWorkflows(self, package, out):
    """Install the custom workflows for this product."""

    productname = 'ProjectDatabase'
    workflowTool = getToolByName(self, 'portal_workflow')

    ourProductWorkflow = ExternalMethod('temp', 'temp',
                                        productname+'.'+'State_Machine_1',
                                        'createState_Machine_1')
    workflow = ourProductWorkflow(self, 'State_Machine_1')
    if 'State_Machine_1' in workflowTool.listWorkflows():
        print >> out, 'State_Machine_1 already in workflows.'
    else:
        workflowTool._setObject('State_Machine_1', workflow)
    workflowTool.setChainForPortalTypes(['Project'], workflow.getId())

    ourProductWorkflow = ExternalMethod('temp', 'temp',
                                        productname+'.'+'State_Machine_2',
                                        'createState_Machine_2')
    workflow = ourProductWorkflow(self, 'State_Machine_2')
    if 'State_Machine_2' in workflowTool.listWorkflows():
        print >> out, 'State_Machine_2 already in workflows.'
    else:
        workflowTool._setObject('State_Machine_2', workflow)
    workflowTool.setChainForPortalTypes(['Milestone'], workflow.getId())

    ourProductWorkflow = ExternalMethod('temp', 'temp',
                                        productname+'.'+'State_Machine_1',
                                        'createState_Machine_1')
    workflow = ourProductWorkflow(self, 'State_Machine_1')
    if 'State_Machine_1' in workflowTool.listWorkflows():
        print >> out, 'State_Machine_1 already in workflows.'
    else:
        workflowTool._setObject('State_Machine_1', workflow)
    workflowTool.setChainForPortalTypes(['Financials'], workflow.getId())

    ##code-section after-workflow-install #fill in your manual code here
    ##/code-section after-workflow-install

    return workflowTool

def uninstallWorkflows(self, package, out):
    """Deinstall the workflows.

    This code doesn't really do anything, but you can place custom
    code here in the protected section.
    """

    ##code-section workflow-uninstall #fill in your manual code here
    ##/code-section workflow-uninstall

    pass
