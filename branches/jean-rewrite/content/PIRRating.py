# -*- coding: utf-8 -*-
#
# File: PIRRating.py
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
        name='FiscalYear',
        widget=StringWidget(
            label="Fiscal Year",
            label_msgid='ProjectDatabase_label_FiscalYear',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='AchievementOfResults',
        widget=SelectionWidget(
            label="Achievement of Results",
            label_msgid='ProjectDatabase_label_AchievementOfResults',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='ImplementationProgress',
        widget=SelectionWidget(
            label="Implementation Progress",
            label_msgid='ProjectDatabase_label_ImplementationProgress',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='MonitoringAndEvaluation',
        widget=SelectionWidget(
            label="Monitoring and Evaluation",
            label_msgid='ProjectDatabase_label_MonitoringAndEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='Risk',
        widget=SelectionWidget(
            label='Risk',
            label_msgid='ProjectDatabase_label_Risk',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""InceptionRiskRating""")
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PIRRating_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PIRRating(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'PIRRating'

    meta_type = 'PIRRating'
    portal_type = 'PIRRating'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'PIRRating.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "PIRRating"
    typeDescMsgId = 'description_edit_pirrating'

    _at_rename_after_creation = True

    schema = PIRRating_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(PIRRating, PROJECTNAME)
# end of class PIRRating

##code-section module-footer #fill in your manual code here
##/code-section module-footer



