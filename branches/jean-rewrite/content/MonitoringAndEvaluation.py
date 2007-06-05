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

copied_fields = {}
copied_fields['CurrentTaskManager'] = Project.schema['CurrentTaskManager'].copy()
copied_fields['GEFAgencyImplementation'] = Project.schema['GEFAgencyImplementation'].copy()
schema = Schema((

    StringField(
        name='IMISNumber',
        widget=StringWidget(
            label='Imisnumber',
            label_msgid='ProjectDatabase_label_IMISNumber',
            i18n_domain='ProjectDatabase',
        )
    ),

    copied_fields['CurrentTaskManager'],
        ReferenceField(
        name='FundManagerOfficer',
        widget=ReferenceField._properties['widget'](
            label="Fund Manager Officer",
            label_msgid='ProjectDatabase_label_FundManagerOfficer',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        relationship="MandE_fundmanagerofficer"
    ),

    DateTimeField(
        name='CEOApproval',
        widget=CalendarWidget(
            label="CEO Approval Date",
            label_msgid='ProjectDatabase_label_CEOApproval',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='CEOEndorsement',
        widget=CalendarWidget(
            label="CEO Endorsement",
            label_msgid='ProjectDatabase_label_CEOEndorsement',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='FirstDisbursement',
        widget=CalendarWidget(
            label="First Disbursement",
            label_msgid='ProjectDatabase_label_FirstDisbursement',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='RevisedCompletionDate',
        widget=CalendarWidget(
            label='Revisedcompletiondate',
            label_msgid='ProjectDatabase_label_RevisedCompletionDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='InitialCompletionDate',
        widget=CalendarWidget(
            label='Initialcompletiondate',
            label_msgid='ProjectDatabase_label_InitialCompletionDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    DateTimeField(
        name='FinancialClosure',
        widget=CalendarWidget(
            label="Financial Closure",
            label_msgid='ProjectDatabase_label_FinancialClosure',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='JointEvaluation',
        widget=SelectionWidget(
            label="Joint Evaluation",
            label_msgid='ProjectDatabase_label_JointEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""YesOrNo""")
    ),

    copied_fields['GEFAgencyImplementation'],
        StringField(
        name='OtherAgency',
        widget=StringWidget(
            label="Other Agency",
            label_msgid='ProjectDatabase_label_OtherAgency',
            i18n_domain='ProjectDatabase',
        )
    ),

    ReferenceField(
        name='JointEvaluationAgencyContact',
        widget=ReferenceField._properties['widget'](
            label="Joint Evaluation Agency Contact",
            description="Name of evaluation officer in the other agency",
            label_msgid='ProjectDatabase_label_JointEvaluationAgencyContact',
            description_msgid='ProjectDatabase_help_JointEvaluationAgencyContact',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        relationship="EvaluationAgencyContact"
    ),

    StringField(
        name='MidtermReviewPlanned',
        widget=SelectionWidget(
            label="Mid-Term Review Planned",
            label_msgid='ProjectDatabase_label_MidtermReviewPlanned',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""YesOrNo""")
    ),

    MoneyField(
        name='MidtermReviewBudget',
        widget=MoneyField._properties['widget'](
            label="Mid-Term Review Budget",
            label_msgid='ProjectDatabase_label_MidtermReviewBudget',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='MidtermEvaluationPlanned',
        widget=SelectionWidget(
            label="Mid-Term Evaluation Planned",
            label_msgid='ProjectDatabase_label_MidtermEvaluationPlanned',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""YesOrNo""")
    ),

    MoneyField(
        name='MidtermEvaluationBudget',
        widget=MoneyField._properties['widget'](
            label="Mid-Term Evaluation Budget",
            label_msgid='ProjectDatabase_label_MidtermEvaluationBudget',
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
    allowed_content_types = ['EvaluationMilestone', 'RatingTrackingSystem', 'EvaluatorsInformation']
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
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/evaluation_process_progress",
        'category': "object_tabs",
        'id': 'evaluation_process_progress_view',
        'name': 'Evaluation Process Progress',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = MonitoringAndEvaluation_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(MonitoringAndEvaluation, PROJECTNAME)
# end of class MonitoringAndEvaluation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



