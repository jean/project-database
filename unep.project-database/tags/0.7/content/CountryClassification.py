# -*- coding: utf-8 -*-
#
# File: CountryClassification.py
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

    StringField(
        name='CountryName',
        widget=SelectionWidget(
            label="Country",
            label_msgid='ProjectDatabase_label_CountryName',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Country"""),
    ),
    LinesField(
        name='ConventionRatification',
        widget=MultiSelectionWidget(
            label="Convention Ratification",
            label_msgid='ProjectDatabase_label_ConventionRatification',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""ConventionRatification"""),
    ),
    LinesField(
        name='CountryGrouping',
        widget=MultiSelectionWidget(
            label="Country Grouping",
            label_msgid='ProjectDatabase_label_CountryGrouping',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""CountryGrouping"""),
    ),
    StringField(
        name='OtherGroup',
        widget=StringField._properties['widget'](
            label="Other Group",
            label_msgid='ProjectDatabase_label_OtherGroup',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='RiskRating',
        widget=SelectionWidget(
            label="Risk Rating",
            label_msgid='ProjectDatabase_label_RiskRating',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""RiskLevel"""),
    ),
    TextField(
        name='Remarks',
        widget=TextAreaWidget(
            label="Remarks",
            label_msgid='ProjectDatabase_label_Remarks',
            i18n_domain='ProjectDatabase',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CountryClassification_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CountryClassification(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ICountryClassification)

    meta_type = 'CountryClassification'
    _at_rename_after_creation = True

    schema = CountryClassification_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(CountryClassification, PROJECTNAME)
# end of class CountryClassification

##code-section module-footer #fill in your manual code here
##/code-section module-footer



