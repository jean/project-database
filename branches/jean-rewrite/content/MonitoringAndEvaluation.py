# -*- coding: utf-8 -*-
#
# File: MonitoringAndEvaluation.py
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
##/code-section module-header

schema = Schema((

    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label="Joint Evaluation Agency Contact",
            description="Name of evaluation officer in the other agency",
            label_msgid='ProjectDatabase_label_ProjectTitle',
            description_msgid='ProjectDatabase_help_ProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
        relationship="EvaluationAgencyContact"
    ),

    StringField(
        name='IMISNumber',
        dummy="IMIS Number",
        widget=StringWidget(
            label="IMIS Number",
            label_msgid='ProjectDatabase_label_IMISNumber',
            i18n_domain='ProjectDatabase',
        )
    ),

    ReferenceField(
        name='CurrentTaskManager',
        dummy="""Current Task Manager
        python:('mxmContacstPerson',)""",
        widget=ReferenceField._properties['widget'](
            label="Current Task Manager",
            label_msgid='ProjectDatabase_label_CurrentTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        relationship="MandE_TaskManager"
    ),

    ReferenceField(
        name='FundManagementOfficer',
        dummy=('mxmContactsPerson',),
        widget=ReferenceField._properties['widget'](
            label="Fund Manager Officer",
            label_msgid='ProjectDatabase_label_FundManagementOfficer',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        relationship="MandE_fundmanagerofficer"
    ),

    DateTimeField(
        name='CEOApproval',
        widget=CalendarWidget(
            label="CEO Approval Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_CEOApproval',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='CEOEndorsement',
        widget=CalendarWidget(
            label="CEO Endorsement",
            show_hm=False,
            label_msgid='ProjectDatabase_label_CEOEndorsement',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='FirstDisbursement',
        widget=CalendarWidget(
            label="First Disbursement",
            show_hm=False,
            label_msgid='ProjectDatabase_label_FirstDisbursement',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='RevisedCompletionDate',
        dummy="Revised Completion Date",
        widget=CalendarWidget(
            label="Revised Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_RevisedCompletionDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='InitialCompletionDate',
        dummy="Initial Completion Date",
        widget=CalendarWidget(
            label="Initial Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_InitialCompletionDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='FinancialClosure',
        widget=CalendarWidget(
            label="Financial Closure",
            show_hm=False,
            label_msgid='ProjectDatabase_label_FinancialClosure',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='JointImplementation',
        widget=SelectionWidget(
            label="Joint Implementation",
            label_msgid='ProjectDatabase_label_JointImplementation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""YesOrNo""")
    ),

    StringField(
        name='GEFAgencyImplementation',
        dummy="Project.schema",
        widget=SelectionWidget(
            label="GEF Agency Implementation",
            label_msgid='ProjectDatabase_label_GEFAgencyImplementation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""AgencyImplementation""")
    ),

    StringField(
        name='LeadExecutingAgency',
        widget=StringWidget(
            label="Lead Executing Agency",
            label_msgid='ProjectDatabase_label_LeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='MidtermReview',
        widget=SelectionWidget(
            label="Mid-Term Review Planned",
            label_msgid='ProjectDatabase_label_MidtermReview',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ReviewEvaluation""")
    ),

    DateTimeField(
        name='PlannedDate',
        widget=CalendarWidget(
            label="Planned Date",
            label_msgid='ProjectDatabase_label_PlannedDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='Budget',
        widget=MoneyField._properties['widget'](
            label="Budget",
            label_msgid='ProjectDatabase_label_Budget',
            i18n_domain='ProjectDatabase',
        )
    ),

    TextField(
        name='RemarksOnFundSourceMTR',
        widget=TextAreaWidget(
            label="Remarks on Source of Funds for MTR/MTE",
            label_msgid='ProjectDatabase_label_RemarksOnFundSourceMTR',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='MTRActualCost',
        widget=MoneyField._properties['widget'](
            label="Actual Cost MTR/MTE",
            label_msgid='ProjectDatabase_label_MTRActualCost',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='TerminalEvaluationPlanned',
        widget=CalendarWidget(
            label="Terminal Evaluation Planned",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalEvaluationPlanned',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='TerminalEvaluationBudget',
        widget=MoneyField._properties['widget'](
            label="Terminal Evaluation Budget",
            label_msgid='ProjectDatabase_label_TerminalEvaluationBudget',
            i18n_domain='ProjectDatabase',
        )
    ),

    TextField(
        name='RemarksOnSourceOfFundsTE',
        widget=TextAreaWidget(
            label="Remarks on the Source of Funds for TE",
            label_msgid='ProjectDatabase_label_RemarksOnSourceOfFundsTE',
            i18n_domain='ProjectDatabase',
        )
    ),

    MoneyField(
        name='TEActualCost',
        widget=MoneyField._properties['widget'](
            label="Actual Cost TE",
            label_msgid='ProjectDatabase_label_TEActualCost',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='MidtermReviewReportDate',
        widget=CalendarWidget(
            label="Midterm Review Report Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MidtermReviewReportDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='MidtermReviewEvaluatorName',
        widget=StringWidget(
            label="Midterm Review Evaluator Name",
            label_msgid='ProjectDatabase_label_MidtermReviewEvaluatorName',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='MidtermReviewPlannedDate',
        widget=CalendarWidget(
            label="Midterm Review Planned Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MidtermReviewPlannedDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='MidtermReviewActualDate',
        widget=CalendarWidget(
            label="Midterm Review Actual Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MidtermReviewActualDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='TerminalEvaluationReportDate',
        widget=CalendarWidget(
            label="Terminal Evaluation Report Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalEvaluationReportDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='TerminalReportEvaluatorName',
        widget=StringWidget(
            label="Terminal Report Evaluator Name",
            label_msgid='ProjectDatabase_label_TerminalReportEvaluatorName',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='TerminalReportPlannedEvaluationDate',
        widget=CalendarWidget(
            label="Terminal Report Planned Evaluation Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalReportPlannedEvaluationDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='TerminalReportActualEvaluationDate',
        widget=CalendarWidget(
            label="Terminal Report Actual Evaluation Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalReportActualEvaluationDate',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MonitoringAndEvaluation_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MonitoringAndEvaluation(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Monitoring and Evaluation'

    meta_type = 'MonitoringAndEvaluation'
    portal_type = 'MonitoringAndEvaluation'
    allowed_content_types = ['EvaluationMilestoneFolder', 'RTSFolder', 'EvaluatorsInformationFolder']
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'MonitoringAndEvaluation.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Monitoring and Evaluation"
    typeDescMsgId = 'description_edit_monitoringandevaluation'


    actions =  (


       {'action': "string:${object_url}/project_ratings_disconnect_view",
        'category': "object_tabs",
        'id': 'project_ratings_disconnect_view',
        'name': 'Project Ratings Disconnect',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:0'
       },


       {'action': "string:${object_url}/evaluation_process_progress",
        'category': "object_tabs",
        'id': 'evaluation_process_progress_view',
        'name': 'Evaluation Process Progress',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:0'
       },


    )

    _at_rename_after_creation = True

    schema = MonitoringAndEvaluation_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container):
        """
        """
        me = self
        if 'evaluation_milestone_folder' not in me.objectIds():
            me.invokeFactory('EvaluationMilestoneFolder', 'evaluation_milestone_folder', title='Evaluation Milestones')
            #me['evaluation_milestone_folder'].setTitle('Evaluation Milestones')
        if 'rtsfolder' not in me.objectIds():
            me.invokeFactory('RTSFolder', 'rtsfolder')
            me['rtsfolder'].setTitle('Rating Tracking Systems')
        if 'evaluators_information_folder' not in me.objectIds():
            me.invokeFactory('EvaluatorsInformationFolder', 'evaluators_information_folder')
            me['evaluators_information_folder'].setTitle('Evaluators Information')
        BaseFolder.manage_afterAdd(self, item, container)

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """
        """
        return self.getProject().Title()


registerType(MonitoringAndEvaluation, PROJECTNAME)
# end of class MonitoringAndEvaluation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



