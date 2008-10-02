# -*- coding: utf-8 -*-
#
# File: EvaluationMilestone.py
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
        name='EvaluationTypeMilestone',
        widget=SelectionWidget(
            label="Evaluation Type Milestone",
            label_msgid='ProjectDatabase_label_EvaluationTypeMilestone',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""EvaluationTypeMilestone"""),
    ),
    StringField(
        name='MEMilestoneName',
        widget=SelectionWidget(
            label="M&E Milestone Name",
            label_msgid='ProjectDatabase_label_MEMilestoneName',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""MEMilestoneName"""),
    ),
    DateTimeField(
        name='PlannedDate',
        widget=DateTimeField._properties['widget'](
            label="Planned Date",
            description="Planned date for the particular milestone",
            show_hm=False,
            label_msgid='ProjectDatabase_label_PlannedDate',
            description_msgid='ProjectDatabase_help_PlannedDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DateTimeField(
        name='ActualDate',
        widget=DateTimeField._properties['widget'](
            label="Actual Date",
            description="Actual date for the particular milestone",
            show_hm=False,
            label_msgid='ProjectDatabase_label_ActualDate',
            description_msgid='ProjectDatabase_help_ActualDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    TextField(
        name='Remarks',
        widget=TextAreaWidget(
            description="To track changes related to evaluation planning",
            label='Remarks',
            label_msgid='ProjectDatabase_label_Remarks',
            description_msgid='ProjectDatabase_help_Remarks',
            i18n_domain='ProjectDatabase',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EvaluationMilestone_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class EvaluationMilestone(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IEvaluationMilestone)

    meta_type = 'EvaluationMilestone'
    _at_rename_after_creation = True

    schema = EvaluationMilestone_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(EvaluationMilestone, PROJECTNAME)
# end of class EvaluationMilestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



