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

    ReferenceField(
        name='TeamLeader',
        widget=ReferenceField._properties['widget'](
            label="Team Leader",
            description="Name of evaluation team leader",
            label_msgid='ProjectDatabase_label_TeamLeader',
            description_msgid='ProjectDatabase_help_TeamLeader',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        multiValued=0,
        relationship="Evaluators_TeamLeader"
    ),

    ReferenceField(
        name='TeamMembers',
        widget=ReferenceField._properties['widget'](
            label="Team Members",
            description="Names of other evaluation team members",
            label_msgid='ProjectDatabase_label_TeamMembers',
            description_msgid='ProjectDatabase_help_TeamMembers',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        multiValued=1,
        relationship="Evaluators_TeamMembers"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EvaluatorsInformation_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
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



