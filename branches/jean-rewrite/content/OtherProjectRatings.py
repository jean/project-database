# -*- coding: utf-8 -*-
#
# File: OtherProjectRatings.py
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
        name='OtherRating',
        widget=SelectionWidget(
            label="Other Rating",
            label_msgid='ProjectDatabase_label_OtherRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""OtherRatings""")
    ),

    StringField(
        name='ProjectObjectives',
        widget=SelectionWidget(
            label="Project Objectives",
            label_msgid='ProjectDatabase_label_ProjectObjectives',
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
        name='ProjectOutputsAndActivities',
        widget=SelectionWidget(
            label="Project Outputs and Actvities",
            label_msgid='ProjectDatabase_label_ProjectOutputsAndActivities',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='CostEffectiveness',
        widget=SelectionWidget(
            label="Cost Effectiveness",
            label_msgid='ProjectDatabase_label_CostEffectiveness',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='ProjectSustainability',
        widget=SelectionWidget(
            label="Project Sustainability",
            label_msgid='ProjectDatabase_label_ProjectSustainability',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='StakeholderParticipation',
        widget=SelectionWidget(
            label="Stakeholder Participation",
            label_msgid='ProjectDatabase_label_StakeholderParticipation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='CountryOwnership',
        widget=SelectionWidget(
            label="Country Ownership",
            label_msgid='ProjectDatabase_label_CountryOwnership',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='ImplementationApproach',
        widget=SelectionWidget(
            label="Implementation Approach",
            label_msgid='ProjectDatabase_label_ImplementationApproach',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='FinancialPlanning',
        widget=SelectionWidget(
            label="Financial Planning",
            label_msgid='ProjectDatabase_label_FinancialPlanning',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='Replicability',
        widget=SelectionWidget(
            label='Replicability',
            label_msgid='ProjectDatabase_label_Replicability',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='OverallRating',
        widget=SelectionWidget(
            label="Overall Rating",
            label_msgid='ProjectDatabase_label_OverallRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

OtherProjectRatings_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class OtherProjectRatings(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'OtherProjectRatings'

    meta_type = 'OtherProjectRatings'
    portal_type = 'OtherProjectRatings'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'OtherProjectRatings.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "OtherProjectRatings"
    typeDescMsgId = 'description_edit_otherprojectratings'

    _at_rename_after_creation = True

    schema = OtherProjectRatings_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(OtherProjectRatings, PROJECTNAME)
# end of class OtherProjectRatings

##code-section module-footer #fill in your manual code here
##/code-section module-footer



