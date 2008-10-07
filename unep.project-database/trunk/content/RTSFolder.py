# -*- coding: utf-8 -*-
#
# File: RTSFolder.py
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

RTSFolder_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RTSFolder(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IRTSFolder)

    meta_type = 'RTSFolder'
    _at_rename_after_creation = True

    schema = RTSFolder_schema

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

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container):
        """
        """

        if 'rating_tracking_system' not in self.objectIds():
            self.invokeFactory('RatingTrackingSystem', 'rating_tracking_system')
            self['rating_tracking_system'].setTitle('Rating Tracking System')
        BaseFolder.manage_afterAdd(self, item, container)


registerType(RTSFolder, PROJECTNAME)
# end of class RTSFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



