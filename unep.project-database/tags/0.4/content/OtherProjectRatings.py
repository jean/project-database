# -*- coding: utf-8 -*-
#
# File: OtherProjectRatings.py
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
##/code-section module-header

schema = Schema((

    DataGridField(
        name='MTERating',
        widget=DataGridField._properties['widget'](
            label="Midterm Evaluation Rating",
            columns={'evaluation_elements':SelectColumn("Evaluation Elements", vocabulary="getOtherProjectRatingElements"), 'evaluator_rating':SelectColumn("Evaluator Rating", vocabulary="getRatingList"), 'eou_rating':SelectColumn("EOU Rating", vocabulary="getRatingList")},
            label_msgid='ProjectDatabase_label_MTERating',
            i18n_domain='ProjectDatabase',
        ),
        columns=('evaluation_elements', 'evaluator_rating', 'eou_rating',),
    ),
    DataGridField(
        name='MTRRating',
        widget=DataGridField._properties['widget'](
            label="Midterm Review Rating",
            columns={'review_elements':SelectColumn("Review Elements", vocabulary="getOtherProjectRatingElements"), 'mtr_rating':SelectColumn("MTR Rating", vocabulary="getRatingList")},
            label_msgid='ProjectDatabase_label_MTRRating',
            i18n_domain='ProjectDatabase',
        ),
        columns=('review_elements', 'mtr_rating',),
    ),
    DataGridField(
        name='TERating',
        widget=DataGridField._properties['widget'](
            label="Terminal Evaluation Rating",
            columns={'evaluation_elements':SelectColumn("Evaluation Elements", vocabulary="getOtherProjectRatingElements"), 'evaluator_rating':SelectColumn("Evaluator Rating", vocabulary="getRatingList"), 'eou_rating':SelectColumn("EOU Rating", vocabulary="getRatingList"), 'eo_rating':SelectColumn("EO Rating", vocabulary="getRatingList")},
            label_msgid='ProjectDatabase_label_TERating',
            i18n_domain='ProjectDatabase',
        ),
        columns=('evaluation_elements', 'evaluator_rating', 'eou_rating', 'eo_rating',),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

OtherProjectRatings_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class OtherProjectRatings(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IOtherProjectRatings)

    meta_type = 'OtherProjectRatings'
    _at_rename_after_creation = True

    schema = OtherProjectRatings_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getOtherProjectRatingElements')
    def getOtherProjectRatingElements(self):
        """
        """
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('OtherRatings')
        return vocab.getDisplayList(self)


registerType(OtherProjectRatings, PROJECTNAME)
# end of class OtherProjectRatings

##code-section module-footer #fill in your manual code here
##/code-section module-footer



