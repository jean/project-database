# -*- coding: utf-8 -*-
#
# File: ProjectGeneralInformation.py
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
from Products.ProjectDatabase.content.CurrencyMixin import CurrencyMixin
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
# from Products.ProjectDatabase.content.SubProjectFolder import SubProjectFolder
import permissions
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            visible={'edit':'hidden','view':'invisible'},
            label="Project Title",
            label_msgid='ProjectDatabase_label_title',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='DatabaseID',
        widget=StringField._properties['widget'](
            label='Databaseid',
            label_msgid='ProjectDatabase_label_DatabaseID',
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
    TextField(
        name='FormerProjectTitle',
        widget=TextAreaWidget(
            label="Former Project Title",
            label_msgid='ProjectDatabase_label_FormerProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='GEFid',
        widget=StringField._properties['widget'](
            label="GEF ID",
            description="Enter the 5 digit GEF ID",
            label_msgid='ProjectDatabase_label_GEFid',
            description_msgid='ProjectDatabase_help_GEFid',
            i18n_domain='ProjectDatabase',
        ),
    ),
    LinesField(
        name='UNEPThematicPriority',
        widget=MultiSelectionWidget(
            label="UNEP Thematic Priority",
            label_msgid='ProjectDatabase_label_UNEPThematicPriority',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""UNEPThematicPriority"""),
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
        name='GEFPhase',
        widget=SelectionWidget(
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""GEFPhase"""),
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
            label="Other Geographic Scope",
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
    StringField(
        name='SubRegion',
        widget=StringField._properties['widget'](
            label="Sub-Region",
            label_msgid='ProjectDatabase_label_SubRegion',
            i18n_domain='ProjectDatabase',
        ),
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
        multiValued=0,
        relationship="Project_LeadAgency",
        allowed_types=('Person',),
    ),
    LinesField(
        name='OtherImplementingAgency',
        widget=MultiSelectionWidget(
            label="Other GEF Agency(ies)",
            label_msgid='ProjectDatabase_label_OtherImplementingAgency',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""LeadAgency"""),
    ),
    StringField(
        name='ExecutionMode',
        widget=SelectionWidget(
            label="Mode of Execution",
            label_msgid='ProjectDatabase_label_ExecutionMode',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ExecutionMode"""),
    ),
    StringField(
        name='LeadDivision',
        widget=SelectionWidget(
            label="Lead Division",
            label_msgid='ProjectDatabase_label_LeadDivision',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Division"""),
    ),
    LinesField(
        name='OtherDivisions',
        widget=MultiSelectionWidget(
            label="Other Division",
            label_msgid='ProjectDatabase_label_OtherDivisions',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Division"""),
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
    DataGridField(
        name='ProjectImplementationStatus',
        widget=DataGridField._properties['widget'](
            label="Project Implementation Status",
            columns={'fiscal_year':Column('Fiscal Year'),'narrative_description':Column('Project activities and objectives met')},
            label_msgid='ProjectDatabase_label_ProjectImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        columns=('fiscal_year','narrative_description'),
    ),
    DataGridField(
        name='TaskManager',
        widget=DataGridField._properties['widget'](
            label="Task Manager",
            columns={'name':Column('Name'),'category':SelectColumn('Category', vocabulary='getTMCategoryVocab'),'period':Column('Period')},
            label_msgid='ProjectDatabase_label_TaskManager',
            i18n_domain='ProjectDatabase',
        ),
        columns=('name','category','period'),
    ),
    MoneyField(
        name='PDFAmount',
        widget=MoneyField._properties['widget'](
            label="PDF Amount",
            label_msgid='ProjectDatabase_label_PDFAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='PPGUNEPAmount',
        widget=MoneyField._properties['widget'](
            label='Ppgunepamount',
            label_msgid='ProjectDatabase_label_PPGUNEPAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='PPGUNEPFeeAmount',
        widget=MoneyField._properties['widget'](
            label='Ppgunepfeeamount',
            label_msgid='ProjectDatabase_label_PPGUNEPFeeAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='PPGOtherIAAmount',
        widget=MoneyField._properties['widget'](
            label='Ppgotheriaamount',
            label_msgid='ProjectDatabase_label_PPGOtherIAAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='PPGOtherIAFeeAmount',
        widget=MoneyField._properties['widget'](
            label='Ppgotheriafeeamount',
            label_msgid='ProjectDatabase_label_PPGOtherIAFeeAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='ProjectUNEPAmount',
        widget=MoneyField._properties['widget'](
            label='Projectunepamount',
            label_msgid='ProjectDatabase_label_ProjectUNEPAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='ProjectUNEPFeeAmount',
        widget=MoneyField._properties['widget'](
            label='Projectunepfeeamount',
            label_msgid='ProjectDatabase_label_ProjectUNEPFeeAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='ProjectOtherIAAmount',
        widget=MoneyField._properties['widget'](
            label='Projectotheriaamount',
            label_msgid='ProjectDatabase_label_ProjectOtherIAAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='ProjectOtherIAFeeAmount',
        widget=MoneyField._properties['widget'](
            label='Projectotheriafeeamount',
            label_msgid='ProjectDatabase_label_ProjectOtherIAFeeAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalPPGAmount',
        widget=ComputedField._properties['widget'](
            label='Totalppgamount',
            label_msgid='ProjectDatabase_label_TotalPPGAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TotalProjectAmount',
        widget=ComputedField._properties['widget'](
            label='Totalprojectamount',
            label_msgid='ProjectDatabase_label_TotalProjectAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='ProjectGrantTotal',
        widget=ComputedField._properties['widget'](
            label='Projectgranttotal',
            label_msgid='ProjectDatabase_label_ProjectGrantTotal',
            i18n_domain='ProjectDatabase',
        ),
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
        multiValued=0,
        relationship="Project_ProjectCoordinator",
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
            description="Enter Sources and Purposes",
            label_msgid='ProjectDatabase_label_LeveragedFinancingRemark',
            description_msgid='ProjectDatabase_help_LeveragedFinancingRemark',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
    ),
    StringField(
        name='PhaseTranche',
        widget=SelectionWidget(
            label="Is this a Tranched/Phased/Addon Project?",
            label_msgid='ProjectDatabase_label_PhaseTranche',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""PhasedTranche"""),
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
    LinesField(
        name='OperationalProgramme',
        widget=MultiSelectionWidget(
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""OperationalProgramme"""),
    ),
    LinesField(
        name='EABiodiversity',
        widget=MultiSelectionWidget(
            label="EA Biodiversity",
            label_msgid='ProjectDatabase_label_EABiodiversity',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EABiodiversity"""),
    ),
    LinesField(
        name='EAClimateChange',
        widget=MultiSelectionWidget(
            label="EA Climate Change",
            label_msgid='ProjectDatabase_label_EAClimateChange',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAClimateChange"""),
    ),
    LinesField(
        name='EAPOP',
        widget=MultiSelectionWidget(
            label="EA POP",
            label_msgid='ProjectDatabase_label_EAPOP',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAPOP"""),
    ),
    LinesField(
        name='EAMultipleFocalAreas',
        widget=MultiSelectionWidget(
            label="Multiple Focal Areas",
            label_msgid='ProjectDatabase_label_EAMultipleFocalAreas',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""MultipleFocalAreas"""),
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
        name='PDFCStatus',
        widget=ComputedField._properties['widget'](
            label='Pdfcstatus',
            label_msgid='ProjectDatabase_label_PDFCStatus',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='PPGStatus',
        widget=ComputedField._properties['widget'](
            label='Ppgstatus',
            label_msgid='ProjectDatabase_label_PPGStatus',
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
    BooleanField(
        name='ProgrammeFramework',
        widget=BooleanField._properties['widget'](
            label="Is this project in a Programme Framework?",
            label_msgid='ProjectDatabase_label_ProgrammeFramework',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ReferenceField(
        name='ProgrammeFrameworkTitle',
        widget=ReferenceBrowserWidget(
            label='Programmeframeworktitle',
            label_msgid='ProjectDatabase_label_ProgrammeFrameworkTitle',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('ProgrammeFramework',),
        relationship="project_programmeframework",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProjectGeneralInformation_schema = BaseSchema.copy() + \
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

ProjectGeneralInformation_schema['LeadAgencyContact'].widget.startup_directory = '/contacts'
# ProjectGeneralInformation_schema['CurrentTaskManager'].widget.startup_directory = '/contacts'
# ProjectGeneralInformation_schema['PreviousTaskManager'].widget.startup_directory = '/contacts'
ProjectGeneralInformation_schema['ProjectCoordinator'].widget.startup_directory = '/contacts'
##/code-section after-schema

class ProjectGeneralInformation(BaseContent, CurrencyMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProjectGeneralInformation)

    meta_type = 'ProjectGeneralInformation'
    _at_rename_after_creation = True

    schema = ProjectGeneralInformation_schema

    ##code-section class-header #fill in your manual code here
    # schema.moveField('GEFid', after='title')
    ##/code-section class-header

    # Methods

    security.declarePublic('getTotalGEFAllocation')
    def getTotalGEFAllocation(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
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
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            if fmi_obj.getCashUNEPAllocation():
                total += fmi_obj.getCashUNEPAllocation()
        return total

    security.declarePublic('getTotalCofinancingPlanned')
    def getTotalCofinancingPlanned(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
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
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
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
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
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
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
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
        fmi_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF A':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getPDFBStatus')
    def getPDFBStatus(self):
        """
        """
        fmi_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF B':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getPDFCStatus')
    def getPDFCStatus(self):
        """
        """
        fmi_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PDF C':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getMSPStatus')
    def getMSPStatus(self):
        """
        """
        fmi_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'MSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getFSPStatus')
    def getFSPStatus(self):
        """
        """
        fmi_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'FSP':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getPPGStatus')
    def getPPGStatus(self):
        """
        """
        fmi_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        status = ''
        for fmi_obj in fmi_objs:
            if fmi_obj.getFinanceCategory() == 'PPG':
                status = fmi_obj.getStatus()
        return status

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """ Code copied from previous project; dunno what it means...
        """
        return self.getAProject().Title()

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

    security.declarePublic('getTMCategoryVocab')
    def getTMCategoryVocab(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('TMCategory')
        return vocab.getDisplayList(self)


    security.declarePublic('displayContentsTab')
    def displayContentsTab(self):
        """
        """
        return False

    # security.declarePublic('validate_GEFid')
    # def validate_GEFid(self, value):
    #     """
    #     Check that the GEF id consists of 5 digits
    #     """
    #     if len(value) != 5:
    #         return 'The GEF ID must be 5 digits in length'

    #     for char in value:
    #         if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    #             return 'Only digits are allowed in the GEF ID'

    #     return None

    # Manually created methods

    security.declarePublic('getProjectTitle')
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


    security.declarePublic('getTotalPPGAmount')
    def getTotalPPGAmount(self):
        """
        """
        return 0.0

    security.declarePublic('getTotalProjectAmount')
    def getTotalProjectAmount(self):
        """
        """
        return 0.0

    security.declarePublic('getProjectGrantTotal')
    def getProjectGrantTotal(self):
        """
        """
        return 0.0


registerType(ProjectGeneralInformation, PROJECTNAME)
# end of class ProjectGeneralInformation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



