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

    DataGridField(
        name='PIRRating',
        widget=DataGridField._properties['widget'](
            columns={'pir_rating_category':SelectColumn('PIR Rating Category', vocabulary='getPIRRatingCategory'), 'rating':SelectColumn('Rating', vocabulary='getRatingList')},
            label='Pirrating',
            label_msgid='ProjectDatabase_label_PIRRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""PIRRatingCategory"""),
        columns=('pir_rating_category','rating')
    ),

    StringField(
        name='FiscalYear',
        widget=StringWidget(
            label="Fiscal Year",
            description="Eg FY06, where the FY refers to the date of the PIR",
            label_msgid='ProjectDatabase_label_FiscalYear',
            description_msgid='ProjectDatabase_help_FiscalYear',
            i18n_domain='ProjectDatabase',
        )
    ),

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
        name='ProjectAtRiskSelfRatings',
        widget=SelectionWidget(
            label="Project-at-risk self-ratings",
            label_msgid='ProjectDatabase_label_ProjectAtRiskSelfRatings',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""PARSelfRatings""")
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

    StringField(
        name='CostOverrunRiskRating',
        widget=SelectionWidget(
            label="Cost Overrun Risk Rating",
            label_msgid='ProjectDatabase_label_CostOverrunRiskRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""InceptionRiskRating""")
    ),

    StringField(
        name='RevisionNumber',
        widget=SelectionWidget(
            label="Revision Number",
            label_msgid='ProjectDatabase_label_RevisionNumber',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""RevisionNumber""")
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
        name='ConsultantMTEMTRRatingElements',
        widget=SelectionWidget(
            label="Consultant MTE/MTR Rating Elements",
            label_msgid='ProjectDatabase_label_ConsultantMTEMTRRatingElements',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ConsultantRatingElements""")
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
        name='ConsultantMTEMTRRiskRating',
        widget=SelectionWidget(
            label="Consultant MTE/ MTR Risk Rating",
            label_msgid='ProjectDatabase_label_ConsultantMTEMTRRiskRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""InceptionRiskRating""")
    ),

    StringField(
        name='ConsultantTERatingElements',
        widget=SelectionWidget(
            label="Consultant TE Rating Elements",
            label_msgid='ProjectDatabase_label_ConsultantTERatingElements',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ConsultantRatingElements""")
    ),

    StringField(
        name='TERating',
        widget=SelectionWidget(
            label="TE Rating",
            label_msgid='ProjectDatabase_label_TERating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating""")
    ),

    StringField(
        name='EORatingElements',
        widget=SelectionWidget(
            label="EO Rating Elements",
            label_msgid='ProjectDatabase_label_EORatingElements',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""EORatingElements""")
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

RatingTrackingSystem_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RatingTrackingSystem(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'RatingTrackingSystem'

    meta_type = 'RatingTrackingSystem'
    portal_type = 'RatingTrackingSystem'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'RatingTrackingSystem.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "RatingTrackingSystem"
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


registerType(RatingTrackingSystem, PROJECTNAME)
# end of class RatingTrackingSystem

##code-section module-footer #fill in your manual code here
##/code-section module-footer



