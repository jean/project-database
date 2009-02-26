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

__author__ = """Mike Metcalfe <mikejmets@gmail.com>, Jurgen Blignaut
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
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
from Products.ProjectDatabase.utils import getYearVocabulary
from Products.DataGridField import MoneyColumn, ReferenceColumn

datagrid_schema = Schema((
    MoneyField(
        name='grant_to_unep',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='ProjectDatabase',
        ),
    ),

    MoneyField(
        name='grant_to_other_ia',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='ProjectDatabase',
        ),
    ),

    MoneyField(
        name='cofinancing',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='ProjectDatabase',
        ),
    ),

    MoneyField(
        name='unep_fee',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='ProjectDatabase',
        ),
    ),

    MoneyField(
        name='other_ia_fee',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="",
            i18n_domain='ProjectDatabase',
        ),
    ),
))
##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].write_permission = "TM"
schema = Schema((

    copied_fields['title'],

    ComputedField(
        name='DatabaseID',
        widget=ComputedField._properties['widget'](
            label="Database ID",
            label_msgid='ProjectDatabase_label_DatabaseID',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    TextField(
        name='FormerProjectTitle',
        widget=TextAreaWidget(
            label="Former Project Title",
            label_msgid='ProjectDatabase_label_FormerProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    StringField(
        name='GEFid',
        widget=StringField._properties['widget'](
            label="GEF ID",
            label_msgid='ProjectDatabase_label_GEFid',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="Registrar TM",
    ),
    LinesField(
        name='UNEPThematicPriority',
        widget=InAndOutWidget(
            label="UNEP Priority",
            label_msgid='ProjectDatabase_label_UNEPThematicPriority',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""UNEPThematicPriority"""),
        write_permission="TM",
    ),
    LinesField(
        name='FocalArea',
        widget=InAndOutWidget(
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""FocalArea"""),
        write_permission="TM",
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
        write_permission="TM",
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
        write_permission="TM",
    ),
    StringField(
        name='GEFPhase',
        widget=SelectionWidget(
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""GEFPhase"""),
        write_permission="TM",
    ),
    LinesField(
        name='Scope',
        widget=InAndOutWidget(
            label="Geographic Scope",
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Scope"""),
        write_permission="TM",
    ),
    StringField(
        name='ScopeOther',
        widget=StringField._properties['widget'](
            label="Other Geographic Scope",
            label_msgid='ProjectDatabase_label_ScopeOther',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    LinesField(
        name='Region',
        widget=InAndOutWidget(
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Region"""),
        write_permission="TM",
    ),
    StringField(
        name='SubRegion',
        widget=StringField._properties['widget'](
            label="Sub-Region",
            label_msgid='ProjectDatabase_label_SubRegion',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    LinesField(
        name='Country',
        widget=InAndOutWidget(
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Country"""),
        write_permission="TM",
    ),
    LinesField(
        name='OtherNonGEFEligibleCountries',
        widget=InAndOutWidget(
            label="Other Non-GEF Eligible Project Participating Countries",
            label_msgid='ProjectDatabase_label_OtherNonGEFEligibleCountries',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Country"""),
        write_permission="TM",
    ),
    StringField(
        name='TrustFund',
        widget=SelectionWidget(
            label="Trust Fund",
            label_msgid='ProjectDatabase_label_TrustFund',
            i18n_domain='ProjectDatabase',
        ),
        required=True,
        write_permission="TM",
        vocabulary=NamedVocabulary("""TrustFund"""),
    ),
    DataGridField(
        name='PIFFinancialData',
        widget=DataGridField._properties['widget'](
            columns={'stage':SelectColumn('Stage', vocabulary='getPIFStageVocabulary'), 'grant_to_unep':MoneyColumn('Grant to UNEP', field=datagrid_schema['grant_to_unep']), 'grant_to_other_ia':MoneyColumn('Grant to other IA', field=datagrid_schema['grant_to_other_ia']), 'cofinancing':MoneyColumn('Co-Financing', field=datagrid_schema['cofinancing']), 'unep_fee':MoneyColumn('UNEP Fee', field=datagrid_schema['unep_fee']), 'other_ia_fee':MoneyColumn('Other IA Fee', field=datagrid_schema['other_ia_fee'])},
            label="Financial Data at PIF",
            label_msgid='ProjectDatabase_label_PIFFinancialData',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        columns=('stage', 'grant_to_unep', 'grant_to_other_ia', 'cofinancing', 'unep_fee', 'other_ia_fee'),
    ),
    BooleanField(
        name='JointImplementation',
        widget=BooleanWidget(
            label="Joint Implementation",
            label_msgid='ProjectDatabase_label_JointImplementation',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
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
        write_permission="TM",
    ),
    StringField(
        name='LeadAgency',
        widget=SelectionWidget(
            label="Lead GEF Agency",
            label_msgid='ProjectDatabase_label_LeadAgency',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
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
        relationship="Project_LeadAgency",
        multiValued=0,
        allowed_types=('Person',),
        write_permission="TM",
    ),
    LinesField(
        name='OtherImplementingAgency',
        widget=InAndOutWidget(
            label="Other GEF Agency(ies)",
            label_msgid='ProjectDatabase_label_OtherImplementingAgency',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""LeadAgency"""),
        write_permission="TM",
    ),
    StringField(
        name='ExecutionMode',
        widget=SelectionWidget(
            label="Mode of Execution",
            label_msgid='ProjectDatabase_label_ExecutionMode',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        vocabulary=NamedVocabulary("""ExecutionMode"""),
    ),
    StringField(
        name='LeadDivision',
        widget=SelectionWidget(
            label="Lead Division",
            label_msgid='ProjectDatabase_label_LeadDivision',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        vocabulary=NamedVocabulary("""Division"""),
    ),
    LinesField(
        name='OtherDivisions',
        widget=InAndOutWidget(
            label="Other Divisions",
            label_msgid='ProjectDatabase_label_OtherDivisions',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Division"""),
        write_permission="TM",
    ),
    DataGridField(
        name='ProjectExecutingAgency',
        vocabulary=NamedVocabulary("""Category"""),
        widget=DataGridField._properties['widget'](
            label="Lead Executing Agency",
            columns={'executing_agency':ReferenceColumn('Executing Agency', fieldname='ExecutingAgencyName'),'executing_agency_category':SelectColumn('Category', vocabulary='getCategoryVocab')},
            label_msgid='ProjectDatabase_label_ProjectExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        columns=('executing_agency','executing_agency_category'),
    ),
    DataGridField(
        name='OtherProjectExecutingPartners',
        widget=DataGridField._properties['widget'](
            label="Other Project Executing Partners",
            columns={'partner_name':ReferenceColumn('Partner', fieldname='OtherExecutingPartnerName'),'category':SelectColumn('Category',vocabulary='getCategoryVocab')},
            label_msgid='ProjectDatabase_label_OtherProjectExecutingPartners',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        columns=('partner_name','category'),
    ),
    DataGridField(
        name='ProjectImplementationStatus',
        widget=DataGridField._properties['widget'](
            label="Project Implementation Status",
            columns={'fiscal_year':SelectColumn('Fiscal Year', vocabulary='getFiscalYearVocabulary'),'narrative':Column('Project activities and objectives met')},
            label_msgid='ProjectDatabase_label_ProjectImplementationStatus',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        columns=('fiscal_year','narrative'),
    ),
    DataGridField(
        name='TaskManager',
        widget=DataGridField._properties['widget'](
            label="Task Manager",
            columns={'name':ReferenceColumn('Name', fieldname='TaskManagerName'),'category':SelectColumn('Category', vocabulary='getTMCategoryVocab'),'period':SelectColumn('Period', vocabulary='getFiscalYearVocabulary')},
            label_msgid='ProjectDatabase_label_TaskManager',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        columns=('name','category','period'),
    ),
    StringField(
        name='RiskRatingAtInception',
        widget=SelectionWidget(
            label="Risk Rating at Inception",
            label_msgid='ProjectDatabase_label_RiskRatingAtInception',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        vocabulary=NamedVocabulary("""InceptionRiskRating"""),
    ),
    TextField(
        name='RiskRatingComments',
        widget=TextAreaWidget(
            label="Risk Rating Comments",
            label_msgid='ProjectDatabase_label_RiskRatingComments',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ReferenceField(
        name='ProjectManager',
        widget=ReferenceBrowserWidget(
            label="Project Manager",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_ProjectManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        multiValued=0,
        relationship="Project_ProjectManager",
        write_permission="TM",
    ),
    StringField(
        name='Website',
        widget=StringField._properties['widget'](
            label="Project Website Address",
            label_msgid='ProjectDatabase_label_Website',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        validators=('isUrl',),
    ),
    TextField(
        name='ProjectResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Project Results",
            description="Enter overall Project Results AFTER Project Terminal Evaluation",
            label_msgid='ProjectDatabase_label_ProjectResults',
            description_msgid='ProjectDatabase_help_ProjectResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        write_permission="TM",
    ),
    StringField(
        name='PhaseTranche',
        widget=SelectionWidget(
            label="Is this a Tranched/Phased/Addon Project?",
            label_msgid='ProjectDatabase_label_PhaseTranche',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
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
        write_permission="TM",
    ),
    LinesField(
        name='OperationalProgramme',
        widget=InAndOutWidget(
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""OperationalProgramme"""),
        write_permission="TM",
    ),
    LinesField(
        name='EABiodiversity',
        widget=InAndOutWidget(
            label="EA Biodiversity",
            label_msgid='ProjectDatabase_label_EABiodiversity',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EABiodiversity"""),
        write_permission="TM",
    ),
    LinesField(
        name='EAClimateChange',
        widget=InAndOutWidget(
            label="EA Climate Change",
            label_msgid='ProjectDatabase_label_EAClimateChange',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAClimateChange"""),
        write_permission="TM",
    ),
    LinesField(
        name='EAPOP',
        widget=InAndOutWidget(
            label="EA POP",
            label_msgid='ProjectDatabase_label_EAPOP',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""EAPOP"""),
        write_permission="TM",
    ),
    LinesField(
        name='EAMultipleFocalAreas',
        widget=InAndOutWidget(
            label="Multiple Focal Areas",
            label_msgid='ProjectDatabase_label_EAMultipleFocalAreas',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""MultipleFocalAreas"""),
        write_permission="TM",
    ),
    StringField(
        name='StrategicPriority',
        widget=SelectionWidget(
            label="Strategic Priority",
            label_msgid='ProjectDatabase_label_StrategicPriority',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicPriority"""),
        write_permission="TM",
    ),
    StringField(
        name='StrategicObjectives',
        widget=SelectionWidget(
            label="Strategic Objectives",
            label_msgid='ProjectDatabase_label_StrategicObjectives',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        vocabulary=NamedVocabulary("""StrategicObjectives"""),
    ),
    StringField(
        name='StrategicProgram',
        widget=SelectionWidget(
            label="Strategic Program",
            label_msgid='ProjectDatabase_label_StrategicProgram',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
        vocabulary=NamedVocabulary("""StrategicProgram"""),
    ),
    ComputedField(
        name='TotalGEFAllocation',
        widget=ComputedField._properties['widget'](
            label="Total GEF Allocation",
            visible={'view':'invisible', 'edit':'hidden'},
            label_msgid='ProjectDatabase_label_TotalGEFAllocation',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='TotalUNEPAllocation',
        widget=ComputedField._properties['widget'](
            label="Total UNEP Allocation",
            visible={'view':'invisible', 'edit':'hidden'},
            label_msgid='ProjectDatabase_label_TotalUNEPAllocation',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='TotalCoFinancingPlanned',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing (planned)",
            visible={'view':'invisible', 'edit':'hidden'},
            label_msgid='ProjectDatabase_label_TotalCoFinancingPlanned',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='TotalCoFinancingActual',
        widget=ComputedField._properties['widget'](
            label="Total Co-financing (actual)",
            visible={'view':'invisible', 'edit':'hidden'},
            label_msgid='ProjectDatabase_label_TotalCoFinancingActual',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='TotalCashDisbursements',
        widget=ComputedField._properties['widget'](
            label="Total Cash Disbursements",
            visible={'view':'invisible', 'edit':'hidden'},
            label_msgid='ProjectDatabase_label_TotalCashDisbursements',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='TotalYearlyExpenditures',
        widget=ComputedField._properties['widget'](
            label="Total Yearly Expenditures",
            visible={'view':'invisible', 'edit':'hidden'},
            label_msgid='ProjectDatabase_label_TotalYearlyExpenditures',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='PDFAStatus',
        widget=ComputedField._properties['widget'](
            label="PDFA Status",
            label_msgid='ProjectDatabase_label_PDFAStatus',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='PDFBStatus',
        widget=ComputedField._properties['widget'](
            label="PDFB Status",
            label_msgid='ProjectDatabase_label_PDFBStatus',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='PDFCStatus',
        widget=ComputedField._properties['widget'](
            label="PDFC Status",
            label_msgid='ProjectDatabase_label_PDFCStatus',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='PPGStatus',
        widget=ComputedField._properties['widget'](
            label="PPG Status",
            label_msgid='ProjectDatabase_label_PPGStatus',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='MSPStatus',
        widget=ComputedField._properties['widget'](
            label="MSP Status",
            label_msgid='ProjectDatabase_label_MSPStatus',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ComputedField(
        name='FSPStatus',
        widget=ComputedField._properties['widget'](
            label="FSP Status",
            label_msgid='ProjectDatabase_label_FSPStatus',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    BooleanField(
        name='ProgrammeFramework',
        widget=BooleanField._properties['widget'](
            label="Is this project in a Programme Framework?",
            label_msgid='ProjectDatabase_label_ProgrammeFramework',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),
    ReferenceField(
        name='ProgrammeFrameworkTitle',
        widget=ReferenceBrowserWidget(
            label="Programme Framework Title",
            label_msgid='ProjectDatabase_label_ProgrammeFrameworkTitle',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('ProgrammeFramework',),
        multiValued=0,
        relationship="project_programmeframework",
        write_permission="TM",
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
        write_permission="TM",
    ),
    MoneyField(
        name='LeveragedFinancingAmount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="Leveraged Financing Amount",
            label_msgid='ProjectDatabase_label_LeveragedFinancingAmount',
            i18n_domain='ProjectDatabase',
        ),
        write_permission="TM",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProjectGeneralInformation_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ProjectGeneralInformation_schema['title'].widget.label = 'Project Title'
ProjectGeneralInformation_schema['LeadAgencyContact'].widget.startup_directory_method = \
        'getContactsPath'
ProjectGeneralInformation_schema['ProjectManager'].widget.startup_directory_method = \
        'getContactsPath'
ProjectGeneralInformation_schema['ProgrammeFrameworkTitle'].widget.startup_directory_method = \
        'getPGFPath'

ProjectGeneralInformation_schema = ProjectGeneralInformation_schema.copy()  + Schema((

    ReferenceField("fakeTaskManagerName",
            widget = ReferenceBrowserWidget(
                label="Task Manager",
                visible={'view':'invisible', 'edit':'hidden'},
                startup_directory='/contacts',
            ),
            allowed_types=('Person',),
            relationship='pgi_taskmanager_fake',
            multiValued=0,
        ),

    ReferenceField("fakeExecutingAgencyName",
            widget = ReferenceBrowserWidget(
                label="Executing Agency",
                visible={'view':'invisible', 'edit':'hidden'},
                startup_directory='/contacts',
            ),
            allowed_types=('Organisation',),
            relationship='pgi_executingagency_fake',
            multiValued=0,
        ),

    ReferenceField("fakeOtherExecutingPartnerName",
            widget = ReferenceBrowserWidget(
                label="Partner",
                visible={'view':'invisible', 'edit':'hidden'},
                startup_directory='/contacts',
            ),
            allowed_types=('Organisation',),
            relationship='pgi_executingpartner_fake',
            multiValued=0,
        ),
))
#
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
    ##/code-section class-header

    # Methods

    security.declarePublic('getTotalGEFAllocation')
    def getTotalGEFAllocation(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            total += fmi_obj.getCommittedGEFGrant()
        return total

    security.declarePublic('getTotalUNEPAllocation')
    def getTotalUNEPAllocation(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            total += fmi_obj.getTotalFinanceObject()
        return total

    security.declarePublic('getTotalCoFinancingPlanned')
    def getTotalCoFinancingPlanned(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            total += fmi_obj.getSumCoFinCashPlanned()
            total += fmi_obj.getSumCoFinInKindPlanned()
        return total

    security.declarePublic('getTotalCoFinancingActual')
    def getTotalCoFinancingActual(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            total += fmi_obj.getSumCoFinCashActual()
            total += fmi_obj.getSumCoFinInKindActual()
        return total

    security.declarePublic('getTotalCashDisbursements')
    def getTotalCashDisbursements(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            total += fmi_obj.getSumCashDisbursements()
        return total

    security.declarePublic('getTotalYearlyExpenditures')
    def getTotalYearlyExpenditures(self):
        """
        """
        fmi_cash_objs = self.getAProject()['fmi_folder'].contentValues({'portal_type':'Financials'})
        total = self.getZeroMoneyInstance()
        for fmi_obj in fmi_cash_objs:
            total += fmi_obj.getSumYearlyExpenditures()
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
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('Category')
        return vocab.getDisplayList(self)

    security.declarePublic('displayContentsTab')
    def displayContentsTab(self):
        """
        """
        return False

    # Manually created methods

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

    security.declarePublic('getTMCategoryVocab')
    def getTMCategoryVocab(self):
        """
        """
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('TMCategory')
        return vocab.getDisplayList(self)

    def getPIFStageVocabulary(self):
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('PIFStage')
        return vocab.getDisplayList(self)

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

    def getDatabaseID(self):
        return self.aq_inner.aq_parent.getId()

    def getFocalAreaNames(self):
        areas = self.getFocalArea()
        return self.getSelectedVocabularyValues(areas, 'FocalArea')

    def getProjectTypeName(self):
        type = self.getProjectType()
        return self.getSelectedVocabularyValue(type, 'ProjectType')

    def getRegionNames(self):
        areas = self.getRegion()
        return self.getSelectedVocabularyValues(areas, 'Region')

    def getCountryNames(self):
        countries = self.getCountry()
        return self.getSelectedVocabularyValues(countries, 'Country')

    def getUNEPPriorityNames(self):
        names = self.getUNEPThematicPriority()
        return self.getSelectedVocabularyValues(names, 'UNEPThematicPriority')

    def getGeographicScopeValues(self):
        scopes = self.getScope()
        return self.getSelectedVocabularyValues(scopes, 'Scope')

    def getStrategicObjectiveName(self):
        objective = self.getStrategicObjectives()
        return self.getSelectedVocabularyValue(objective, 'StrategicObjectives')

    def getLeadExecutingAgencyNames(self):
        values = self.getProjectExecutingAgency()
        result = ''
        if values:
            for v in values:
                if v['executing_agency']:
                    result += v['executing_agency'] + ', '
        if len(result) > 2:
            result = result[:-2]
        else:
            result = 'Unspecified'
        return result

    def getOtherExecutingAgencyNames(self):
        values = self.getOtherProjectExecutingPartners()
        result = ''
        if values:
            refcat = getToolByName(self, 'reference_catalog')
            for v in values:
                if v['partner_name']:
                    partner = refcat.lookupObject(v['partner_name'])
                    if partner is not None:
                        name = partner.getName()
                    else:
                        name = 'Unspecified'
                    result += name + ', '
        if len(result) > 2:
            result = result[:-2]
        else:
            result = 'Unspecified'
        return result

    def getAllExecutingAgencyNames(self):
        result = self.getLeadExecutingAgencyNames()
        if result != 'Unspecified':
            tmp = self.getOtherExecutingAgencyNames()
            if tmp != 'Unspecified':
                result = result + ', ' + tmp
        return result

    def getLeadGEFAgencyName(self):
        lead = self.getLeadAgency()
        return self.getSelectedVocabularyValue(lead, 'LeadAgency')

    def getStrategicPriorityName(self):
        priority = self.getStrategicPriority()
        return self.getSelectedVocabularyValue(priority, 'StrategicPriority')

    def getGEFAgencyNames(self):
        lead = self.getLeadAgency()
        result = self.getSelectedVocabularyValue(lead, 'LeadAgency')
        other = self.getOtherImplementingAgency()
        if other:
            result += ', ' + self.getSelectedVocabularyValues(other, 'LeadAgency')
        return result

    def getTaskManagers(self):
        values = self.getTaskManager()
        result = ''
        if values:
            refcat = getToolByName(self, 'reference_catalog')
            for v in values:
                if v['name']:
                    mem = refcat.lookupObject(v['name'])
                    if mem is not None:
                        name = mem.getFullname()
                    else:
                        name = 'Unspecified'
                    result += name + ', '
        if len(result) > 2:
            result = result[:-2]
        else:
            result = 'Unspecified'
        return result

    def getSelectedVocabularyValue(self, selection, vocabName):
        if selection:
            atvm = getToolByName(self, 'portal_vocabularies')
            vocab = atvm.getVocabularyByName(vocabName)
            dict = vocab.getVocabularyDict(self)
            return dict[selection][0]
        return None

    def getSelectedVocabularyValues(self, selections, vocabName):
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName(vocabName)
        dict = vocab.getVocabularyDict(self)
        result = ''
        for value in selections:
            result += dict[value][0] + ', '
        return result[:-2]

    def getCurrentTM(self):
        values = self.getTaskManager()
        if values:
            refcat = getToolByName(self, 'reference_catalog')
            date = '1900'
            for v in values:
                if v['period'] and v['name'] and v['category'] == 'Principal':
                    if date < v['period']:
                        date = v['period']
                        mem = refcat.lookupObject(v['name'])
                        if mem is not None:
                            name = mem.getFullname()
                        else:
                            name = 'Unspecified'
            if date != '1900':
                return name
        return 'Unspecified'

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

    def getPIFTotalGEFAmount(self):
        values = self.getPIFFinancialData()
        amount = self.getZeroMoneyInstance()
        for v in values:
            amount += v['grant_to_unep'] + \
                    v['grant_to_other_ia'] + \
                    v['unep_fee'] + \
                    v['other_ia_fee']
        return amount

    def getPIFUNEPGEFAmount(self):
        values = self.getPIFFinancialData()
        amount = self.getZeroMoneyInstance()
        for v in values:
            amount += v['grant_to_unep']
        return amount

    def getPIFUNEPFee(self):
        values = self.getPIFFinancialData()
        amount = self.getZeroMoneyInstance()
        for v in values:
            amount += v['unep_fee']
        return amount

    def getPIFCofinancingAmount(self):
        values = self.getPIFFinancialData()
        amount = self.getZeroMoneyInstance()
        for v in values:
            amount += v['cofinancing']
        return amount

    def getPIFPPGAmount(self):
        values = self.getPIFFinancialData()
        amount = self.getZeroMoneyInstance()
        for v in values:
            if v['stage'] == 'PPG':
                amount += v['grant_to_unep']
        return amount

    security.declarePublic('getPGFPath')
    def getPGFPath(self):
        purl = getToolByName(self, 'portal_url').getPortalObject().absolute_url()
        pc = getToolByName(self, 'portal_catalog')
        brains = pc({'portal_type':'FrameworkDatabase'})
        if len(brains) > 0:
            pgf = brains[0].getObject()
            curl = pgf.absolute_url()
            return curl[len(purl)+1:]
        return ''

    def getHideFieldNames(self):
        fieldnames = []
        if self.getExecutionMode() == 'External':
            fieldnames.append('LeadDivision')
            fieldnames.append('OtherDivisions')
        if self.getJointImplementation() == False:
            fieldnames.append('UnepComponentDescription')
        if self.getGEFPhase() != 'I' and \
           self.getGEFPhase() != 'II' and \
           self.getGEFPhase() != 'III':
            fieldnames.append('OperationalProgramme')
        if self.getGEFPhase() != 'II' and self.getGEFPhase() != 'III':
            fieldnames.append('StrategicPriority')
        if self.getGEFPhase() != 'IV':
            fieldnames.append('StrategicObjectives')
            fieldnames.append('StrategicProgram')
        if not(self.getProjectType() == 'EA' and \
               'BD' in self.getFocalArea()):
            fieldnames.append('EABiodiversity')
            fieldnames.append('EAClimateChange')
            fieldnames.append('EAPOP')
            fieldnames.append('EAMultipleFocalAreas')

        return fieldnames

    def getToggleFieldNames(self, fieldname, value=None, **kwargs):
        hide = []
        show = []
        if fieldname == 'ExecutionMode':
            if value == 'External':
                hide.append('LeadDivision')
                hide.append('OtherDivisions')
            else:
                show.append('LeadDivision')
                show.append('OtherDivisions')

        if fieldname == 'JointImplementation':
          if value == 'on':
              show.append('UnepComponentDescription')
          else:
              hide.append('UnepComponentDescription')

        if fieldname == 'GEFPhase':
            if value != 'I' and \
               value != 'II' and \
               value != 'III':
                hide.append('OperationalProgramme')
            else:
                show.append('OperationalProgramme')
            if value != 'II' and \
               value != 'III':
                hide.append('StrategicPriority')
            else:
                show.append('StrategicPriority')
            if value != 'IV':
                hide.append('StrategicObjectives')
                hide.append('StrategicProgram')
            else:
                show.append('StrategicObjectives')
                show.append('StrategicProgram')

        if fieldname == 'ProjectType':
            if value == 'EA' and 'BD' in kwargs['FocalArea']:
                show.append('EABiodiversity')
                show.append('EAClimateChange')
                show.append('EAPOP')
                show.append('EAMultipleFocalAreas')
            else:
                hide.append('EABiodiversity')
                hide.append('EAClimateChange')
                hide.append('EAPOP')
                hide.append('EAMultipleFocalAreas')

        if fieldname == 'FocalArea':
            if kwargs.get('ProjectType', None) and \
               kwargs['ProjectType'] == 'EA' and \
               'BD' in value:
                show.append('EABiodiversity')
                show.append('EAClimateChange')
                show.append('EAPOP')
                show.append('EAMultipleFocalAreas')
            else:
                hide.append('EABiodiversity')
                hide.append('EAClimateChange')
                hide.append('EAPOP')
                hide.append('EAMultipleFocalAreas')

        return show, hide

    def getFiscalYearVocabulary(self):
        return getYearVocabulary()



registerType(ProjectGeneralInformation, PROJECTNAME)
# end of class ProjectGeneralInformation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



