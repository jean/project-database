# -*- coding: utf-8 -*-
#
# File: DocumentLinks.py
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
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

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
        widget=StringField._properties['widget'](
            label="Project Document",
            label_msgid='ProjectDatabase_label_ProjectDocument',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='MidtermEvaluation',
        widget=StringField._properties['widget'](
            label="Midterm Evaluation",
            label_msgid='ProjectDatabase_label_MidtermEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='TerminalEvaluation',
        widget=StringField._properties['widget'](
            label="Terminal Evaluation",
            label_msgid='ProjectDatabase_label_TerminalEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='ExecutiveSummary',
        widget=StringField._properties['widget'](
            label="Executive Summary",
            label_msgid='ProjectDatabase_label_ExecutiveSummary',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='GEFReviewSheets',
        widget=StringField._properties['widget'](
            label="GEF Review Sheets",
            label_msgid='ProjectDatabase_label_GEFReviewSheets',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='ProjectBrief',
        widget=StringField._properties['widget'](
            label="Project Brief",
            label_msgid='ProjectDatabase_label_ProjectBrief',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='AnnexesToProjectBrief',
        widget=StringField._properties['widget'](
            label="Annexes To Project Brief",
            label_msgid='ProjectDatabase_label_AnnexesToProjectBrief',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='CEOEndorsementLetter',
        widget=StringField._properties['widget'](
            label="CEO Endorsement Letter",
            label_msgid='ProjectDatabase_label_CEOEndorsementLetter',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='GEFFocalPointEndorsementLetters',
        widget=StringField._properties['widget'](
            label="GEF Focal Point Endrosement Letters",
            label_msgid='ProjectDatabase_label_GEFFocalPointEndorsementLetters',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='UNEPProjectDocument',
        widget=StringField._properties['widget'](
            label="UNEP Project Document",
            label_msgid='ProjectDatabase_label_UNEPProjectDocument',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='UNEPProjectAnnexes',
        widget=StringField._properties['widget'](
            label="UNEP Project Annexes",
            label_msgid='ProjectDatabase_label_UNEPProjectAnnexes',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='FinancialReport1',
        widget=StringField._properties['widget'](
            label="Financial Report 1st Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport1',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='FinancialReport2',
        widget=StringField._properties['widget'](
            label="Financial Report 2nd Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport2',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='FinancialReport3',
        widget=StringField._properties['widget'](
            label="Financial Report 3rd Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport3',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='FinancialReport4',
        widget=StringField._properties['widget'](
            label="Financial Report 4th Quarter",
            label_msgid='ProjectDatabase_label_FinancialReport4',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='AuditedCertificateOfAccounts',
        widget=StringField._properties['widget'](
            label="Audited Certificate of Accounts",
            label_msgid='ProjectDatabase_label_AuditedCertificateOfAccounts',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='SubProjectDocuments',
        widget=StringField._properties['widget'](
            label="Sub-project Documents",
            label_msgid='ProjectDatabase_label_SubProjectDocuments',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='MOU',
        widget=StringField._properties['widget'](
            label="MOU",
            label_msgid='ProjectDatabase_label_MOU',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='ProjectRevisions',
        widget=StringField._properties['widget'](
            label="Project Revisions",
            label_msgid='ProjectDatabase_label_ProjectRevisions',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='NewTablesForProjectRevisions',
        widget=StringField._properties['widget'](
            label="New Tables for Project Revisions",
            label_msgid='ProjectDatabase_label_NewTablesForProjectRevisions',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='InventoryOfNonExpendableEquipment',
        widget=StringField._properties['widget'](
            label="Inventory of Non-expendable Equipment",
            label_msgid='ProjectDatabase_label_InventoryOfNonExpendableEquipment',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='PIR',
        widget=StringField._properties['widget'](
            label="PIR",
            label_msgid='ProjectDatabase_label_PIR',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='ProgressReport',
        widget=StringField._properties['widget'](
            label="Progress Reports",
            label_msgid='ProjectDatabase_label_ProgressReport',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='MidtermReview',
        widget=StringField._properties['widget'](
            label="Mid term Reviews/Evaluations",
            label_msgid='ProjectDatabase_label_MidtermReview',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='RecommendationsFollowUp',
        widget=StringField._properties['widget'](
            label="Recommendations Follow-up",
            label_msgid='ProjectDatabase_label_RecommendationsFollowUp',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='SteeringCommitteeMeetingMinutes',
        widget=StringField._properties['widget'](
            label="Steering Committee Meeting Minutes",
            label_msgid='ProjectDatabase_label_SteeringCommitteeMeetingMinutes',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='MissionReports',
        widget=StringField._properties['widget'](
            label="Mission Reports",
            label_msgid='ProjectDatabase_label_MissionReports',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='SubstantiveReport',
        widget=StringField._properties['widget'](
            label="Substantive Reports",
            label_msgid='ProjectDatabase_label_SubstantiveReport',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='SubstantivePublication',
        widget=StringField._properties['widget'](
            label="Substantive Publications",
            label_msgid='ProjectDatabase_label_SubstantivePublication',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
    StringField(
        name='PDFDocument',
        widget=StringField._properties['widget'](
            label="PDF Financial Information Documents",
            label_msgid='ProjectDatabase_label_PDFDocument',
            i18n_domain='ProjectDatabase',
        ),
        schemata="DocumentLinks",
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

DocumentLinks_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class DocumentLinks(BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IDocumentLinks)

    meta_type = 'DocumentLinks'
    _at_rename_after_creation = True

    schema = DocumentLinks_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


# end of class DocumentLinks

##code-section module-footer #fill in your manual code here
##/code-section module-footer



