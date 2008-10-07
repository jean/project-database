# -*- coding: utf-8 -*-
#
# File: EvaluationMilestoneFolder.py
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

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EvaluationMilestoneFolder_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class EvaluationMilestoneFolder(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IEvaluationMilestoneFolder)

    meta_type = 'EvaluationMilestoneFolder'
    _at_rename_after_creation = True

    schema = EvaluationMilestoneFolder_schema

    ##code-section class-header #fill in your manual code here
    actions = ({  'action':"string:${object_url}/edit",
                            'category':"object",
                            'id':'edit',
                            'name':'edit',
                            'permissions':('Modify portal content'),
                            'condition':'python:0',
                        },)
    ##/code-section class-header

    # Methods


registerType(EvaluationMilestoneFolder, PROJECTNAME)
# end of class EvaluationMilestoneFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer


