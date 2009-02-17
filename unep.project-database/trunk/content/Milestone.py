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
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
from Products.Archetypes.utils import DisplayList
from DateTime import DateTime
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
        write_permission="Registrar TM SPO",
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
        write_permission="Registrar",
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
        write_permission="Registrar",
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
        write_permission="Registrar TM FMO",
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
        write_permission="Registrar",
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
        write_permission="Registrar TM FMO",
        columns=('milestone_action', 'milestone_date'),
    ),
    DataGridField(
        name='NewPhaseApproval',
        widget=DataGridField._properties['widget'](
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getNewPhaseApprovalActionsVocabulary'), 'milestone_date':CalendarColumn('Milestone Date'), 'comment':Column('Comment')},
            label="Add-on, Phase or Tranche Approval",
            label_msgid='ProjectDatabase_label_NewPhaseApproval',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="Registrar",
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
        write_permission="Registrar FMO",
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
        write_permission="Registrar TM MO EO",
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

    # Manually created methods

    def getProjectTitle(self):
        return self.getAProject().project_general_info.Title()

    def getConceptDevelopmentActionsVocabulary(self):
        return self.getVocabulary('ConceptDevelopmentActions')

    def getPIFApprovalActionsVocabulary(self):
        return self.getVocabulary('PIFApprovalActions')

    def getPPGApprovalActionsVocabulary(self):
        return self.getVocabulary('PPGApprovalActions')

    def getPPGImplementationActionsVocabulary(self):
        return self.getVocabulary('PPGImplementationActions')

    def getProjectImplementationActionsVocabulary(self):
        return self.getVocabulary('ProjectImplementationActions')

    def getProjectApprovalActionsVocabulary(self):
        return self.getVocabulary('ProjectApprovalActions')

    def getNewPhaseApprovalActionsVocabulary(self):
        return self.getVocabulary('NewPhaseApprovalActions')

    def getNewPhaseImplementationActionsVocabulary(self):
        return self.getVocabulary('NewPhaseImplementationActions')

    def getEvaluationDatesActionsVocabulary(self):
        return self.getVocabulary('EvaluationDatesActions')

    def getMilestoneResultVocabulary(self):
        return self.getVocabulary('MilestoneResult')

    def getVocabulary(self, vocabularyName):
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName(vocabularyName)
        if vocab:
            return vocab.getDisplayList(self)
        return DisplayList()

    def isConceptClearedBySPO(self):
        return self.getConceptDevelopmentDate('SPOClearance') is not None \
            or self.getConceptDevelopmentDate('DirectorClearance') is not None \
            or self.getConceptDevelopmentDate('PAGClearance') is not None
    def getConceptDevelopmentDate(self, action):
        values = self.getConceptDevelopment()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def isPIFClearedByCEO(self):
        return self.getPIFApprovalDate('CEOPIFApprovalActual') is not None

    def getPIFApprovalDate(self, action):
        values = self.getPIFApproval()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def getProjectApprovalDate(self, action):
        values = self.getProjectApproval()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def getProjectImplementationDate(self, action):
        values = self.getProjectImplementation()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def getPPGApprovalDate(self, action):
        values = self.getPPGApproval()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def getPPGImplementationDate(self, action):
        values = self.getPPGImplementation()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def getNewPhaseImplementationDate(self, action):
        values = self.getNewPhaseImplementation()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def getEvaluationDatesDate(self, action):
        values = self.getEvaluationDates()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['milestone_date'] \
                   and v['milestone_action'] == action:
                    if date < v['milestone_date']:
                        date = v['milestone_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    security.declarePublic('getProjectStage')
    def getProjectStage(self):
        """ Return the stage in which the project is
        """
        stage = 'PIF Approval'
        if self.getPIFApprovalComplete():
            stage = 'PPG Approval'
        if self.getPPGApprovalComplete():
            stage = 'PPG Implementation'
        if self.getPPGImplementationComplete():
            stage = 'Project Approval'
        if self.getProjectApprovalComplete():
            stage = 'Project Implementation'
        if self.getProjectImplementationComplete():
            stage = 'Project Complete'
        return stage



registerType(Milestone, PROJECTNAME)
# end of class Milestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



