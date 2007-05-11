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
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Project Description",
            label_msgid='ProjectDatabase_label_SummaryDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

    LinesField(
        name='Country',
        schemata="Location",
        widget=MultiSelectionWidget(
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Country""")
    ),

    LinesField(
        name='OtherNonGEFEligibleCountries',
        widget=LinesField._properties['widget'](
            label="Other Non-GEF Eligible Project Participating Countries",
            label_msgid='ProjectDatabase_label_OtherNonGEFEligibleCountries',
            i18n_domain='ProjectDatabase',
        )
    ),

    LinesField(
        name='Scope',
        widget=MultiSelectionWidget(
            label='Scope',
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        schemata="Location",
        multiValued=1,
        vocabulary=NamedVocabulary("""Scope""")
    ),

    LinesField(
        name='Region',
        widget=MultiSelectionWidget(
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        schemata="Location",
        multiValued=1,
        vocabulary=NamedVocabulary("""Region""")
    ),

    StringField(
        name='FocalArea',
        index="FieldIndex:brains",
        widget=SelectionWidget(
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""FocalArea""")
    ),

    StringField(
        name='OperationalProgramme',
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

    StringField(
        name='StrategicPriority',
        widget=SelectionWidget(
            label="Strategic Priority",
            label_msgid='ProjectDatabase_label_StrategicPriority',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicPriority""")
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

    TextField(
        name='UnepComponentDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="UNEP Component Description",
            label_msgid='ProjectDatabase_label_UnepComponentDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

    StringField(
        name='GEFPhase',
        widget=SelectionWidget(
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""GEFPhase""")
    ),

    MoneyField(
        name='ImplementingAgencyFee',
        widget=MoneyField._properties['widget'](
            label="Implementing Agency Fee",
            label_msgid='ProjectDatabase_label_ImplementingAgencyFee',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='UNEPImplementingAgencyFee',
        widget=MoneyField._properties['widget'](
            label="UNEP Implementing Agency Fee",
            label_msgid='ProjectDatabase_label_UNEPImplementingAgencyFee',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='ImplementationMode',
        widget=SelectionWidget(
            label="Implementation Mode",
            label_msgid='ProjectDatabase_label_ImplementationMode',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ImplementationMode""")
    ),

    StringField(
        name='Office',
        widget=StringWidget(
            label='Office',
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
            label="Leveraged Financing Remark",
            label_msgid='ProjectDatabase_label_LeveragedFinancingRemark',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        schemata="Financing"
    ),

    TextField(
        name='ProjectResults',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Project Results",
            label_msgid='ProjectDatabase_label_ProjectResults',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html'
    ),

    ReferenceField(
        name='OtherImplementingAgency',
        widget=ReferenceField._properties['widget'](
            label="Other Implementing Agency",
            label_msgid='ProjectDatabase_label_OtherImplementingAgency',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Agency',),
        multiValued=0,
        relationship="Project_OtherImplementingAgency"
    ),

    StringField(
        name='LeadAgency',
        widget=SelectionWidget(
            label="Lead Agency",
            label_msgid='ProjectDatabase_label_LeadAgency',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=0,
        relationship="Project_LeadAgency",
        vocabulary=NamedVocabulary("""LeadAgency"""),
        allowed_types=('Agency',)
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
    allowed_content_types = ['ProjectImplementation', 'Financials', 'Milestone', 'SubProject'] + list(getattr(DocumentLinks, 'allowed_content_types', []))
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
        'id': 'view',
        'name': 'Project General Information',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
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
        pass

    security.declarePublic('getTotalUNEPAllocation')
    def getTotalUNEPAllocation(self):
        """
        """
        pass

    security.declarePublic('getTotalCofinancingPlanned')
    def getTotalCofinancingPlanned(self):
        """
        """
        pass

    security.declarePublic('getTotalCofinancingActual')
    def getTotalCofinancingActual(self):
        """
        """
        pass

    security.declarePublic('getTotalCashDisbursements')
    def getTotalCashDisbursements(self):
        """
        """
        pass

    security.declarePublic('getTotalIMISExpenditures')
    def getTotalIMISExpenditures(self):
        """
        """
        pass

    security.declarePublic('getPDFAStatus')
    def getPDFAStatus(self):
        """
        """
        pass

    security.declarePublic('getPDFBStatus')
    def getPDFBStatus(self):
        """
        """
        pass

    security.declarePublic('getMSPStatus')
    def getMSPStatus(self):
        """
        """
        pass

    security.declarePublic('getFSPStatus')
    def getFSPStatus(self):
        """
        """
        pass

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """
        """
        pass


registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
##/code-section module-footer



