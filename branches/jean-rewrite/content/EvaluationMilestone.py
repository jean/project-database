# -*- coding: utf-8 -*-
#
# File: EvaluationMilestone.py
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
        name='EvaluationTypeMilestone',
        widget=SelectionWidget(
            label="Evaluation Type Milestone",
            label_msgid='ProjectDatabase_label_EvaluationTypeMilestone',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""EvaluationTypeMilestone""")
    ),

    StringField(
        name='MEMilestoneName',
        widget=SelectionWidget(
            label="M&E Milestone Name",
            label_msgid='ProjectDatabase_label_MEMilestoneName',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""MEMilestoneName""")
    ),

    DateTimeField(
        name='PlannedDate',
        widget=CalendarWidget(
            label="Planned Date",
            description="Planned date for the particular milestone",
            label_msgid='ProjectDatabase_label_PlannedDate',
            description_msgid='ProjectDatabase_help_PlannedDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='ActualDate',
        widget=CalendarWidget(
            label="Actual Date",
            description="Actual date for the particular milestone",
            label_msgid='ProjectDatabase_label_ActualDate',
            description_msgid='ProjectDatabase_help_ActualDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    TextField(
        name='Remarks',
        widget=TextAreaWidget(
            description="To track changes related to evaluation planning",
            label='Remarks',
            label_msgid='ProjectDatabase_label_Remarks',
            description_msgid='ProjectDatabase_help_Remarks',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EvaluationMilestone_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
title_field = EvaluationMilestone_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
##/code-section after-schema

class EvaluationMilestone(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Evaluation Milestone'

    meta_type = 'EvaluationMilestone'
    portal_type = 'EvaluationMilestone'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'EvaluationMilestone.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Evaluation Milestone"
    typeDescMsgId = 'description_edit_evaluationmilestone'

    _at_rename_after_creation = True

    schema = EvaluationMilestone_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(EvaluationMilestone, PROJECTNAME)
# end of class EvaluationMilestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



