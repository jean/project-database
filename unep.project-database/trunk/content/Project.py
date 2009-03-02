# -*- coding: utf-8 -*-
#
# File: Project.py
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
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Project_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
Project_schema['title'].required = False
Project_schema['title'].widget.visible= {'edit':'hidden', 'view':'invisible'}
##/code-section after-schema

class Project(BaseFolder, CurrencyMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProject)

    meta_type = 'Project'
    _at_rename_after_creation = True

    schema = Project_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getVocabulary')
    def getVocabulary(self, vocabName):
        """
        """
        pv_tool = getToolByName(self, 'portal_vocabularies')
        vocab = pv_tool.getVocabularyByName(vocabName)
        return vocab.getDisplayList(vocab)

    security.declarePublic('getProjectGeneralInformation')
    def getProjectGeneralInformation(self):
        """
        """
        return self['project_general_info']

    security.declarePublic('getAProject')
    def getAProject(self):
        """
        """
        return self

    # Manually created methods

    security.declarePublic('getTotalGEFAmount')
    def getTotalGEFAmount(self):
        """
        """
        fin_objs = self.fmi_folder.objectValues(spec='Financials')
        total = self.getZeroMoneyInstance()
        for fo in fin_objs:
            total += fo.getTotalFinanceObject()
        return total

    security.declarePublic('getTotalUNEPGEFAmount')
    def getTotalUNEPGEFAmount(self):
        """
        """
        fin_objs = self.fmi_folder.objectValues(spec='Financials')
        total = self.getZeroMoneyInstance()
        for fo in fin_objs:
            total += fo.getSumFinanceObjectAmount()
        return total

    security.declarePublic('getTotalUNEPFee')
    def getTotalUNEPFee(self):
        """
        """
        fin_objs = self.fmi_folder.objectValues(spec='Financials')
        total = self.getZeroMoneyInstance()
        for fo in fin_objs:
            total += fo.getFinanceObjectFee()
        return total

    security.declarePublic('isTheProjectPublished')
    def isTheProjectPublished(self):
        wft = getToolByName(self, 'portal_workflow')
        return wft.getInfoFor(self, 'review_state').lower() == 'published'

    security.declarePublic('projectRisk')
    def projectRisk(self):
        risk = 0
        #Project Risk
        pgi = self.project_general_info
        rating = pgi.getRiskRatingAtInception()
        if rating == 'S' or rating == 'H':
            risk += 1
        #PIR Risk
        mandef = self.mne_folder
        pir = mandef.getLatestPIRRating()
        rating = pir.getProjectRisk()
        if rating == 'S' or rating == 'H':
            risk += 1
        #EA Risk
        #Country Risk
        #Completion Delays
        #Disbursement Delays
        #Delayed Finanacial reports
        #Delayed Substantive reports
        #Lack of revision

        return risk

    def getProjectStaff(self):
        pgi = self.project_general_info
        mofu = self.fmi_folder.getMainFinanceObject()
        ms = self.milestones
        milestone = ms.getProjectStageMilestone()
        result = []
        principal_tm = pgi.getCurrentTMSortable(tm_category='Principal')
        if principal_tm:
            result.append([principal_tm, 'TM', pgi.getFocalAreaNames(), \
                    pgi.Title(), ms.getProjectStage(), milestone[0], \
                    milestone[1], mofu.getSumFinanceObjectAmount()])
        backup_tm = pgi.getCurrentTMSortable(tm_category='Backup')
        if backup_tm:
            result.append([backup_tm, 'PA', pgi.getFocalAreaNames(), \
                pgi.Title(), ms.getProjectStage(), milestone[0], \
                milestone[1], mofu.getSumFinanceObjectAmount()])
        if mofu:
            principal_fmo = mofu.getCurrentFMOSortable(fmo_type='Principal')
            if principal_fmo:
                result.append([principal_fmo, 'FMO', pgi.getFocalAreaNames(), \
                        pgi.Title(), ms.getProjectStage(), milestone[0], \
                        milestone[1], mofu.getSumFinanceObjectAmount()])
            backup_fmo = mofu.getCurrentFMOSortable(fmo_type='Backup')
            if backup_fmo:
                result.append([backup_fmo, 'FA', pgi.getFocalAreaNames(), \
                    pgi.Title(), ms.getProjectStage(), milestone[0], \
                    milestone[1], mofu.getSumFinanceObjectAmount()])
        return result


registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
##/code-section module-footer



