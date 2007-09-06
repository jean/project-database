# -*- coding: utf-8 -*-
#
# File: EvaluatorsInformation.py
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

    DataGridField(
        name='TeamLeader',
        widget=DataGridField._properties['widget'](
            label="Team Lead",
            description="Name of Evaluation Team Leader",
            columns={'team_leader':Column('Team Leader')},
            label_msgid='ProjectDatabase_label_TeamLeader',
            description_msgid='ProjectDatabase_help_TeamLeader',
            i18n_domain='ProjectDatabase',
        ),
        columns=('team_leader',)
    ),

    DataGridField(
        name='TeamMembers',
        widget=DataGridField._properties['widget'](
            label="Team Members",
            description="Names of other evaluation Team Members",
            columns={'team_member':Column('Team Member')},
            label_msgid='ProjectDatabase_label_TeamMembers',
            description_msgid='ProjectDatabase_help_TeamMembers',
            i18n_domain='ProjectDatabase',
        ),
        columns=('team_member',)
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EvaluatorsInformation_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
title_field = EvaluatorsInformation_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
##/code-section after-schema

class EvaluatorsInformation(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Information on Evaluators'

    meta_type = 'EvaluatorsInformation'
    portal_type = 'EvaluatorsInformation'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'EvaluatorsInformation.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Information on Evaluators"
    typeDescMsgId = 'description_edit_evaluatorsinformation'

    _at_rename_after_creation = True

    schema = EvaluatorsInformation_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(EvaluatorsInformation, PROJECTNAME)
# end of class EvaluatorsInformation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



