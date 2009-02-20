# -*- coding: utf-8 -*-
#
# File: MandEfolder.py
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


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MandEfolder_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MandEfolder(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IMandEfolder)

    meta_type = 'MandEfolder'
    _at_rename_after_creation = True

    schema = MandEfolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    security.declarePublic('getLatestPIRRating')
    def getLatestPIRRating(self):
        year = '1900'
        for pir in self.objectValues(spec='PIRRating'):
            if pir.getFiscalYear() > year:
                year = pir.getFiscalYear()
        if year != '1900':
            return pir

    security.declarePublic('getFinalReportInfoInYear')
    def getFinalReportInfoInYear(self, year_end):
        for mne in self.objectValues(spec='MonitoringAndEvaluation'):
            report_date = mne.getEvaluationProcessStatusDates('FinalReport')
            if report_date and \
               report_date <= year_end and \
               report_date > year_end - 365:
                rating = mne.getEvaluationRatingsDates('Overall rating')
                return mne.getEvaluationType, report_date, rating
        None, None, None
  

registerType(MandEfolder, PROJECTNAME)
# end of class MandEfolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



