# -*- coding: utf-8 -*-
#
# File: RatingTrackingSystem.py
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
        name='ProjectInceptionRiskRating',
        widget=SelectionWidget(
            label="Project Risk Rating at Inception",
            label_msgid='ProjectDatabase_label_ProjectInceptionRiskRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""InceptionRiskRating""")
    ),

    StringField(
        name='ProjectRiskRatingForEachPIR',
        widget=SelectionWidget(
            label="Project Risk Rating for each PIR",
            label_msgid='ProjectDatabase_label_ProjectRiskRatingForEachPIR',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""InceptionRiskRating""")
    ),

    TextField(
        name='Remarks',
        widget=TextAreaWidget(
            description="Refers to significant changes within specific budget lines as compared to the originally approved budget",
            label='Remarks',
            label_msgid='ProjectDatabase_label_Remarks',
            description_msgid='ProjectDatabase_help_Remarks',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='MTEMTRRating',
        widget=SelectionWidget(
            label="MTE/MTR Rating",
            label_msgid='ProjectDatabase_label_MTEMTRRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='Assessment',
        widget=SelectionWidget(
            label="Assessment (if applicable)",
            label_msgid='ProjectDatabase_label_Assessment',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Assessment""")
    ),

    StringField(
        name='EOURatingElements',
        widget=SelectionWidget(
            label="EOU Rating Elements",
            label_msgid='ProjectDatabase_label_EOURatingElements',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""EORatingElements""")
    ),

    StringField(
        name='EOUAssessment',
        widget=SelectionWidget(
            label="EOU Assessment",
            label_msgid='ProjectDatabase_label_EOUAssessment',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Assessment""")
    ),

    StringField(
        name='EOURating',
        widget=SelectionWidget(
            label="EOU Rating",
            label_msgid='ProjectDatabase_label_EOURating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RatingTrackingSystem_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RatingTrackingSystem(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Rating Tracking System'

    meta_type = 'RatingTrackingSystem'
    portal_type = 'RatingTrackingSystem'
    allowed_content_types = ['OtherProjectRatingsFolder', 'PIRRatingFolder']
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'RatingTrackingSystem.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Rating Tracking System"
    typeDescMsgId = 'description_edit_ratingtrackingsystem'

    _at_rename_after_creation = True

    schema = RatingTrackingSystem_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getPIRRatingCategory')
    def getPIRRatingCategory(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('PIRRatingCategory')
        return vocab.getDisplayList(self)

    security.declarePublic('getRatingList')
    def getRatingList(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('Rating')
        return vocab.getDisplayList(self)

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container):
        """
        """

        if 'pir_ratings' not in self.objectIds():
            self.invokeFactory('PIRRatingFolder', 'pir_ratings')
            self['pir_ratings'].setTitle('PIR Ratings')
        if 'other_project_ratings_folder' not in self.objectIds():
            self.invokeFactory('OtherProjectRatingsFolder', 'other_project_ratings_folder')
            self['other_project_ratings_folder'].setTitle('Other Project Ratings')
        BaseFolder.manage_afterAdd(self, item, container)


registerType(RatingTrackingSystem, PROJECTNAME)
# end of class RatingTrackingSystem

##code-section module-footer #fill in your manual code here
##/code-section module-footer



