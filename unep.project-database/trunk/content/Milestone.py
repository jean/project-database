# -*- coding: utf-8 -*-
#
# File: Milestone.py
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
from zope import interface
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

    StringField(
        name='ProjectCycleStage',
        widget=SelectionWidget(
            label="Project Cycle Stage",
            label_msgid='ProjectDatabase_label_ProjectCycleStage',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectCycleStage"""),
    ),
    StringField(
        name='MilestoneName',
        widget=SelectionWidget(
            label="Milestone Name",
            label_msgid='ProjectDatabase_label_MilestoneName',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""MilestoneName"""),
    ),
    DateTimeField(
        name='MilestoneDate',
        widget=CalendarWidget(
            label="Milestone Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MilestoneDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='MilestoneDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Remarks on Decision",
            label_msgid='ProjectDatabase_label_MilestoneDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        vocabulary=NamedVocabulary("""ProjectStatusses"""),
    ),
    DataGridField(
        name='ProjectProcess',
        widget=DataGridField._properties['widget'](
            columns={'project_process':SelectColumn('Project Process',vocabulary='getProjectProcesses'),'project_status':SelectColumn('Status', vocabulary='getProjectStatusses')},
            label="Project Processes",
            description="Project Process and Review Dates",
            label_msgid='ProjectDatabase_label_ProjectProcess',
            description_msgid='ProjectDatabase_help_ProjectProcess',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectProcesses"""),
        columns=('project_process', 'project_status'),
    ),
    DataGridField(
        name='NationalFocalPointEndorsements',
        widget=DataGridField._properties['widget'](
            label="National Focal Point Endorsements",
            columns={'country':SelectColumn('Country', vocabulary='getCountryNames'),'endorsement_date':CalendarColumn('Endorsement Date')},
            label_msgid='ProjectDatabase_label_NationalFocalPointEndorsements',
            i18n_domain='ProjectDatabase',
        ),
        columns=('country', 'endorsement_date'),
    ),
    DataGridField(
        name='ApprovalInitiationAndClosure',
        widget=DataGridField._properties['widget'](
            label="Project Approval, Initiation and Closure",
            columns={'approval_initiation_closure':SelectColumn('Project Approval, Initiation and Closure', vocabulary='getApprovalInitiationClosure'), 'actual_date':CalendarColumn('Date')},
            label_msgid='ProjectDatabase_label_ApprovalInitiationAndClosure',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ApprovalInitiationClosure"""),
        columns=('approval_initiation_closure','actual_date'),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Milestone_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
title_field = Milestone_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
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

    security.declarePublic('getProjectProcesses')
    def getProjectProcesses(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('ProjectProcesses')
        return vocab.getDisplayList(self)

    security.declarePublic('getProjectStatusses')
    def getProjectStatusses(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('ProjectStatusses')
        return vocab.getDisplayList(self)

    security.declarePublic('getCountryNames')
    def getCountryNames(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('Country')
        return vocab.getDisplayList(self)

    security.declarePublic('getApprovalInitiationClosure')
    def getApprovalInitiationClosure(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('ApprovalInitiationClosure')
        return vocab.getDisplayList(self)

    # Manually created methods

    security.declarePublic('Title')
    def Title(self):
        """
        """
        return self.getMilestoneName()


registerType(Milestone, PROJECTNAME)
# end of class Milestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



