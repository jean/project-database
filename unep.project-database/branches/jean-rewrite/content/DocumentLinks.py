# -*- coding: utf-8 -*-
#
# File: DocumentLinks.py
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

    StringField(
        name='ProjectDocument',
        widget=StringWidget(
            label="Project Document",
            label_msgid='ProjectDatabase_label_ProjectDocument',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='MidtermEvaluation',
        widget=StringWidget(
            label="Midterm Evaluation",
            label_msgid='ProjectDatabase_label_MidtermEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='TerminalEvaluation',
        widget=StringWidget(
            label="Terminal Evaluation",
            label_msgid='ProjectDatabase_label_TerminalEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='ExecutiveSummary',
        widget=StringWidget(
            label="Executive Summary",
            label_msgid='ProjectDatabase_label_ExecutiveSummary',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='GEFReviewSheets',
        widget=StringWidget(
            label="GEF Review Sheets",
            label_msgid='ProjectDatabase_label_GEFReviewSheets',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='ProjectBrief',
        widget=StringWidget(
            label="Project Brief",
            label_msgid='ProjectDatabase_label_ProjectBrief',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='AnnexesToProjectBrief',
        widget=StringWidget(
            label="Annexes To Project Brief",
            label_msgid='ProjectDatabase_label_AnnexesToProjectBrief',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='CEOEndorsementLetter',
        widget=StringWidget(
            label="CEO Endorsement Letter",
            label_msgid='ProjectDatabase_label_CEOEndorsementLetter',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='GEFFocalPointEndorsementLetters',
        widget=StringWidget(
            label="GEF Focal Point Endrosement Letters",
            label_msgid='ProjectDatabase_label_GEFFocalPointEndorsementLetters',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='UNEPProjectDocument',
        widget=StringWidget(
            label="UNEP Project Document",
            label_msgid='ProjectDatabase_label_UNEPProjectDocument',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='UNEPProjectAnnexes',
        widget=StringWidget(
            label="UNEP Project Annexes",
            label_msgid='ProjectDatabase_label_UNEPProjectAnnexes',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='FinancialReport1',
        widget=StringWidget(
            label="Financial Report 1st Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport1',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='FinancialReport2',
        widget=StringWidget(
            label="Financial Report 2nd Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport2',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='FinancialReport3',
        widget=StringWidget(
            label="Financial Report 3rd Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport3',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='FinancialReport4',
        widget=StringWidget(
            label="Financial Report 4th Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport4',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='AuditedCertificateOfAccounts',
        widget=StringWidget(
            label="Audited Certificate of Accounts",
            label_msgid='ProjectDatabase_label_AuditedCertificateOfAccounts',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='SubProjectDocuments',
        widget=StringWidget(
            label="Sub-project Documents",
            label_msgid='ProjectDatabase_label_SubProjectDocuments',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='MOU',
        widget=StringWidget(
            label="MOU",
            label_msgid='ProjectDatabase_label_MOU',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='ProjectRevisions',
        widget=StringWidget(
            label="Project Revisions",
            label_msgid='ProjectDatabase_label_ProjectRevisions',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='NewTablesForProjectRevisions',
        widget=StringWidget(
            label="New Tables for Project Revisions",
            label_msgid='ProjectDatabase_label_NewTablesForProjectRevisions',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='InventoryOfNonExpendableEquipment',
        widget=StringWidget(
            label="Inventory of Non-expendable Equipment",
            label_msgid='ProjectDatabase_label_InventoryOfNonExpendableEquipment',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='PIR',
        widget=StringWidget(
            label="PIR",
            label_msgid='ProjectDatabase_label_PIR',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='ProgressReport',
        widget=StringWidget(
            label="Progress Reports",
            label_msgid='ProjectDatabase_label_ProgressReport',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='MidtermReview',
        widget=StringWidget(
            label="Mid term Reviews/Evaluations",
            label_msgid='ProjectDatabase_label_MidtermReview',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='RecommendationsFollowUp',
        widget=StringWidget(
            label="Recommendations Follow-up",
            label_msgid='ProjectDatabase_label_RecommendationsFollowUp',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='SteeringCommitteeMeetingMinutes',
        widget=StringWidget(
            label="Steering Committee Meeting Minutes",
            label_msgid='ProjectDatabase_label_SteeringCommitteeMeetingMinutes',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='MissionReports',
        widget=StringWidget(
            label="Mission Reports",
            label_msgid='ProjectDatabase_label_MissionReports',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='SubstantiveReport',
        widget=StringWidget(
            label="Substantive Reports",
            label_msgid='ProjectDatabase_label_SubstantiveReport',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='SubstantivePublication',
        widget=StringWidget(
            label="Substantive Publications",
            label_msgid='ProjectDatabase_label_SubstantivePublication',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

    StringField(
        name='PDFDocument',
        widget=StringWidget(
            label="PDF Financial Information Documents",
            label_msgid='ProjectDatabase_label_PDFDocument',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

DocumentLinks_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class DocumentLinks:
    """
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'DocumentLinks'

    meta_type = 'DocumentLinks'
    portal_type = 'DocumentLinks'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'DocumentLinks.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "DocumentLinks"
    typeDescMsgId = 'description_edit_documentlinks'

    _at_rename_after_creation = True

    schema = DocumentLinks_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


# end of class DocumentLinks

##code-section module-footer #fill in your manual code here
##/code-section module-footer



