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
##/code-section module-header

schema = Schema((

    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label='Projecttitle',
            label_msgid='ProjectDatabase_label_ProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='IMISNumber',
        widget=StringField._properties['widget'](
            label="IMIS Number",
            label_msgid='ProjectDatabase_label_IMISNumber',
            i18n_domain='ProjectDatabase',
        ),
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
        relationship="MandE_TaskManager",
    ),
    ReferenceField(
        name='FundManagementOfficer',
        widget=ReferenceBrowserWidget(
            label="Fund Manager Officer",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_FundManagementOfficer',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="MandE_fundmanagerofficer",
    ),
    DateTimeField(
        name='CEOApproval',
        widget=DateTimeField._properties['widget'](
            label="CEO Approval Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_CEOApproval',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='CEOEndorsement',
        widget=DateTimeField._properties['widget'](
            label="CEO Endorsement",
            show_hm=False,
            label_msgid='ProjectDatabase_label_CEOEndorsement',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='FirstDisbursement',
        widget=DateTimeField._properties['widget'](
            label="First Disbursement",
            show_hm=False,
            label_msgid='ProjectDatabase_label_FirstDisbursement',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='RevisedCompletionDate',
        widget=DateTimeField._properties['widget'](
            label="Revised Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_RevisedCompletionDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='InitialCompletionDate',
        widget=DateTimeField._properties['widget'](
            label="Initial Completion Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_InitialCompletionDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='FinancialClosure',
        widget=DateTimeField._properties['widget'](
            label="Financial Closure",
            show_hm=False,
            label_msgid='ProjectDatabase_label_FinancialClosure',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='LeadExecutingAgency',
        widget=StringField._properties['widget'](
            label="Lead Executing Agency",
            label_msgid='ProjectDatabase_label_LeadExecutingAgency',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='MidtermReview',
        widget=SelectionWidget(
            label="Mid-Term Review Planned",
            label_msgid='ProjectDatabase_label_MidtermReview',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ReviewEvaluation"""),
    ),
    DataGridField(
        name='PlannedDate',
        widget=DataGridField._properties['widget'](
            label="Planned Date",
            columns={'planned_date':CalendarColumn("Planned Date"),},
            label_msgid='ProjectDatabase_label_PlannedDate',
            i18n_domain='ProjectDatabase',
        ),
        columns=('planned_date',),
    ),
    MoneyField(
        name='Budget',
        widget=MoneyField._properties['widget'](
            label="Budget",
            label_msgid='ProjectDatabase_label_Budget',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='RemarksOnFundSourceMTR',
        widget=TextAreaWidget(
            label="Remarks on Source of Funds for MTR/MTE",
            label_msgid='ProjectDatabase_label_RemarksOnFundSourceMTR',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='MTRActualCost',
        widget=MoneyField._properties['widget'](
            label="Actual Cost MTR/MTE",
            label_msgid='ProjectDatabase_label_MTRActualCost',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='TerminalEvaluationPlanned',
        widget=DateTimeField._properties['widget'](
            label="Terminal Evaluation Planned",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalEvaluationPlanned',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='TerminalEvaluationBudget',
        widget=MoneyField._properties['widget'](
            label="Terminal Evaluation Budget",
            label_msgid='ProjectDatabase_label_TerminalEvaluationBudget',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='RemarksOnSourceOfFundsTE',
        widget=TextAreaWidget(
            label="Remarks on the Source of Funds for TE",
            label_msgid='ProjectDatabase_label_RemarksOnSourceOfFundsTE',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='TEActualCost',
        widget=MoneyField._properties['widget'](
            label="Actual Cost TE",
            label_msgid='ProjectDatabase_label_TEActualCost',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='MidtermReviewReportDate',
        widget=CalendarWidget(
            label="Midterm Review Report Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MidtermReviewReportDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ReferenceField(
        name='MidtermReviewEvaluatorName',
        widget=ReferenceBrowserWidget(
            label="Midterm Review Evaluator Name",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_MidtermReviewEvaluatorName',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="MandE_MTREvaluator",
    ),
    DateTimeField(
        name='MidtermReviewPlannedDate',
        widget=CalendarWidget(
            label="Midterm Review Planned Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MidtermReviewPlannedDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='MidtermReviewActualDate',
        widget=CalendarWidget(
            label="Midterm Review Actual Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MidtermReviewActualDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='TerminalEvaluationReportDate',
        widget=CalendarWidget(
            label="Terminal Evaluation Report Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalEvaluationReportDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ReferenceField(
        name='TerminalReportEvaluatorName',
        widget=ReferenceBrowserWidget(
            label="Terminal Report Evaluator Name",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_TerminalReportEvaluatorName',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="MandE_TEEvaluator",
    ),
    DateTimeField(
        name='TerminalReportPlannedEvaluationDate',
        widget=CalendarWidget(
            label="Terminal Report Planned Evaluation Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalReportPlannedEvaluationDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='TerminalReportActualEvaluationDate',
        widget=CalendarWidget(
            label="Terminal Report Actual Evaluation Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_TerminalReportActualEvaluationDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='EvaluationMilestones',
        widget=DataGridField._properties['widget'](
            columns={'evaluation_type_milestone':SelectColumn("Evaluation Type Milestone", vocabulary="getEvaluationTypeMilestoneVocabulary"),'memilestone_name':SelectColumn("ME Milestone Name", vocabulary="getMEMilestoneNameVocabulary"), 'planned_date':CalendarColumn("Planned Date"), 'actual_date':CalendarColumn("Actual Date"), 'remarks':Column("Remarks")},
            label='Evaluationmilestones',
            label_msgid='ProjectDatabase_label_EvaluationMilestones',
            i18n_domain='ProjectDatabase',
        ),
        columns=('evaluation_type_milestone', 'memilestone_name','planned_date','actual_date','remarks'),
    ),
    MoneyField(
        name='TEEstimatedCost',
        widget=MoneyField._properties['widget'](
            label="Cost Estimate for the TE",
            label_msgid='ProjectDatabase_label_TEEstimatedCost',
            i18n_domain='ProjectDatabase',
        ),
    ),
    MoneyField(
        name='MTREstimatedCost',
        widget=MoneyField._properties['widget'](
            label="Cost Estimate for the MTR/MTE",
            label_msgid='ProjectDatabase_label_MTREstimatedCost',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='EvaluationActualEstimateDifference',
        widget=ComputedField._properties['widget'](
            label='Evaluationactualestimatedifference',
            label_msgid='ProjectDatabase_label_EvaluationActualEstimateDifference',
            i18n_domain='ProjectDatabase',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MonitoringAndEvaluation_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
MonitoringAndEvaluation_schema['ProjectTitle'].widget.label = "Project Title"
title_field = MonitoringAndEvaluation_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
MonitoringAndEvaluation_schema['Budget'].widget.size = 15
MonitoringAndEvaluation_schema['MTRActualCost'].widget.size = 15
MonitoringAndEvaluation_schema['TerminalEvaluationBudget'].widget.size = 15
MonitoringAndEvaluation_schema['TEActualCost'].widget.size = 15

MonitoringAndEvaluation_schema['CurrentTaskManager'].widget.startup_directory = '/contacts'
MonitoringAndEvaluation_schema['FundManagementOfficer'].widget.startup_directory = '/contacts'
MonitoringAndEvaluation_schema['MidtermReviewEvaluatorName'].widget.startup_directory = '/contacts'
MonitoringAndEvaluation_schema['TerminalReportEvaluatorName'].widget.startup_directory = '/contacts'
##/code-section after-schema

class MonitoringAndEvaluation(BaseFolder, BrowserDefaultMixin):
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
        return self.getAProject().Title()

    security.declarePublic('getEvaluationTypeMilestoneVocabulary')
    def getEvaluationTypeMilestoneVocabulary(self):
        """
        """
        atvm = self.portal_vocabularies
        # vocab = atvm.getVocabularyByName('EvaluationMilestones')
        vocab = atvm.getVocabularyByName('EvaluationTypeMilestone')
        return vocab.getDisplayList(self)

    security.declarePublic('getMEMilestoneNameVocabulary')
    def getMEMilestoneNameVocabulary(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('MEMilestoneName')
        return vocab.getDisplayList(self)

    security.declarePublic('getEvaluationActualEstimateDifference')
    def getEvaluationActualEstimateDifference(self):
        """
        calculate the difference between estimated and actual cost
        """
        # import pdb; pdb.set_trace()
        budget = self.getBudget()
        teBudget = self.getTerminalEvaluationBudget()
        mtrEstimate = self.getMTREstimatedCost()
        teEstimate = self.getTEEstimatedCost()
        if (budget is not None) and \
                (teBudget is not None) and \
                (mtrEstimate is not None) and  \
                (teEstimate is not None):
            budgetCost = budget + teBudget
            estimatedCost = mtrEstimate + teEstimate
            # actualCost = getTEActualCost() + getMTRActualCost()
            # return estimatedCost = actualCost
            return budgetCost - estimatedCost
        return 0

    # Manually created methods

    def getIMISNumber(self):
        """
        """
        try:
            if self.IMISNumber == '':
                fmis = self.getAProject()['fmi_folder'].contentValues()
                if fmis:
                    return fmis[len(fmis)-1]['IMISNumber']
                else:
                    return ''
        except AttributeError:
            return ''
        except IndexError:
            return ''

    security.declarePublic("getCurrentTaskManager")
    def getCurrentTaskManager(self):
        """
        """
        if not self['CurrentTaskManager']:
            return self.getAProject().getCurrentTaskManager()
        return self['CurrentTaskManager']

    security.declarePublic("getFundManagementOfficer")
    def getFundManagementOfficer(self):
        """
        """
        if not self['FundManagementOfficer']:
            try:
                fmis = self.getAProject()['fmi_folder'].contentValues()
                return fmis[len(fmis)-1]['FundManagementOfficer']
            except AttributeError:
                return ''
            except IndexError:
                return ''

        return self['FundManagementOfficer']

    security.declarePublic("getCEOApproval")
    def getCEOApproval(self):
        """
        """
        if not self.getField('CEOApproval'):
            milestones = self.getAProject()['milestonesfolder'].contentValues()
            if milestones:
                approval = milestones[len(milestones)-1]['ApprovalInitiationAndClosure']
                if approval:
                    for appr in approval:
                        if appr['approval_initiation_closure'] == 'CEO approval (PDFB or MSP or EEA and now PDFA and PIF)':
                            return appr['actual_date']
        return self.getField('CEOApproval')

    security.declarePublic("getCEOEndorsement")
    def getCEOEndorsement(self):
        """
        """
        if not self.getField('CEOEndorsement'):
            milestones = self.getAProject()['milestonesfolder'].contentValues()
            if milestones:
                approval = milestones[len(milestones)-1]['ApprovalInitiationAndClosure']
                if approval:
                    for appr in approval:
                        if appr['approval_initiation_closure'] == 'CEO endorsement (for FSP)':
                            return appr['actual_date']
        return self.getField('CEOEndorsement')

    def getFirstDisbursement(self):
        """
        """
        if not self.getField('FirstDisbursement'):
            milestones = self.getAProject()['milestonesfolder'].contentValues()
            if milestones:
                approval = milestones[len(milestones)-1]['ApprovalInitiationAndClosure']
                if approval:
                    for appr in approval:
                        if appr['approval_initiation_closure'] == 'First disbursement (date)':
                            return appr['actual_date']
        return self.getField('FirstDisbursement')

    security.declarePublic('getRevisedCompletionDate')
    def getRevisedCompletionDate(self):
        """
        """
        if not self.getField('RevisedCompletionDate'):
            fmis = self.getAProject()['fmi_folder'].contentValues()
            if fmis:
                return fmis[len(fmis)-1]['RevisedCompletionDate']
        return self.getField('RevisedCompletionDate')

    security.declarePublic('getInitialCompletionDate')
    def getInitialCompletionDate(self):
        """
        """
        if not self.getField('InitialCompletionDate'):
            milestones = self.getAProject()['milestonesfolder'].contentValues()
            if milestones:
                approval = milestones[len(milestones)-1]['ApprovalInitiationAndClosure']
                if approval:
                    for appr in approval:
                        if appr['approval_initiation_closure'] == 'Project completion (date of Completion Revision) ':
                            return appr['actual_date']
        return self.getField('InitialCompletionDate')

    def getFinancialClosure(self):
        """
        """
        if not self.getField('FinancialClosure'):
            milestones = self.getAProject()['milestonesfolder'].contentValues()
            if milestones:
                approval = milestones[len(milestones)-1]['ApprovalInitiationAndClosure']
                if approval:
                    for appr in approval:
                        if appr['approval_initiation_closure'] == 'Financial closure':
                            return appr['actual_date']
        return self.getField('FinancialClosure')



registerType(MonitoringAndEvaluation, PROJECTNAME)
# end of class MonitoringAndEvaluation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



