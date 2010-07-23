# -*- coding: utf-8 -*-
#
# File: FMIFolder.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mikejmets@gmail.com>, Jurgen Blignaut
<jurgen.blignaut@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ProjectDatabase.content.CurrencyMixin import CurrencyMixin
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
import logging
logger = logging.getLogger('[FMIFolder]')
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

FMIFolder_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class FMIFolder(BaseFolder, CurrencyMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IFMIFolder)

    meta_type = 'FMIFolder'
    _at_rename_after_creation = True

    schema = FMIFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    security.declarePublic('getTotalPPGAmount')
    def getTotalPPGAmount(self):
        result = self.getZeroMoneyInstance()
        ppg = self.get('ppg', None)
        if ppg:
            result = ppg.getSumFinanceObjectAmount()
        return result

    def _queryObjects(self, cat_ids=None):
        pc = getToolByName(self, 'portal_catalog')
        query = {'portal_type':'Financials',
                 'path': '/'.join(self.getPhysicalPath())}
        if cat_ids is not None:
            query.update({'getFinanceCategory': cat_ids})
        brains = pc(**query)
        return [b.getObject() for b in brains]

    security.declarePublic('getTotalPDFPPGcofinActual')
    def getTotalPDFPPGcofinActual(self):
        result = self.getZeroMoneyInstance()
        fin_objs = self._queryObjects(cat_ids=\
                        ['ppg', 'pdfa', 'pdfb', 'pdfc'])
        for fo in fin_objs:
            result += fo.getTotalCoFinOfFinanceObjectActual()
        return result

    security.declarePublic('getTotalPDFFunding')
    def getTotalPDFFunding(self):
        result = self.getZeroMoneyInstance()
        fin_objs = self._queryObjects(cat_ids=\
                        ['ppg', 'pdfa', 'pdfb', 'pdfc'])
        for fo in fin_objs:
            result += fo.getSumFinanceObjectAmount()
        return result

    security.declarePublic('getMainFinanceObject')
    def getMainFinanceObject(self):
        for item in ('fsp', 'msp', 'eea',):
            mfos = self._queryObjects(cat_ids=item)
            if mfos:
                return mfos[0]

    def getAllFinanceObjects(self):
        return self._queryObjects()

    security.declarePublic('getTotalGrantToUnep')
    def getTotalGrantToUnep(self):
        result = self.getZeroMoneyInstance()
        for fo in self.getAllFinanceObjects():
            amount = fo.getSumFinanceObjectAmount()
            if amount:
                result += amount
        return result

    security.declarePublic('getTotalDisbursements')
    def getTotalDisbursements(self):
        result = self.getZeroMoneyInstance()
        for fo in self.getAllFinanceObjects():
            amount = fo.getSumCashDisbursements()
            if amount:
                result += amount
        return result

    security.declarePublic('getTotalUnepFee')
    def getTotalUnepFee(self):
        result = self.getZeroMoneyInstance()
        for fo in self.getAllFinanceObjects():
            amount = fo.getFinanceObjectFee()
            if amount:
                result += amount
        return result

    security.declarePublic('getTotalActualCofin')
    def getTotalActualCofin(self):
        result = self.getZeroMoneyInstance()
        for fo in self.getAllFinanceObjects():
            amount = fo.getTotalCoFinOfFinanceObjectActual()
            if amount:
                result += amount
        return result

    security.declarePublic('getFspSubProjects')
    def getFspSubProjects(self):
        fsps = self._queryObjects(cat_ids=['fsp',])
        subprojects = []
        for fsp in fsps:
            tempsubs = fsp.getSubProjects()
            if tempsubs is not None and len(tempsubs) > 0:
                subprojects.extend(tempsubs)
        return subprojects


registerType(FMIFolder, PROJECTNAME)
# end of class FMIFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



