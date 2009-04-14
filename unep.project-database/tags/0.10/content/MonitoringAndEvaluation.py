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

__author__ = """Mike Metcalfe <mikejmets@gmail.com>, Jurgen Blignaut
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
from DateTime import DateTime
from Products.ProjectDatabase.utils import getVocabularyValue
from Products.DataGridField import ReferenceColumn
##/code-section module-header

schema = Schema((

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
    ReferenceField(
        name='OtherAgency',
        widget=ReferenceBrowserWidget(
            label="Other Agency",
            label_msgid='ProjectDatabase_label_OtherAgency',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types= ('Organisation',),
        relationship="OtherAgency_Organisation",
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
    StringField(
        name='EOUTerminalEvaluationReportQuality',
        widget=SelectionWidget(
            label="Terminal Evaluation Report Quality: EOU Rating",
            label_msgid='ProjectDatabase_label_EOUTerminalEvaluationReportQuality',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='GEFTerminalEvaluationReportQuality',
        widget=SelectionWidget(
            label="Terminal Evaluation Report Quality: GEF EO Rating",
            label_msgid='ProjectDatabase_label_GEFTerminalEvaluationReportQuality',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    DataGridField(
        name='EvaluationTeam',
        widget=DataGridField._properties['widget'](
            label="Evaluation Team",
            columns={'name':ReferenceColumn('Evaluator Name', fieldname='EvaluationTeamEvaluatorName'), 'role':SelectColumn('Role', vocabulary='getEvaluatorRoleVocabulary')},
            label_msgid='ProjectDatabase_label_EvaluationTeam',
            i18n_domain='ProjectDatabase',
        ),
        columns=('name', 'role'),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MonitoringAndEvaluation_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
MonitoringAndEvaluation_schema['OtherAgencyEvaluationContact'].widget.startup_directory_method = \
            'getContactsPath'
MonitoringAndEvaluation_schema['PlannedStartDate'].widget.show_hm = False
MonitoringAndEvaluation_schema['EvaluationType'].widget.visible = \
            {'edit':'hidden', 'view':'visible'}
MonitoringAndEvaluation_schema['title'].widget.visible = \
            {'edit':'hidden', 'view':'visible'}

MonitoringAndEvaluation_schema = MonitoringAndEvaluation_schema.copy()  + Schema((

    ReferenceField("EvaluationTeamEvaluatorName",
            widget = ReferenceBrowserWidget(
                label="Name",
                visible=False,
                startup_directory='/contacts',
            ),
            allowed_types=('Person',),
            relationship='mne_evaluator',
            multiValued=1,
        ),

    ))
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

    def getLatestEvaluationProcessStatus(self):
        values = self.getEvaluationProcessStatus()
        if values:
            step = ''
            date = DateTime('1900/01/01')
            for v in values:
                if v['step_date'] and v['process_step']:
                    if date < v['step_date']:
                        date = v['step_date']
                        step = v['process_step']
            if date != DateTime('1900/01/01'):
                return getVocabularyValue(self, 'MEProcessStep', step)
        return None

    security.declarePublic('getEvaluationCriterionRatings')
    def getEvaluationCriterionRatings(self, criterion):
        values = self.getEvaluationRatings()
        for v in values:
            if v['criterion'] == criterion:
                return (getVocabularyValue(self, 'Rating', v['evaluator_rating']),
                        getVocabularyValue(self, 'Rating', v['EOU_rating']),
                        getVocabularyValue(self, 'Rating', v['GEF_EO_Rating']))
        return (None, None, None)

    security.declarePublic('getContactsPath')
    def getContactsPath(self):
        purl = getToolByName(self, 'portal_url').getPortalObject().absolute_url()
        pc = getToolByName(self, 'portal_catalog')
        brains = pc({'portal_type':'ContactManager'})
        if len(brains) > 0:
            contacts = brains[0].getObject()
            curl = contacts.absolute_url()
            return curl[len(purl)+1:]
        return ''

    security.declarePublic('getLeadEvaluatorPerson')
    def getLeadEvaluatorPerson(self):
        values = self.getEvaluationTeam()
        if values:
            refcat = getToolByName(self, 'reference_catalog')
            for v in values:
                if v['name'] and v['role'] and v['role'] == 'Lead':
                    lead = refcat.lookupObject(v['name'])
                    if lead is not None:
                        return lead
        return None

    security.declarePublic('getLeadEvaluatorPerson')
    def getLeadEvaluator(self):
        person = self.getLeadEvaluatorPerson()
        if person:
            return person.getFullname()
        return ''

    security.declarePublic('getLeadEvaluatorDetails')
    def getLeadEvaluatorDetails(self):
        person = self.getLeadEvaluatorPerson()
        if person:
            address = person.getPhysicalAddress()
            nationality = 'Unknown'
            if address:
                nationality = address.get('country', '')
            return person.getFullname(), \
                    nationality, \
                    'Unknown', \
                    person.getEmail(), \
                    person.getMobilePhone(), \
                    person.getBusinessPhone()
        return None, None, None, None, None, None

    security.declarePublic('getOtherEvaluators')
    def getOtherEvaluators(self):
        values = self.getEvaluationTeam()
        names = ""
        if values:
            for v in values:
                if v['name'] and v['role'] and v['role'] == 'Member':
                    names += v['name'] + ', '
            return names[:-2]
        return None


    def getHideFieldNames(self):
        fieldnames = []
        if self.getJointEvaluation() == False:
            fieldnames.append('OtherAgency')
            fieldnames.append('OtherAgencyEvaluationContact')

        return fieldnames

    def getToggleFieldNames(self, fieldname, value=None, **kwargs):
        hide = []
        show = []
        if fieldname == 'JointEvaluation':
            if value == 'on':
                hide.append('OtherAgency')
                hide.append('OtherAgencyEvaluationContact')
            else:
                show.append('OtherAgency')
                show.append('OtherAgencyEvaluationContact')
        return show, hide

registerType(MonitoringAndEvaluation, PROJECTNAME)
# end of class MonitoringAndEvaluation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



