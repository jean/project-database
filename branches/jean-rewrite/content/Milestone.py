# -*- coding: utf-8 -*-
#
# File: Milestone.py
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
from Products.ProjectDatabase.interfaces.IMilestone import IMilestone
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
        name='ImplementationStatus',
        widget=SelectionWidget(
            label="Implementation Status",
            label_msgid='ProjectDatabase_label_ImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationStatus""")
    ),

    StringField(
        name='MilestoneName',
        widget=SelectionWidget(
            label="Milestone Name",
            label_msgid='ProjectDatabase_label_MilestoneName',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""MilestoneName""")
    ),

    DateTimeField(
        name='MilestoneDate',
        widget=CalendarWidget(
            label="Milestone Date",
            label_msgid='ProjectDatabase_label_MilestoneDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    TextField(
        name='MilestoneDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Milestone Description",
            label_msgid='ProjectDatabase_label_MilestoneDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Milestone_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Milestone(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IMilestone)

    # This name appears in the 'add' box
    archetype_name = 'Milestone'

    meta_type = 'Milestone'
    portal_type = 'Milestone'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Milestone.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Milestone"
    typeDescMsgId = 'description_edit_milestone'

    _at_rename_after_creation = True

    schema = Milestone_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Milestone, PROJECTNAME)
# end of class Milestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



