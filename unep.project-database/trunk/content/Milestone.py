# -*- coding: utf-8 -*-
#
# File: Milestone.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.1
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
from Products.DataGridField import CalendarColumn
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn, CalendarColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label="Project Title",
            label_msgid='ProjectDatabase_label_ProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='ConceptDevelopment',
        widget=DataGridField._properties['widget'](
            label="Concept Development (IPI)",
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getConceptDevelopmentActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date'), 'milestone_result':SelectColumn('Milestone Result', vocabulary='getMilestoneResultVocabulary')},
            label_msgid='ProjectDatabase_label_ConceptDevelopment',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date', 'milestone_result'),
    ),
    DataGridField(
        name='PIFApproval',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getPIFApprovalActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date'), 'milestone_result':SelectColumn('Milestone Result', vocabulary='getMilestoneResultVocabulary')},
            label="PIF Approval",
            label_msgid='ProjectDatabase_label_PIFApproval',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date', 'milestone_result'),
    ),
    DataGridField(
        name='PPGApproval',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getPPGApprovalActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date'), 'milestone_result':SelectColumn('Milestone Result', vocabulary='getMilestoneResultVocabulary')},
            label="PPG Approval",
            label_msgid='ProjectDatabase_label_PPGApproval',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date', 'milestone_result'),
    ),
    DataGridField(
        name='PPGImplementation',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getPPGImplementationActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date')},
            label="PPG Implementation",
            label_msgid='ProjectDatabase_label_PPGImplementation',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date'),
    ),
    DataGridField(
        name='ProjectApproval',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getProjectApprovalActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date'), 'milestone_result':SelectColumn('Milestone Result', vocabulary='getMilestoneResultVocabulary')},
            label="Project Approval",
            label_msgid='ProjectDatabase_label_ProjectApproval',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date', 'milestone_result'),
    ),
    DataGridField(
        name='ProjectImplementation',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getProjectImplementationActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date')},
            label="Project Implementation",
            label_msgid='ProjectDatabase_label_ProjectImplementation',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date'),
    ),
    DataGridField(
        name='NewPhaseApproval',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getNewPhaseApprovalActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date'), 'comment':Column('Comment', vocabulary='getMilestoneResultVocabulary')},
            label="Add-on, Phase or Tranche Approval",
            label_msgid='ProjectDatabase_label_NewPhaseApproval',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date', 'comment'),
    ),
    DataGridField(
        name='NewPhaseImplementation',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getNewPhaseImplementationActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date')},
            label="Add-on, Phase or Tranche Implementation",
            label_msgid='ProjectDatabase_label_NewPhaseImplementation',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date'),
    ),
    DataGridField(
        name='EvaluationDates',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getEvaluationDatesActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date')},
            label="Evaluation Dates",
            label_msgid='ProjectDatabase_label_EvaluationDates',
            i18n_domain='ProjectDatabase',
        ),
        columns=('milestone_action', 'milestone_date'),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Milestone_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Milestone(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IMilestone)

    meta_type = 'Milestone'
    _at_rename_after_creation = True

    schema = Milestone_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Milestone, PROJECTNAME)
# end of class Milestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



