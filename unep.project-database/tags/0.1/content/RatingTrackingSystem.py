# -*- coding: utf-8 -*-
#
# File: RatingTrackingSystem.py
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
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn, CalendarColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='ProjectInceptionRiskRating',
        widget=SelectionWidget(
            label="Project Risk Rating at Inception",
            label_msgid='ProjectDatabase_label_ProjectInceptionRiskRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""InceptionRiskRating"""),
    ),
    TextField(
        name='Remarks',
        widget=TextAreaWidget(
            description="Refers to significant changes within specific budget lines as compared to the originally approved budget",
            label='Remarks',
            label_msgid='ProjectDatabase_label_Remarks',
            description_msgid='ProjectDatabase_help_Remarks',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='Assessment',
        widget=SelectionWidget(
            label="Assessment (if applicable)",
            label_msgid='ProjectDatabase_label_Assessment',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Assessment"""),
    ),
    StringField(
        name='EOUAssessment',
        widget=SelectionWidget(
            label="EOU Assessment",
            label_msgid='ProjectDatabase_label_EOUAssessment',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Assessment"""),
    ),
    DataGridField(
        name='PIRRating',
        widget=DataGridField._properties['widget'](
            columns={'fiscal_year':Column("Fiscal Year"), 'achievement_of_results':SelectColumn("Achievement of Results", vocabulary="getRatingList"), "implementation_progress":SelectColumn("Implementation Progress", vocabulary="getRatingList"),'monitoring_and_evaluation':SelectColumn("Monitoring and Evalutation", vocabulary="getRatingList"),'risk':SelectColumn("Risk", vocabulary="getInceptionRiskRatingVocabulary"),},
            label="PIR Rating",
            label_msgid='ProjectDatabase_label_PIRRating',
            i18n_domain='ProjectDatabase',
        ),
        columns=('fiscal_year', 'achievement_of_results','implementation_progress','monitoring_and_evaluation','risk'),
    ),
    DataGridField(
        name='MTERating',
        widget=DataGridField._properties['widget'](
            label="Midterm Evaluation Rating",
            columns={'evaluation_elements':SelectColumn("Evaluation Elements", vocabulary="getEORatingElements"), 'evaluator_rating':SelectColumn("Evaluator Rating", vocabulary="getRatingList"), 'eou_rating':SelectColumn("EOU Rating", vocabulary="getRatingList")},
            label_msgid='ProjectDatabase_label_MTERating',
            i18n_domain='ProjectDatabase',
        ),
        columns=('evaluation_elements', 'evaluator_rating', 'eou_rating',),
    ),
    DataGridField(
        name='MTRRating',
        widget=DataGridField._properties['widget'](
            label="Midterm Review Rating",
            columns={'review_elements':SelectColumn("Review Elements", vocabulary="getEORatingElements"), 'mtr_rating':SelectColumn("MTR Rating", vocabulary="getRatingList")},
            label_msgid='ProjectDatabase_label_MTRRating',
            i18n_domain='ProjectDatabase',
        ),
        columns=('review_elements', 'mtr_rating',),
    ),
    DataGridField(
        name='TERating',
        widget=DataGridField._properties['widget'](
            label="Terminal Evaluation Rating",
            columns={'evaluation_elements':SelectColumn("Evaluation Elements", vocabulary="getEORatingElements"), 'evaluator_rating':SelectColumn("Evaluator Rating", vocabulary="getRatingList"), 'eou_rating':SelectColumn("EOU Rating", vocabulary="getRatingList"), 'eo_rating':SelectColumn("EO Rating", vocabulary="getRatingList")},
            label_msgid='ProjectDatabase_label_TERating',
            i18n_domain='ProjectDatabase',
        ),
        columns=('evaluation_elements', 'evaluator_rating', 'eou_rating', 'eo_rating',),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RatingTrackingSystem_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RatingTrackingSystem(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IRatingTrackingSystem)

    meta_type = 'RatingTrackingSystem'
    _at_rename_after_creation = True

    schema = RatingTrackingSystem_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # security.declarePublic('getPIRRatingCategory')
    # def getPIRRatingCategory(self):
    #     """
    #     """
    #     atvm = getToolByName(self, 'portal_vocabularies')
    #     vocab = atvm.getVocabularyByName('PIRRatingCategory')
    #     return vocab.getDisplayList(self)

    security.declarePublic('getRatingList')
    def getRatingList(self):
        """
        """
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('Rating')
        return vocab.getDisplayList(self)

    security.declarePublic('getInceptionRiskRatingVocabulary')
    def getInceptionRiskRatingVocabulary(self):
        """
        """
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('InceptionRiskRating')
        return vocab.getDisplayList(self)

    # Manually created methods

    security.declarePublic('getEORatingElements')
    def getEORatingElements(self):
        """
        """
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('EORatingElements')
        return vocab.getDisplayList(self)



registerType(RatingTrackingSystem, PROJECTNAME)
# end of class RatingTrackingSystem

##code-section module-footer #fill in your manual code here
##/code-section module-footer



