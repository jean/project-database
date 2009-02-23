# -*- coding: utf-8 -*-
#
# File: PIRRating.py
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
from Products.ProjectDatabase.utils import getYearVocabulary
from DateTime import DateTime
##/code-section module-header

schema = Schema((

    StringField(
        name='FiscalYear',
        widget=SelectionWidget(
            label="Fiscal Year",
            label_msgid='ProjectDatabase_label_FiscalYear',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary="getFiscalYearVocabulary",
    ),
    StringField(
        name='DevelopmentObjective',
        default="No Selection",
        widget=SelectionWidget(
            label="Development Objective",
            label_msgid='ProjectDatabase_label_DevelopmentObjective',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='ImplementationProgress',
        default="No Selection",
        widget=SelectionWidget(
            label="Implementation Progress",
            label_msgid='ProjectDatabase_label_ImplementationProgress',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='MonitoringAndEvaluation',
        default="No Selection",
        widget=SelectionWidget(
            label="Monitoring and Evaluation",
            label_msgid='ProjectDatabase_label_MonitoringAndEvaluation',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Rating"""),
    ),
    StringField(
        name='ProjectRisk',
        default="No Selection",
        widget=SelectionWidget(
            label="Project Risk",
            label_msgid='ProjectDatabase_label_ProjectRisk',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""RiskLevel"""),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PIRRating_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
PIRRating_schema['FiscalYear'].default = str(DateTime().year())
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

    # Manually created methods

    def getFiscalYearVocabulary(self):
        return getYearVocabulary()



registerType(PIRRating, PROJECTNAME)
# end of class PIRRating

##code-section module-footer #fill in your manual code here
##/code-section module-footer



