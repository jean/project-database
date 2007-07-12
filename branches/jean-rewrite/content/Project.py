# -*- coding: utf-8 -*-
#
# File: Project.py
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
import zope
from Products.ProjectDatabase.CurrencyMixin import CurrencyMixin
from Products.ProjectDatabase.content.DocumentLinks import DocumentLinks
from Products.ProjectDatabase.interfaces.IProject import IProject
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.ProjectDatabase.content import permissions
from Products.DataGridField import CalendarColumn
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
from Products.FinanceFields.Money import Money
##/code-section module-header

schema = Schema((

    TextField(
        name='SummaryDescription',
        widget=TextAreaWidget(
            label="Project Description",
            label_msgid='ProjectDatabase_label_SummaryDescription',
            i18n_domain='ProjectDatabase',
        ),
        searchable=1
    ),

    LinesField(
        name='FocalArea',
        index="FieldIndex:brains",
        widget=MultiSelectionWidget(
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""FocalArea""")
    ),

    StringField(
        name='OperationalProgramme',
        index="FieldIndex:brains",
        widget=SelectionWidget(
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""OperationalProgramme""")
    ),

    LinesField(
        name='EABiodiversity',
        widget=MultiSelectionWidget(
            label="EA-Biodiversity",
            label_msgid='ProjectDatabase_label_EABiodiversity',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EABiodiversity""")
    ),

    TextField(
        name='EABiodiversityOther',
        widget=TextAreaWidget(
            label="Other EA Biodiversity",
            label_msgid='ProjectDatabase_label_EABiodiversityOther',
            i18n_domain='ProjectDatabase',
        )
    ),

    LinesField(
        name='EAClimateChange',
        widget=MultiSelectionWidget(
            label="EA-Climate Change",
            label_msgid='ProjectDatabase_label_EAClimateChange',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAClimateChange""")
    ),

    TextField(
        name='EAClimateChangeOther',
        widget=TextAreaWidget(
            label="EA Climate Change Other",
            label_msgid='ProjectDatabase_label_EAClimateChangeOther',
            i18n_domain='ProjectDatabase',
        )
    ),

    LinesField(
        name='EAPOP',
        widget=MultiSelectionWidget(
            label="EA-POP",
            label_msgid='ProjectDatabase_label_EAPOP',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAPOP""")
    ),

    TextField(
        name='EAPOPOther',
        widget=TextAreaWidget(
            label="EA-POP Other",
            label_msgid='ProjectDatabase_label_EAPOPOther',
            i18n_domain='ProjectDatabase',
        )
    ),

    LinesField(
        name='MultipleFocalAreas',
        widget=MultiSelectionWidget(
            label="Multiple Focal Areas",
            label_msgid='ProjectDatabase_label_MultipleFocalAreas',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""MultipleFocalAreas""")
    ),

    TextField(
        name='MultipleFocalAreasOther',
        widget=TextAreaWidget(
            label="Multiple Focal Areas Other",
            label_msgid='ProjectDatabase_label_MultipleFocalAreasOther',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='StrategicPriority',
        index="FieldIndex:brains",
        widget=SelectionWidget(
            label="Strategic Priority",
            label_msgid='ProjectDatabase_label_StrategicPriority',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicPriority""")
    ),

    StringField(
        name='StrategicObjectives',
        widget=SelectionWidget(
            label="Strategic Objectives",
            label_msgid='ProjectDatabase_label_StrategicObjectives',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicObjectives""")
    ),

    StringField(
        name='ProjectType',
        index="FieldIndex:brains",
        widget=SelectionWidget(
            label="Project Type",
            label_msgid='ProjectDatabase_label_ProjectType',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectType""")
    ),

    StringField(
        name='PipelineNumber',
        widget=SelectionWidget(
            label="Pipeline Number",
            label_msgid='ProjectDatabase_label_PipelineNumber',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""PipelineNumber""")
    ),

    LinesField(
        name='Scope',
        index="FieldIndex:brains",
        widget=MultiSelectionWidget(
            label="Geographic Scope",
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Scope"""),
        schemata="Location"
    ),

    StringField(
        name='ScopeOther',
        widget=StringWidget(
            label="Geographic Scope - Other",
            label_msgid='ProjectDatabase_label_ScopeOther',
            i18n_domain='ProjectDatabase',
        ),
        schemata="Location"
    ),

    LinesField(
        name='Region',
        index="FieldIndex:brains",
        widget=MultiSelectionWidget(
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Region"""),
        schemata="Location"
    ),

    LinesField(
        name='Country',
        index="FieldIndex:brains",
        widget=MultiSelectionWidget(
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        schemata="Location",
        multiValued=1,
        vocabulary=NamedVocabulary("""Country""")
    ),

    LinesField(
        name='OtherNonGEFEligibleCountries',
        widget=MultiSelectionWidget(
            label="Other Non-GEF Eligible Project Participating Countries",
            label_msgid='ProjectDatabase_label_OtherNonGEFEligibleCountries',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Country""")
    ),

    StringField(
        name='LeadAgency',
        widget=SelectionWidget(
            label="Lead Agency",
            label_msgid='ProjectDatabase_label_LeadAgency',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""LeadAgency""")
    ),

    ReferenceField(
        name='LeadAgencyContact',
        index="FieldIndex:brains",
        widget=ReferenceField._properties['widget'](
            label="Lead GEF Agency",
            label_msgid='ProjectDatabase_label_LeadAgencyContact',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Agency',),
        multiValued=0,
        relationship="Project_LeadAgency"
    ),

    ReferenceField(
        name='OtherImplementingAgency',
        widget=ReferenceField._properties['widget'](
            label="Other GEF Implementing Agency",
            label_msgid='ProjectDatabase_label_OtherImplementingAgency',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Agency',),
        multiValued=0,
        relationship="Project_OtherImplementingAgency"
    ),

    DataGridField(
        name='ProjectExecutingAgency',
        widget=DataGridField._properties['widget'](
            label="Project Executing Agency",
            columns={'executing_agency':Column('Executing Agency'),'executing_agency_category':SelectColumn('Category', vocabulary='getCategoryVocab')},
            label_msgid='ProjectDatabase_label_ProjectExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Category"""),
        columns=('executing_agency','executing_agency_category')
    ),

    DataGridField(
        name='OtherProjectExecutingPartners',
        widget=DataGridField._properties['widget'](
            label="Other Project Executing Partners",
            columns={'partner_name':Column('Partner'),'category':SelectColumn('Category',vocabulary='getCategoryVocab')},
            label_msgid='ProjectDatabase_label_OtherProjectExecutingPartners',
            i18n_domain='ProjectDatabase',
        ),
        columns=('partner_name','category')
    ),

    TextField(
        name='UnepComponentDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="UNEP Component Description",
            description="Enter a description of UNEP components only in the case of jointly implemented projects",
            label_msgid='ProjectDatabase_label_UnepComponentDescription',
            description_msgid='ProjectDatabase_help_UnepComponentDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

    StringField(
        name='GEFPhase',
        index="FieldIndex:brains",
        widget=SelectionWidget(
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""GEFPhase""")
    ),

    StringField(
        name='ImplementationMode',
        widget=SelectionWidget(
            label="Mode of Execution",
            label_msgid='ProjectDatabase_label_ImplementationMode',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationMode""")
    ),

    ReferenceField(
        name='CurrentTaskManager',
        widget=ReferenceField._properties['widget'](
            label="Current Task Manager",
            label_msgid='ProjectDatabase_label_CurrentTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        schemata="Contacts",
        relationship="Project_CurrentTaskManager"
    ),

    ReferenceField(
        name='PreviousTaskManager',
        widget=ReferenceField._properties['widget'](
            label="Previous Task Manager",
            label_msgid='ProjectDatabase_label_PreviousTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        schemata="Contacts",
        multiValued=0,
        relationship="Project_PreviousTaskManager"
    ),

    StringField(
        name='Office',
        widget=StringWidget(
            label="Office of Execution",
            label_msgid='ProjectDatabase_label_Office',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='Website',
        widget=StringWidget(
            label='Website',
            label_msgid='ProjectDatabase_label_Website',
            i18n_domain='ProjectDatabase',
        ),
        validators=('isUrl',)
    ),

    ReferenceField(
        name='ProjectCoordinator',
        widget=ReferenceField._properties['widget'](
            label="Project Coordinator",
            label_msgid='ProjectDatabase_label_ProjectCoordinator',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        schemata="Contacts",
        multiValued=0,
        relationship="Project_ProjectCoordinator"
    ),

    DateTimeField(
        name='MidtermReviewReportDate',
        widget=CalendarWidget(
            label="Midterm Review Report Date",
            label_msgid='ProjectDatabase_label_MidtermReviewReportDate',
            i18n_domain='ProjectDatabase',
        ),
        schemata="MidtermReview"
    ),

    StringField(
        name='MidtermReviewEvaluatorName',
        widget=StringWidget(
            label="Midterm Review Evaluator Name",
            label_msgid='ProjectDatabase_label_MidtermReviewEvaluatorName',
            i18n_domain='ProjectDatabase',
        ),
        schemata="MidtermReview"
    ),

    DateTimeField(
        name='MidtermReviewPlannedDate',
        widget=CalendarWidget(
            label="Midterm Review Date (planned)",
            label_msgid='ProjectDatabase_label_MidtermReviewPlannedDate',
            i18n_domain='ProjectDatabase',
        ),
        schemata="MidtermReview"
    ),

    DateTimeField(
        name='MidtermReviewActualDate',
        widget=CalendarWidget(
            label="Midterm Review Date (actual)",
            label_msgid='ProjectDatabase_label_MidtermReviewActualDate',
            i18n_domain='ProjectDatabase',
        ),
        schemata="MidtermReview"
    ),

    DateTimeField(
        name='TerminalEvaluationReportDate',
        widget=CalendarWidget(
            label="Terminal Evaluation Report Date",
            label_msgid='ProjectDatabase_label_TerminalEvaluationReportDate',
            i18n_domain='ProjectDatabase',
        ),
        schemata="TerminalEvaluation"
    ),

    StringField(
        name='TerminalReportEvaluatorName',
        widget=StringWidget(
            label="Terminal Report Evaluator Name",
            label_msgid='ProjectDatabase_label_TerminalReportEvaluatorName',
            i18n_domain='ProjectDatabase',
        ),
        schemata="TerminalEvaluation"
    ),

    DateTimeField(
        name='TerminalReportPlannedEvaluationDate',
        widget=CalendarWidget(
            label="Terminal Report Evaluation Date (planned)",
            label_msgid='ProjectDatabase_label_TerminalReportPlannedEvaluationDate',
            i18n_domain='ProjectDatabase',
        ),
        schemata="TerminalEvaluation"
    ),

    DateTimeField(
        name='TerminalReportActualEvaluationDate',
        widget=CalendarWidget(
            label="Terminal Report Evaluation Date (actual)",
            label_msgid='ProjectDatabase_label_TerminalReportActualEvaluationDate',
            i18n_domain='ProjectDatabase',
        ),
        schemata="TerminalEvaluation"
    ),

    TextField(
        name='ProjectResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Actual Overall Project Results",
            description="Enter overall Project Results AFTER Project Terminal Evaluation",
            label_msgid='ProjectDatabase_label_ProjectResults',
            description_msgid='ProjectDatabase_help_ProjectResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

    MoneyField(
        name='LeveragedFinancingAmount',
        widget=MoneyField._properties['widget'](
            label="Leveraged Financing Amount",
            label_msgid='ProjectDatabase_label_LeveragedFinancingAmount',
            i18n_domain='ProjectDatabase',
        ),
        schemata="Financing"
    ),

    TextField(
        name='LeveragedFinancingRemark',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Leveraged Financial Amount Description",
            description="Enter sources and Purposes",
            label_msgid='ProjectDatabase_label_LeveragedFinancingRemark',
            description_msgid='ProjectDatabase_help_LeveragedFinancingRemark',
            i18n_domain='ProjectDatabase',
        ),
        schemata="Financing",
        vocabulary=NamedVocabulary("""LeadAgency"""),
        default_output_type='text/html'
    ),

    ComputedField(
        name='TotalGEFAllocation',
        widget=ComputedField._properties['widget'](
            label="Total GEF Allocation",
            label_msgid='ProjectDatabase_label_TotalGEFAllocation',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalUNEPAllocation',
        widget=ComputedField._properties['widget'](
            label="Total UNEP Allocation",
            label_msgid='ProjectDatabase_label_TotalUNEPAllocation',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalCofinancingPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing (planned)",
            label_msgid='ProjectDatabase_label_TotalCofinancingPlanned',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalCofinancingActual',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing (actual)",
            label_msgid='ProjectDatabase_label_TotalCofinancingActual',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalCashDisbursements',
        widget=ComputedField._properties['widget'](
            label="Total Cash Disbursements",
            label_msgid='ProjectDatabase_label_TotalCashDisbursements',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='TotalIMISExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total IMIS Expenditures",
            label_msgid='ProjectDatabase_label_TotalIMISExpenditures',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='PDFAStatus',
        widget=ComputedField._properties['widget'](
            label="PDFA Status",
            label_msgid='ProjectDatabase_label_PDFAStatus',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='PDFBStatus',
        widget=ComputedField._properties['widget'](
            label="PDFB Status",
            label_msgid='ProjectDatabase_label_PDFBStatus',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='MSPStatus',
        widget=ComputedField._properties['widget'](
            label="MSP Status",
            label_msgid='ProjectDatabase_label_MSPStatus',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='FSPStatus',
        widget=ComputedField._properties['widget'](
            label="FSP Status",
            label_msgid='ProjectDatabase_label_FSPStatus',
            i18n_domain='ProjectDatabase',
        )
    ),

    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label="Project Title",
            label_msgid='ProjectDatabase_label_ProjectTitle',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='GEFAgencyImplementation',
        widget=SelectionWidget(
            label="GEF Agency Implementation",
            label_msgid='ProjectDatabase_label_GEFAgencyImplementation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""AgencyImplementation""")
    ),

    StringField(
        name='Tranched',
        widget=SelectionWidget(
            description="Is this a Tranched project?",
            label='Tranched',
            label_msgid='ProjectDatabase_label_Tranched',
            description_msgid='ProjectDatabase_help_Tranched',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""YesOrNo""")
    ),

    IntegerField(
        name='TranchedNumber',
        default=0,
        widget=IntegerField._properties['widget'](
            label="",
            label_msgid='ProjectDatabase_label_TranchedNumber',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='Phased',
        widget=SelectionWidget(
            description="Is this a Phased project?",
            label='Phased',
            label_msgid='ProjectDatabase_label_Phased',
            description_msgid='ProjectDatabase_help_Phased',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""YesOrNo""")
    ),

    IntegerField(
        name='PhasedNumber',
        default=0,
        widget=IntegerField._properties['widget'](
            label="Phased Number",
            label_msgid='ProjectDatabase_label_PhasedNumber',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='AddOn',
        widget=SelectionWidget(
            label='Addon',
            label_msgid='ProjectDatabase_label_AddOn',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""YesOrNo""")
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Project_schema = BaseFolderSchema.copy() + \
    getattr(DocumentLinks, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
idField = Project_schema['id']
idField.widget.visible = {'edit': 'hidden', 'view': 'visible'}
idField.widget.label = 'Internal Id'
##/code-section after-schema

class Project(BaseFolder, CurrencyMixin, DocumentLinks):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),) + (getattr(CurrencyMixin,'__implements__',()),) + (getattr(DocumentLinks,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IProject)

    # This name appears in the 'add' box
    archetype_name = 'Project General Information'

    meta_type = 'Project'
    portal_type = 'Project'
    allowed_content_types = ['ProjectImplementation', 'Financials', 'Milestone', 'ProjectExecutingPartner', 'MonitoringAndEvaluation', 'SubProjectFolder', 'AddOnFolder', 'PhasedFolder', 'TranchedFolder'] + list(getattr(DocumentLinks, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'Project.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Project General Information"
    typeDescMsgId = 'description_edit_project'


    actions =  (


       {'action': "string:${object_url}/Overview",
        'category': "object_tabs",
        'id': 'overview',
        'name': 'Overview',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/project_general_information",
        'category': "object_tabs",
        'id': 'pgi',
        'name': 'Project General Information',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:0'
       },


       {'action': "string:${object_url}/fmi_view",
        'category': "object_tabs",
        'id': 'fmi_view',
        'name': 'FMI View',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:0'
       },


    )

    _at_rename_after_creation = True

    schema = Project_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getTotalGEFAllocation')
    def getTotalGEFAllocation(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getGEFProjectAllocation():
                total += fmi_obj.getGEFProjectAllocation()
        for sp_obj in subproject_objs:
            if sp_obj.getGEFProjectAllocation():
                total += sp_obj.getGEFProjectAllocation()
        return total

    security.declarePublic('getTotalUNEPAllocation')
    def getTotalUNEPAllocation(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getCashUNEPAllocation():
                total += fmi_obj.getCashUNEPAllocation()
        return total

    security.declarePublic('getTotalCofinancingPlanned')
    def getTotalCofinancingPlanned(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCofinCashPlanned():
                total += fmi_obj.getSumCofinCashPlanned()
            if fmi_obj.getSumCofinInKindPlanned():
                total += fmi_obj.getSumCofinInKindPlanned()
        for sp_obj in subproject_objs:
            if sp_obj.getSumCofinCashPlanned():
                total += sp_obj.getSumCofinCashPlanned()
            if sp_obj.getSumCofinInKindPlanned():
                total += sp_obj.getSumCofinInKindPlanned()
        return total

    security.declarePublic('getTotalCofinancingActual')
    def getTotalCofinancingActual(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCofinCashActual():
                total += fmi_obj.getSumCofinCashActual()
            if fmi_obj.getSumCofinInKindActual():
                total += fmi_obj.getSumCofinInKindActual()
        for sp_obj in subproject_objs:
            if sp_obj.getSumCofinCashActual():
                total += sp_obj.getSumCofinCashActual()
            if sp_obj.getSumCofinInKindActual():
                total += sp_obj.getSumCofinInKindActual()
        return total

    security.declarePublic('getTotalCashDisbursements')
    def getTotalCashDisbursements(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCashDisbursements():
                total += fmi_obj.getSumCashDisbursements()
        for sp_obj in subproject_objs:
            if sp_obj.getSumCashDisbursements():
                total += sp_obj.getSumCashDisbursements()
        return total

    security.declarePublic('getTotalIMISExpenditures')
    def getTotalIMISExpenditures(self):
        """
        """
        fmi_cash_objs = self.contentValues('Financials')
        subproject_objs = self.contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumIMISExpenditures():
                total += fmi_obj.getSumIMISExpenditures()
        for sp_obj in subproject_objs:
            if sp_obj.getSumIMISExpenditures():
                total += sp_obj.getSumIMISExpenditures()
        return total

    security.declarePublic('getPDFAStatus')
    def getPDFAStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF A':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getPDFBStatus')
    def getPDFBStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF B':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getMSPStatus')
    def getMSPStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'MSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getFSPStatus')
    def getFSPStatus(self):
        """
        """
        fmi_objs = self.contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'FSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """ Code copied from previous project; dunno what it means...
        """
        start_date_val = ''
        start_date_val_comp = ''
        r_str = ''

        for fobj in self.contentValues('Financials'):
            start_date_val = fobj.getStartDate()
            if start_date_val_comp == '':
                start_date_val_comp = fobj.getStartDate()
                r_str = fobj.Title()
            else:
                if start_date_val > start_date_val_comp:
                    start_date_val_comp = start_date_val
                    r_str = fobj.Title()
        return r_str

    security.declarePublic('validate_TranchedNumber')
    def validate_TranchedNumber(self, value):
        """
        """
        val=0
        try:
            val = int(value)
        except ValueError:
            return 'Value must be an integer'

        if self.REQUEST.get('Tranched') == 'Yes':
            if val <= 0:
                return 'Value must be bigger than zero if Tranched is Yes'
        if self.REQUEST.get('Tranched') == 'No':
            if val != 0:
                return 'Value must be zero if Tranched is No'
        return

    security.declarePublic('validate_PhasedNumber')
    def validate_PhasedNumber(self, value):
        """
        """
        val=0
        try:
            val = int(value)
        except ValueError:
            return 'Value must be an integer'

        if self.REQUEST.get('Phased') == 'Yes':
            if val <= 0:
                return 'Value must be bigger than zero if Phased is Yes'
        if self.REQUEST.get('Phased') == 'No':
            if val != 0:
                return 'Value must be zero if Phased is No'
        return

    security.declarePublic('getProject')
    def getProject(self):
        return self.aq_inner

    security.declarePublic('getCategoryVocab')
    def getCategoryVocab(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('Category')
        return vocab.getDisplayList(self)

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container):
        """
        """
        if 'financials' not in self.objectIds():
            self.invokeFactory('Financials', 'financials')
            self['financials'].setTitle('Financial Management Information')
        if 'tranchedfolder' not in self.objectIds():
            self.invokeFactory('TranchedFolder', 'tranchedfolder')
            self['tranchedfolder'].setTitle('Tranched Projects')
        if 'phasedfolder' not in self.objectIds():
            self.invokeFactory('PhasedFolder', 'phasedfolder')
            self['phasedfolder'].setTitle('Phased Projects')
        if 'addonfolder' not in self.objectIds():
            self.invokeFactory('AddOnFolder', 'addonfolder')
            self['addonfolder'].setTitle('Add On Projects')
        if 'subprojectfolder' not in self.objectIds():
            self.invokeFactory('SubProjectFolder', 'subprojectfolder')
            self['subprojectfolder'].setTitle('Sub-Projects')
        BaseFolder.manage_afterAdd(self, item, container)

    security.declarePublic('displayContentsTab')
    def displayContentsTab(self):
        """ Don't display the contents tab
        """
        return False


registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
def modify_fti(fti):
    for a in fti['actions']:
        if a['id'] in ('metadata', 'references'):
            a['visible'] = 0
    return fti

##/code-section module-footer



