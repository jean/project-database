# -*- coding: utf-8 -*-
#
# File: OtherProjectRatingsFolder.py
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

OtherProjectRatingsFolder_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class OtherProjectRatingsFolder(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'OtherProjectRatingsFolder'

    meta_type = 'OtherProjectRatingsFolder'
    portal_type = 'OtherProjectRatingsFolder'
    allowed_content_types = ['OtherProjectRatings']
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'OtherProjectRatingsFolder.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "OtherProjectRatingsFolder"
    typeDescMsgId = 'description_edit_otherprojectratingsfolder'

    _at_rename_after_creation = True

    schema = OtherProjectRatingsFolder_schema

    ##code-section class-header #fill in your manual code here
    actions = ({  'action':"string:${object_url}/edit",
                            'category':"object",
                            'id':'edit',
                            'name':'edit',
                            'permissions':('Modify portal content'),
                            'condition':'python:0',
                        },)
    ##/code-section class-header

    # Methods


registerType(OtherProjectRatingsFolder, PROJECTNAME)
# end of class OtherProjectRatingsFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer


