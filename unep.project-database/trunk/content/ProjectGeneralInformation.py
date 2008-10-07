# -*- coding: utf-8 -*-
#
# File: ProjectGeneralInformation.py
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
from Products.ProjectDatabase.content.CurrencyMixin import CurrencyMixin
from Products.ProjectDatabase.interfaces.IProject import IProject
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
from Products.ProjectDatabase.content.SubProjectFolder import SubProjectFolder
##/code-section module-header

schema = Schema((

    TextField(
        name='SummaryDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Project Description",
            label_msgid='ProjectDatabase_label_SummaryDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    LinesField(
        name='FocalArea',
        widget=MultiSelectionWidget(
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""FocalArea"""),
    ),
    StringField(
        name='OperationalProgramme',
        widget=SelectionWidget(
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""OperationalProgramme"""),
    ),
    LinesField(
        name='EABiodiversity',
        widget=MultiSelectionWidget(
            label="EA-Biodiversity",
            label_msgid='ProjectDatabase_label_EABiodiversity',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EABiodiversity"""),
    ),
    StringField(
        name='EABiodiversityOther',
        widget=StringField._properties['widget'](
            label="Other EA Biodiversity",
            label_msgid='ProjectDatabase_label_EABiodiversityOther',
            i18n_domain='ProjectDatabase',
        ),
    ),
    LinesField(
        name='EAClimateChange',
        widget=MultiSelectionWidget(
            label="EA-Climate Change",
            label_msgid='ProjectDatabase_label_EAClimateChange',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAClimateChange"""),
    ),
    StringField(
        name='EAClimateChangeOther',
        widget=StringField._properties['widget'](
            label="EA Climate Change Other",
            label_msgid='ProjectDatabase_label_EAClimateChangeOther',
            i18n_domain='ProjectDatabase',
        ),
    ),
    LinesField(
        name='EAPOP',
        widget=MultiSelectionWidget(
            label="EA-POP",
            label_msgid='ProjectDatabase_label_EAPOP',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAPOP"""),
    ),
    StringField(
        name='EAPOPOther',
        widget=StringField._properties['widget'](
            label="EA-POP Other",
            label_msgid='ProjectDatabase_label_EAPOPOther',
            i18n_domain='ProjectDatabase',
        ),
    ),
    LinesField(
        name='MultipleFocalAreas',
        widget=MultiSelectionWidget(
            label="Multiple Focal Areas",
            label_msgid='ProjectDatabase_label_MultipleFocalAreas',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""MultipleFocalAreas"""),
    ),
    StringField(
        name='MultipleFocalAreasOther',
        widget=StringField._properties['widget'](
            label="Multiple Focal Areas Other",
            label_msgid='ProjectDatabase_label_MultipleFocalAreasOther',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='StrategicPriority',
        widget=SelectionWidget(
            label="Strategic Priority",
            label_msgid='ProjectDatabase_label_StrategicPriority',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicPriority"""),
    ),
    StringField(
        name='StrategicObjectives',
        widget=SelectionWidget(
            label="Strategic Objectives",
            label_msgid='ProjectDatabase_label_StrategicObjectives',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicObjectives"""),
    ),
    StringField(
        name='StrategicProgram',
        widget=SelectionWidget(
            label="Strategic Program",
            label_msgid='ProjectDatabase_label_StrategicProgram',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicProgram"""),
    ),
    StringField(
        name='ProjectType',
        widget=SelectionWidget(
            label="Project Type",
            label_msgid='ProjectDatabase_label_ProjectType',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectType"""),
    ),
    StringField(
        name='PipelineNumber',
        widget=SelectionWidget(
            label="Pipeline Number",
            label_msgid='ProjectDatabase_label_PipelineNumber',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""PipelineNumber"""),
    ),
    LinesField(
        name='Scope',
        widget=MultiSelectionWidget(
            label="Geographic Scope",
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Scope"""),
    ),
    StringField(
        name='ScopeOther',
        widget=StringField._properties['widget'](
            label="Geographic Scope - Other",
            label_msgid='ProjectDatabase_label_ScopeOther',
            i18n_domain='ProjectDatabase',
        ),
    ),
    LinesField(
        name='Region',
        widget=MultiSelectionWidget(
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Region"""),
    ),
    LinesField(
        name='Country',
        widget=MultiSelectionWidget(
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Country"""),
    ),
    LinesField(
        name='OtherNonGEFEligibleCountries',
        widget=MultiSelectionWidget(
            label="Other Non-GEF Eligible Project Participating Countries",
            label_msgid='ProjectDatabase_label_OtherNonGEFEligibleCountries',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Country"""),
    ),
    StringField(
        name='LeadAgency',
        widget=SelectionWidget(
            label="Lead GEF Agency",
            label_msgid='ProjectDatabase_label_LeadAgency',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""LeadAgency"""),
    ),
    ReferenceField(
        name='LeadAgencyContact',
        widget=ReferenceBrowserWidget(
            label="Lead GEF Agency Contact",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_LeadAgencyContact',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary='contactsVocab',
        relationship="Project_LeadAgency",
        multiValued=0,
        allowed_types=('Person',),
    ),
    StringField(
        name='OtherImplementingAgency',
        widget=SelectionWidget(
            label="Other GEF Agency(ies)",
            label_msgid='ProjectDatabase_label_OtherImplementingAgency',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""LeadAgency"""),
    ),
    DataGridField(
        name='ProjectExecutingAgency',
        widget=DataGridField._properties['widget'](
            label="Lead Executing Agency",
            columns={'executing_agency':Column('Executing Agency'),'executing_agency_category':SelectColumn('Category', vocabulary='getCategoryVocab')},
            label_msgid='ProjectDatabase_label_ProjectExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Category"""),
        columns=('executing_agency','executing_agency_category'),
    ),
    DataGridField(
        name='OtherProjectExecutingPartners',
        widget=DataGridField._properties['widget'](
            label="Other Project Executing Partners",
            columns={'partner_name':Column('Partner'),'category':SelectColumn('Category',vocabulary='getCategoryVocab')},
            label_msgid='ProjectDatabase_label_OtherProjectExecutingPartners',
            i18n_domain='ProjectDatabase',
        ),
        columns=('partner_name','category'),
    ),
    BooleanField(
        name='JointImplementation',
        widget=BooleanWidget(
            label="Joint Implementation",
            label_msgid='ProjectDatabase_label_JointImplementation',
            i18n_domain='ProjectDatabase',
        ),
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
        default_output_type='text/html',
    ),
    StringField(
        name='GEFPhase',
        widget=SelectionWidget(
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""GEFPhase"""),
    ),
    DataGridField(
        name='ProjectImplementationStatus',
        widget=DataGridField._properties['widget'](
            label="Project Implementation Status",
            columns={'fiscal_year':Column('Fiscal Year'),'narrative':Column('Narrative'),'description':Column('Project activities and objectives met')},
            label_msgid='ProjectDatabase_label_ProjectImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        columns=('fiscal_year','narrative','description'),
    ),
    StringField(
        name='ImplementationMode',
        widget=SelectionWidget(
            label="Mode of Execution",
            label_msgid='ProjectDatabase_label_ImplementationMode',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationMode"""),
    ),
    StringField(
        name='Office',
        widget=StringField._properties['widget'](
            label="Office of Execution",
            label_msgid='ProjectDatabase_label_Office',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='Website',
        widget=StringField._properties['widget'](
            label="Project Website Address",
            label_msgid='ProjectDatabase_label_Website',
            i18n_domain='ProjectDatabase',
        ),
        validators=('isUrl',),
    ),
    ReferenceField(
        name='CurrentTaskManager',
        widget=ReferenceBrowserWidget(
            label="Current Task Manager",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_CurrentTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="Project_CurrentTaskManager",
        vocabulary='contactsVocab',
    ),
    ReferenceField(
        name='PreviousTaskManager',
        widget=ReferenceBrowserWidget(
            label="Previous Task Manager",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_PreviousTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="Project_PreviousTaskManager",
        multiValued=0,
        vocabulary='contactsVocab',
    ),
    ReferenceField(
        name='ProjectCoordinator',
        widget=ReferenceBrowserWidget(
            label="Project Coordinator",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_ProjectCoordinator',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="Project_ProjectCoordinator",
        multiValued=0,
        vocabulary='contactsVocab',
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
        default_output_type='text/html',
    ),
    MoneyField(
        name='LeveragedFinancingAmount',
        widget=MoneyField._properties['widget'](
            label="Leveraged Financing Amount",
            label_msgid='ProjectDatabase_label_LeveragedFinancingAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='LeveragedFinancingRemark',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Leveraged Financing Description",
            description="Enter sources and Purposes",
            label_msgid='ProjectDatabase_label_LeveragedFinancingRemark',
            description_msgid='ProjectDatabase_help_LeveragedFinancingRemark',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        vocabulary=NamedVocabulary("""LeadAgency"""),
    ),
    ComputedField(
        name='TotalGEFAllocation',
        widget=ComputedField._properties['widget'](
            label="Total GEF Allocation",
            label_msgid='ProjectDatabase_label_TotalGEFAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalUNEPAllocation',
        widget=ComputedField._properties['widget'](
            label="Total UNEP Allocation",
            label_msgid='ProjectDatabase_label_TotalUNEPAllocation',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCofinancingPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing (planned)",
            label_msgid='ProjectDatabase_label_TotalCofinancingPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCofinancingActual',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing (actual)",
            label_msgid='ProjectDatabase_label_TotalCofinancingActual',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalCashDisbursements',
        widget=ComputedField._properties['widget'](
            label="Total Cash Disbursements",
            label_msgid='ProjectDatabase_label_TotalCashDisbursements',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalIMISExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total IMIS Expenditures",
            label_msgid='ProjectDatabase_label_TotalIMISExpenditures',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='PDFAStatus',
        widget=ComputedField._properties['widget'](
            label="PDFA Status",
            label_msgid='ProjectDatabase_label_PDFAStatus',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='PDFBStatus',
        widget=ComputedField._properties['widget'](
            label="PDFB Status",
            label_msgid='ProjectDatabase_label_PDFBStatus',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='MSPStatus',
        widget=ComputedField._properties['widget'](
            label="MSP Status",
            label_msgid='ProjectDatabase_label_MSPStatus',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='FSPStatus',
        widget=ComputedField._properties['widget'](
            label="FSP Status",
            label_msgid='ProjectDatabase_label_FSPStatus',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label="Project Title",
            label_msgid='ProjectDatabase_label_ProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='Number',
        widget=SelectionWidget(
            description="Is this a Tranched/Phased/Addon project?",
            label='Number',
            label_msgid='ProjectDatabase_label_Number',
            description_msgid='ProjectDatabase_help_Number',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Number"""),
    ),
    IntegerField(
        name='PhasedTrancheNumber',
        default=0,
        widget=IntegerField._properties['widget'](
            label="Phase/Tranche Number",
            label_msgid='ProjectDatabase_label_PhasedTrancheNumber',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='title',
        widget=StringField._properties['widget'](
            visible={'edit':'hidden','view':'invisible'},
            label='Title',
            label_msgid='ProjectDatabase_label_title',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='LeveragedFinancingAmount',
        widget=MoneyField._properties['widget'](
            label="Leveraged Financing Amount",
            label_msgid='ProjectDatabase_label_LeveragedFinancingAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProjectGeneralInformation_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
title_field = ProjectGeneralInformation_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['TotalGEFAllocation'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['TotalUNEPAllocation'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['TotalCofinancingPlanned'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['TotalCofinancingActual'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['TotalCashDisbursements'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['TotalIMISExpenditures'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['PDFAStatus'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['PDFBStatus'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['MSPStatus'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['FSPStatus'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['ProjectTitle'].widget.visible = {'edit':'hidden', 'view':'invisible'}
ProjectGeneralInformation_schema['LeveragedFinancingAmount'].widget.size = 15
##/code-section after-schema

class ProjectGeneralInformation(BaseFolder, CurrencyMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IProjectGeneralInformation, IProject)

    meta_type = 'ProjectGeneralInformation'
    _at_rename_after_creation = True

    schema = ProjectGeneralInformation_schema

    ##code-section class-header #fill in your manual code here
    actions =  (
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
    ##/code-section class-header

    # Methods

    security.declarePublic('getTotalGEFAllocation')
    def getTotalGEFAllocation(self):
        """
        """
        #fmi_cash_objs = self.contentValues('Financials')
        #subproject_objs = self.contentValues('SubProject')
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        #subproject_objs = self['subprojectsfolder'].contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getGEFProjectAllocation():
                total += fmi_obj.getGEFProjectAllocation()
        # for sp_obj in subproject_objs:
        #     if sp_obj.getGEFProjectAllocation():
        #         total += sp_obj.getGEFProjectAllocation()
        return total

    security.declarePublic('getTotalUNEPAllocation')
    def getTotalUNEPAllocation(self):
        """
        """
        #fmi_cash_objs = self.contentValues('Financials')
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getCashUNEPAllocation():
                total += fmi_obj.getCashUNEPAllocation()
        return total

    security.declarePublic('getTotalCofinancingPlanned')
    def getTotalCofinancingPlanned(self):
        """
        """
        #fmi_cash_objs = self.contentValues('Financials')
        #subproject_objs = self.contentValues('SubProject')
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        #subproject_objs = self['subprojectsfolder'].contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCofinCashPlanned():
                total += fmi_obj.getSumCofinCashPlanned()
            if fmi_obj.getSumCofinInKindPlanned():
                total += fmi_obj.getSumCofinInKindPlanned()
        #for sp_obj in subproject_objs:
        #    if sp_obj.getSumCofinCashPlanned():
        #        total += sp_obj.getSumCofinCashPlanned()
        #    if sp_obj.getSumCofinInKindPlanned():
        #        total += sp_obj.getSumCofinInKindPlanned()
        return total

    security.declarePublic('getTotalCofinancingActual')
    def getTotalCofinancingActual(self):
        """
        """
        #fmi_cash_objs = self.contentValues('Financials')
        #subproject_objs = self.contentValues('SubProject')
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        #subproject_objs = self['subprojectsfolder'].contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCofinCashActual():
                total += fmi_obj.getSumCofinCashActual()
            if fmi_obj.getSumCofinInKindActual():
                total += fmi_obj.getSumCofinInKindActual()
        #for sp_obj in subproject_objs:
        #    if sp_obj.getSumCofinCashActual():
        #        total += sp_obj.getSumCofinCashActual()
        #    if sp_obj.getSumCofinInKindActual():
        #        total += sp_obj.getSumCofinInKindActual()
        return total

    security.declarePublic('getTotalCashDisbursements')
    def getTotalCashDisbursements(self):
        """
        """
        #fmi_cash_objs = self.contentValues('Financials')
        #subproject_objs = self.contentValues('SubProject')
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        #subproject_objs = self['subprojectsfolder'].contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumCashDisbursements():
                total += fmi_obj.getSumCashDisbursements()
        #for sp_obj in subproject_objs:
        #    if sp_obj.getSumCashDisbursements():
        #        total += sp_obj.getSumCashDisbursements()
        return total

    security.declarePublic('getTotalIMISExpenditures')
    def getTotalIMISExpenditures(self):
        """
        """
        #fmi_cash_objs = self.contentValues('Financials')
        #subproject_objs = self.contentValues('SubProject')
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        #subproject_objs = self['subprojectsfolder'].contentValues('SubProject')
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getSumIMISExpenditures():
                total += fmi_obj.getSumIMISExpenditures()
        #for sp_obj in subproject_objs:
        #    if sp_obj.getSumIMISExpenditures():
        #        total += sp_obj.getSumIMISExpenditures()
        return total

    security.declarePublic('getPDFAStatus')
    def getPDFAStatus(self):
        """
        """
        #fmi_objs = self.contentValues('Financials')
        fmi_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF A':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getPDFBStatus')
    def getPDFBStatus(self):
        """
        """
        #fmi_objs = self.contentValues('Financials')
        fmi_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF B':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getMSPStatus')
    def getMSPStatus(self):
        """
        """
        #fmi_objs = self.contentValues('Financials')
        fmi_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'MSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getFSPStatus')
    def getFSPStatus(self):
        """
        """
        #fmi_objs = self.contentValues('Financials')
        fmi_objs = self.getAProject()['fmi_folder'].contentValues('Financials')
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'FSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """ Code copied from previous project; dunno what it means...
        """
        return self.getAProject().Title()

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

    security.declarePublic('validate_PhasedTrancheNumber')
    def validate_PhasedTrancheNumber(self, value):
        """
        """
        val=0
        try:
            val = int(value)
        except ValueError:
            return 'Value must be an integer'

        return

    security.declarePublic('getCategoryVocab')
    def getCategoryVocab(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('Category')
        return vocab.getDisplayList(self)

    security.declarePublic('displayContentsTab')
    def displayContentsTab(self):
        """
        """
        return False

    # Manually created methods

    security.declarePublic('Title')
    def Title(self):
        """
        """
        #if hasattr(self, 'getAProject'):
        #    return 'Project General Information: ' + str(self.getAProject().Title())
        #else:
        #    return 'Project General Information'
        return 'Project General Information'

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


registerType(ProjectGeneralInformation, PROJECTNAME)
# end of class ProjectGeneralInformation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



