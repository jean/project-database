# -*- coding: utf-8 -*-
#
# File: OtherProjectRatings.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Jean Jordaan <jean.jordaan@gmail.com>, Jurgen Blignaut
<jurgen.blignaut@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

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
        vocabulary=NamedVocabulary("""OtherRatings"""),
    ),
    StringField(
        name='ProjectObjectives',
        widget=SelectionWidget(
            label="Project Objectives",
            label_msgid='ProjectDatabase_label_ProjectObjectives',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='ImplementationProgress',
        widget=SelectionWidget(
            label="Implementation Progress",
            label_msgid='ProjectDatabase_label_ImplementationProgress',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='MonitoringAndEvaluation',
        widget=SelectionWidget(
            label="Monitoring and Evaluation",
            label_msgid='ProjectDatabase_label_MonitoringAndEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='ProjectOutputsAndActivities',
        widget=SelectionWidget(
            label="Project Outputs and Actvities",
            label_msgid='ProjectDatabase_label_ProjectOutputsAndActivities',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='CostEffectiveness',
        widget=SelectionWidget(
            label="Cost Effectiveness",
            label_msgid='ProjectDatabase_label_CostEffectiveness',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='ProjectSustainability',
        widget=SelectionWidget(
            label="Project Sustainability",
            label_msgid='ProjectDatabase_label_ProjectSustainability',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='StakeholderParticipation',
        widget=SelectionWidget(
            label="Stakeholder Participation",
            label_msgid='ProjectDatabase_label_StakeholderParticipation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='CountryOwnership',
        widget=SelectionWidget(
            label="Country Ownership",
            label_msgid='ProjectDatabase_label_CountryOwnership',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='ImplementationApproach',
        widget=SelectionWidget(
            label="Implementation Approach",
            label_msgid='ProjectDatabase_label_ImplementationApproach',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='FinancialPlanning',
        widget=SelectionWidget(
            label="Financial Planning",
            label_msgid='ProjectDatabase_label_FinancialPlanning',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='Replicability',
        widget=SelectionWidget(
            label='Replicability',
            label_msgid='ProjectDatabase_label_Replicability',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='OverallRating',
        widget=SelectionWidget(
            label="Overall Rating",
            label_msgid='ProjectDatabase_label_OverallRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

OtherProjectRatings_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class OtherProjectRatings(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IOtherProjectRatings)

    meta_type = 'OtherProjectRatings'
    _at_rename_after_creation = True

    schema = OtherProjectRatings_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(OtherProjectRatings, PROJECTNAME)
# end of class OtherProjectRatings

##code-section module-footer #fill in your manual code here
##/code-section module-footer



