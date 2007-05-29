# -*- coding: utf-8 -*-
#
# File: Tranched.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ProjectDatabase.content.CoreMixin import CoreMixin
from Products.ProjectDatabase.content.BlankCoreMixin import BlankCoreMixin
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

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Tranched_schema = BaseSchema.copy() + \
    getattr(CoreMixin, 'schema', Schema(())).copy() + \
    getattr(BlankCoreMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Tranched(BaseContent, CoreMixin, BlankCoreMixin):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),) + (getattr(CoreMixin,'__implements__',()),) + (getattr(BlankCoreMixin,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Tranched'

    meta_type = 'Tranched'
    portal_type = 'Tranched'
    allowed_content_types = [] + list(getattr(CoreMixin, 'allowed_content_types', [])) + list(getattr(BlankCoreMixin, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Tranched.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Tranched"
    typeDescMsgId = 'description_edit_tranched'

    _at_rename_after_creation = True

    schema = Tranched_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Tranched, PROJECTNAME)
# end of class Tranched

##code-section module-footer #fill in your manual code here
##/code-section module-footer



