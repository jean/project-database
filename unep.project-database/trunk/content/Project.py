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
from Products.ProjectDatabase.widgets.UNEPSelectionWidget import UNEPSelectionWidget
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
from types import StringTypes
from DateTime import DateTime
##/code-section module-header

schema = Schema((

    ComputedField(
        name='Countries',
        widget=ComputedField._properties['widget'](
            label='Countries',
            label_msgid='ProjectDatabase_label_Countries',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='FocalAreas',
        widget=ComputedField._properties['widget'](
            label='Focalareas',
            label_msgid='ProjectDatabase_label_FocalAreas',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='ProjectType',
        widget=ComputedField._properties['widget'](
            label='Projecttype',
            label_msgid='ProjectDatabase_label_ProjectType',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='ExecutingAgencies',
        widget=ComputedField._properties['widget'](
            label='Executingagencies',
            label_msgid='ProjectDatabase_label_ExecutingAgencies',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='GEFApprovalDate',
        widget=ComputedField._properties['widget'](
            label='Gefapprovaldate',
            label_msgid='ProjectDatabase_label_GEFApprovalDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='UNEPApprovalDate',
        widget=ComputedField._properties['widget'](
            label='Unepapprovaldate',
            label_msgid='ProjectDatabase_label_UNEPApprovalDate',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label='Projecttitle',
            label_msgid='ProjectDatabase_label_ProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='TaskManager',
        widget=ComputedField._properties['widget'](
            label='Taskmanager',
            label_msgid='ProjectDatabase_label_TaskManager',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='FundManager',
        widget=ComputedField._properties['widget'](
            label='Fundmanager',
            label_msgid='ProjectDatabase_label_FundManager',
            i18n_domain='ProjectDatabase',
        ),
    ),

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
        return self.get('project_general_info', None)

    security.declarePublic('getAProject')
    def getAProject(self):
        """
        """
        return self

    # Manually created methods

    security.declarePublic('getFMIFolder')
    def getFMIFolder(self):
        """
        """
        return self.get('fmi_folder', None)

    security.declarePublic('getMilestone')
    def getMilestone(self):
        """
        """
        return self.get('milestones', None)

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
        pgi = self.getProjectGeneralInformation()
        ms = self.getMilestone()
        rating = pgi.getRiskRatingAtInception()
        if rating == 'S' or rating == 'H':
            print "Increased risk because of Rating at Inception"
            risk += 1

        #PIR Risk
        mandef = self.mne_folder
        pir = mandef.getLatestPIRRating()
        if pir:
            rating = pir.getProjectRisk()
            if rating == 'S' or rating == 'H':
                print "Increased risk because of PIR Rating"
                risk += 1

        #EA Risk
        ealist = pgi.getLeadExecutingAgencyList()
        if ealist and \
                self.aq_inner.aq_parent.hasExecutingAgencyHighRiskRatingInTwoYears( \
                            ealist):
            print "Increased risk because of EAs"
            risk += 1

        #Country Risk
        ccs = self.restrictedTraverse('countryclassification')
        countries = pgi.getCountry()
        if ccs and len(countries) == 1:
                if ccs.getLatestCountryRiskRating(countries[0]) in ['H', 'S']:
                    print "Increased risk because of Countries"
                    risk += 1

        #Completion Delays
        if self.hasProjectCompletionDelays():
            print "Increased risk because of Completion delays"
            risk += 1

        mofu = self.fmi_folder.getMainFinanceObject()
        if mofu:
            #Disbursement Delays
            last_disbursement, dummy = mofu.getLastDisbursement()
            now = DateTime()
            if not last_disbursement:
                last_disbursement = \
                        ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual')
            if last_disbursement and (now - last_disbursement) > 365:
                print "Increased risk because of Disbursement delays"
                risk += 1

            #Delayed Finanacial reports
            if mofu.hasDelayedFinancialReports():
                print "Increased risk because of Fin report delays"
                risk += 1

            #Delayed Substantive reports
            if mofu.hasDelayedSubstantiveReports():
                print "Increased risk because of Substantive report delays"
                risk += 1

            #Lack of revision
            last_revision = mofu.getLastestRevisionDate()
            if not last_revision:
                last_revision = \
                        ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual')
            if last_revision and now - last_revision > 550:
                print "Increased risk because of revision delays"
                risk += 1

        return risk

    def getProjectStaff(self):
        pgi = self.getProjectGeneralInformation()
        mofu = self.fmi_folder.getMainFinanceObject()
        if mofu:
            sumFinObjAmnt = mofu.getSumFinanceObjectAmount()
        else:
            sumFinObjAmnt = 'Unspecified'
        ms = self.milestones
        milestone = ms.getProjectStageMilestone()
        result = []
        principal_tm = pgi.getCurrentTMSortable(tm_category='Principal')
        if principal_tm:
            result.append([principal_tm, 'TM', pgi.getFocalAreaNames(), \
                    pgi.Title(), ms.getProjectStage(), milestone[0], \
                    milestone[1], sumFinObjAmnt ])
        backup_tm = pgi.getCurrentTMSortable(tm_category='Backup')
        if backup_tm:
            result.append([backup_tm, 'PA', pgi.getFocalAreaNames(), \
                pgi.Title(), ms.getProjectStage(), milestone[0], \
                milestone[1], sumFinObjAmnt])
        if mofu:
            principal_fmo = mofu.getCurrentFMOSortable(fmo_type='Principal')
            if principal_fmo:
                result.append([principal_fmo, 'FMO', pgi.getFocalAreaNames(), \
                        pgi.Title(), ms.getProjectStage(), milestone[0], \
                        milestone[1], sumFinObjAmnt])
            backup_fmo = mofu.getCurrentFMOSortable(fmo_type='Backup')
            if backup_fmo:
                result.append([backup_fmo, 'FA', pgi.getFocalAreaNames(), \
                    pgi.Title(), ms.getProjectStage(), milestone[0], \
                    milestone[1], sumFinObjAmnt])
        return result

    security.declarePrivate('_getSelectedVocabularyValueList')
    def _getSelectedVocabularyValueList(self, selections, vocabName):
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName(vocabName)
        dict = vocab.getVocabularyDict(self)
        result = []
        for value in selections:
            result.append(dict[value][0])
        return result

    security.declarePublic('getCountries')
    def getCountries(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return self._getSelectedVocabularyValueList(\
                      pgi.getCountry(), \
                      'Country')

    security.declarePublic('getFocalAreas')
    def getFocalAreas(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return self._getSelectedVocabularyValueList(\
                      pgi.getFocalArea(), \
                      'FocalArea')

    security.declarePublic('getProjectType')
    def getProjectType(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return pgi.getProjectType()

    security.declarePublic('getExecutingAgencies')
    def getExecutingAgencies(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return pgi.getLeadExecutingAgencyNames()

    security.declarePublic('getGEFApprovalDate')
    def getGEFApprovalDate(self):
        """
        """
        ms = self.getMilestone()
        if ms:
            return ms.getProjectApprovalDate('CEOApprovalEndorsementActual')

    security.declarePublic('getUNEPApprovalDate')
    def getUNEPApprovalDate(self):
        """
        """
        ms = self.getMilestone()
        if ms:
            return ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual')

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return pgi.Title()

    security.declarePublic('getTaskManager')
    def getTaskManager(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return pgi.getCurrentTM()

    security.declarePublic('getFundManager')
    def getFundManager(self):
        """
        """
        fmi = self.getFMIFolder()
        if fmi:
            mofu = fmi.getMainFinanceObject()
            if mofu:
                return mofu.getCurrentPrincipalFMO()

    security.declarePublic('getFundManagerPerson')
    def getFundManagerPerson(self):
        """
        """
        fmi = self.getFMIFolder()
        if fmi:
            mofu = fmi.getMainFinanceObject()
            if mofu:
                return mofu.getCurrentFMOPerson()

    def hasProjectCompletionDelays(self):
        ms = self.milestones
        complete_exp = ms.getProjectImplementationDate('CompletionExpected')
        if complete_exp:
            complete_act = ms.getProjectImplementationDate('CompletionActual')
            if not complete_act:
                complete_act = DateTime()
            return (complete_act - complete_exp) > 180

        return False



registerType(Project, PROJECTNAME)
# end of class Project

##code-section module-footer #fill in your manual code here
##/code-section module-footer



