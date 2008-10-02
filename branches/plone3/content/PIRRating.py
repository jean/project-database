# -*- coding: utf-8 -*-
#
# File: PIRRating.py
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
        name='FiscalYear',
        widget=StringField._properties['widget'](
            label="Fiscal Year",
            label_msgid='ProjectDatabase_label_FiscalYear',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='AchievementOfResults',
        widget=SelectionWidget(
            label="Achievement of Results",
            label_msgid='ProjectDatabase_label_AchievementOfResults',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='ImplementationProgress',
        widget=SelectionWidget(
            label="Implementation Progress",
            label_msgid='ProjectDatabase_label_ImplementationProgress',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='MonitoringAndEvaluation',
        widget=SelectionWidget(
            label="Monitoring and Evaluation",
            label_msgid='ProjectDatabase_label_MonitoringAndEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='Risk',
        widget=SelectionWidget(
            label='Risk',
            label_msgid='ProjectDatabase_label_Risk',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""InceptionRiskRating"""),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PIRRating_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PIRRating(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IPIRRating)

    meta_type = 'PIRRating'
    _at_rename_after_creation = True

    schema = PIRRating_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(PIRRating, PROJECTNAME)
# end of class PIRRating

##code-section module-footer #fill in your manual code here
##/code-section module-footer



