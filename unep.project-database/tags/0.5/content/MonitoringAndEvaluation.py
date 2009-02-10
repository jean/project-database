# -*- coding: utf-8 -*-
#
# File: MonitoringAndEvaluation.py
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
import permissions
from Products.Archetypes.utils import DisplayList
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
    StringField(
        name='EvaluationType',
        widget=SelectionWidget(
            label="Evaluation Type",
            label_msgid='ProjectDatabase_label_EvaluationType',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""EvaluationType"""),
    ),
    BooleanField(
        name='JointEvaluation',
        widget=BooleanField._properties['widget'](
            label="Joint Evaluation",
            label_msgid='ProjectDatabase_label_JointEvaluation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='OtherAgency',
        widget=StringField._properties['widget'](
            label="Other Agency",
            label_msgid='ProjectDatabase_label_OtherAgency',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ReferenceField(
        name='OtherAgencyEvaluationContact',
        widget=ReferenceBrowserWidget(
            label="Other Agency Evaluation Contact",
            label_msgid='ProjectDatabase_label_OtherAgencyEvaluationContact',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        multiValued=0,
        relationship="monitoring_contact",
    ),
    DateTimeField(
        name='PlannedStartDate',
        widget=DateTimeField._properties['widget'](
            label="Planned Start Date",
            label_msgid='ProjectDatabase_label_PlannedStartDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='EvaluationProcessStatus',
        widget=DataGridField._properties['widget'](
            label="Evaluation Process Status",
            columns={'process_step':SelectColumn('Process Step', vocabulary='getEvaluationProcessStepVocabulary'), 'step_date':CalendarColumn('Step Date')},
            label_msgid='ProjectDatabase_label_EvaluationProcessStatus',
            i18n_domain='ProjectDatabase',
        ),
        columns=('process_step', 'step_date'),
    ),
    DataGridField(
        name='EvaluationRatings',
        widget=DataGridField._properties['widget'](
            label="Evaluation Ratings",
            columns={'criterion':SelectColumn('Criterion', vocabulary='getEvaluationCriteria'), 'evaluator_rating':SelectColumn('Evaluator Rating', vocabulary='getRatingVocabulary'), 'EOU_rating':SelectColumn('EOU Rating', vocabulary='getRatingVocabulary'), 'GEF_EO_Rating':SelectColumn('GEF EO Rating', vocabulary='getRatingVocabulary')},
            label_msgid='ProjectDatabase_label_EvaluationRatings',
            i18n_domain='ProjectDatabase',
        ),
        columns=('criterion', 'evaluator_rating', 'EOU_rating', 'GEF_EO_Rating'),
    ),
    DataGridField(
        name='TerminalEvaluationReportQuality',
        widget=DataGridField._properties['widget'](
            label="Terminal Evaluation Report Quality",
            columns={'EOU_rating':SelectColumn('EOU Rating', vocabulary='getRatingVocabulary'), 'GEF_EO_rating':SelectColumn('GEF EO Rating', vocabulary='getRatingVocabulary')},
            label_msgid='ProjectDatabase_label_TerminalEvaluationReportQuality',
            i18n_domain='ProjectDatabase',
        ),
        columns=('EOU_rating', 'GEF_EO_rating'),
    ),
    DataGridField(
        name='EvaluationTeam',
        widget=DataGridField._properties['widget'](
            label="Evaluation Team",
            columns={'name':Column('Evaluator Name'), 'role':SelectColumn('Role', vocabulary='getEvaluatorRoleVocabulary')},
            label_msgid='ProjectDatabase_label_EvaluationTeam',
            i18n_domain='ProjectDatabase',
        ),
        columns=('name', 'role'),
    ),
    DataGridField(
        name='PIRRatings',
        widget=DataGridField._properties['widget'](
            label="PIR Ratings",
            columns={'year':Column('Fiscal Year'), 'dev_obj':SelectColumn('Development Objective', vocabulary='getRatingVocabulary'), 'imp_obj':SelectColumn('Implementation Progress', vocabulary='getRatingVocabulary'), 'm_and_e':SelectColumn('Monitoring and Evaluation', vocabulary='getRatingVocabulary'), 'risk':SelectColumn('Project Risk', vocabulary='getRiskLevelVocabulary')},
            label_msgid='ProjectDatabase_label_PIRRatings',
            i18n_domain='ProjectDatabase',
        ),
        columns=('year', 'dev_obj', 'imp_obj', 'm_and_e', 'risk'),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MonitoringAndEvaluation_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MonitoringAndEvaluation(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IMonitoringAndEvaluation)

    meta_type = 'MonitoringAndEvaluation'
    _at_rename_after_creation = True

    schema = MonitoringAndEvaluation_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """
        """
        return self.getAProject().project_general_info.Title()

    # Manually created methods

    def getEvaluationProcessStepVocabulary(self):
        return self.getVocabulary('MEProcessStep')

    def getEvaluationCriteria(self):
        return self.getVocabulary('EvaluationCriteria')

    def getRatingVocabulary(self):
        return self.getVocabulary('Rating')

    def getEvaluatorRoleVocabulary(self):
        return self.getVocabulary('EvaluatorRole')

    def getRiskLevelVocabulary(self):
        return self.getVocabulary('RiskLevel')

    def getVocabulary(self, vocabName):
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName(vocabName)
        if vocab:
            return vocab.getDisplayList(self)
        return DisplayList()

    def getEvaluationProcessStatusDates(self, step):
        values = self.getEvaluationProcessStatus()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['step_date'] \
                   and v['process_step'] == step:
                    if date < v['step_date']:
                        date = v['step_date']
            if date != DateTime('1900/01/01'):
                return date
        return None

    def getEvaluationRatingsDates(self, step):
        values = self.getEvaluationRatings()
        if values:
            date = DateTime('1900/01/01')
            for v in values:
                if v['step_date'] \
                   and v['process_step'] == step:
                    if date < v['step_date']:
                        date = v['step_date']
            if date != DateTime('1900/01/01'):
                return date
        return None


registerType(MonitoringAndEvaluation, PROJECTNAME)
# end of class MonitoringAndEvaluation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



