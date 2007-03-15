# -*- coding: utf-8 -*-
#
# File: SubProject.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
import zope
from Products.ProjectDatabase.CurrencyMixin import CurrencyMixin
from Products.ProjectDatabase.content.FinancialsMixin import FinancialsMixin
from Products.ProjectDatabase.interfaces.ISubProject import ISubProject
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['SummaryDescription'] = Project.schema['SummaryDescription'].copy()
copied_fields['Country'] = Project.schema['Country'].copy()
copied_fields['Scope'] = Project.schema['Scope'].copy()
copied_fields['Region'] = Project.schema['Region'].copy()
copied_fields['ImplementationMode'] = Project.schema['ImplementationMode'].copy()
copied_fields['Office'] = Project.schema['Office'].copy()
copied_fields['Website'] = Project.schema['Website'].copy()
copied_fields['ProjectCoordinator'] = Project.schema['ProjectCoordinator'].copy()
copied_fields['ProjectCoordinator'].relationship = "SubProject_ProjectCoordinator"
copied_fields['LeadExecutingAgency'] = Financials.schema['LeadExecutingAgency'].copy()
copied_fields['LeadExecutingAgency'].relationship = "SubProject_LeadExecutingAgency"
copied_fields['OtherLeadExecutingAgency'] = Financials.schema['OtherLeadExecutingAgency'].copy()
copied_fields['OtherLeadExecutingAgency'].relationship = "SubProject_OtherLeadExecutingAgency"
schema = Schema((

    copied_fields['SummaryDescription'],

    copied_fields['Country'],

    copied_fields['Scope'],

    copied_fields['Region'],

    copied_fields['ImplementationMode'],

    copied_fields['Office'],

    copied_fields['Website'],

    copied_fields['ProjectCoordinator'],

    copied_fields['LeadExecutingAgency'],

    copied_fields['OtherLeadExecutingAgency'],

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

SubProject_schema = BaseFolderSchema.copy() + \
    getattr(FinancialsMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class SubProject(BaseFolder, CurrencyMixin, FinancialsMixin):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),) + (getattr(CurrencyMixin,'__implements__',()),) + (getattr(FinancialsMixin,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(ISubProject)

    # This name appears in the 'add' box
    archetype_name = 'SubProject'

    meta_type = 'SubProject'
    portal_type = 'SubProject'
    allowed_content_types = ['ProjectImplementation'] + list(getattr(FinancialsMixin, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'SubProject.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "SubProject"
    typeDescMsgId = 'description_edit_subproject'

    _at_rename_after_creation = True

    schema = SubProject_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(SubProject, PROJECTNAME)
# end of class SubProject

##code-section module-footer #fill in your manual code here
##/code-section module-footer



