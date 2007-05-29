# -*- coding: utf-8 -*-
#
# File: ProjectExecutingPartner.py
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

    StringField(
        name='Category',
        widget=SelectionWidget(
            label='Category',
            label_msgid='ProjectDatabase_label_Category',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Category""")
    ),

    TextField(
        name='OtherCategories',
        widget=TextAreaWidget(
            label="Other Categories",
            label_msgid='ProjectDatabase_label_OtherCategories',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProjectExecutingPartner_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ProjectExecutingPartner(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Project Executing Partner'

    meta_type = 'ProjectExecutingPartner'
    portal_type = 'ProjectExecutingPartner'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'ProjectExecutingPartner.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Project Executing Partner"
    typeDescMsgId = 'description_edit_projectexecutingpartner'

    _at_rename_after_creation = True

    schema = ProjectExecutingPartner_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(ProjectExecutingPartner, PROJECTNAME)
# end of class ProjectExecutingPartner

##code-section module-footer #fill in your manual code here
##/code-section module-footer



