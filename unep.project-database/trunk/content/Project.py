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

    ComputedField(
        name='Countries',
        widget=ComputedField._properties['widget'](
            label='Countries',
            label_msgid='ProjectDatabase_label_Countries',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='GeographicScope',
        widget=ComputedField._properties['widget'](
            label='GeographicScope',
            label_msgid='ProjectDatabase_label_GeographicScope',
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
        searchable=True,
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
    ComputedField(
        name='GEFid',
        searchable=True,
        widget=ComputedField._properties['widget'](
            label='Gefid',
            label_msgid='ProjectDatabase_label_GEFid',
            i18n_domain='ProjectDatabase',
        ),
    ),
    ComputedField(
        name='ProjectSummaryDescription',
        searchable=True,
        widget=ComputedField._properties['widget'](
            label='Project Summary',
            label_msgid='ProjectDatabase_label_ProjectSummary',
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
        fin_objs = self.fmi_folder.getAllFinanceObjects()
        total = self.getZeroMoneyInstance()
        for fo in fin_objs:
            total += fo.getTotalFinanceObject()
        return total

    security.declarePublic('getTotalUNEPGEFAmount')
    def getTotalUNEPGEFAmount(self):
        """
        """
        fin_objs = self.fmi_folder.getAllFinanceObjects()
        total = self.getZeroMoneyInstance()
        for fo in fin_objs:
            total += fo.getSumFinanceObjectAmount()
        return total

    security.declarePublic('getTotalUNEPFee')
    def getTotalUNEPFee(self):
        """
        """
        fin_objs = self.fmi_folder.getAllFinanceObjects()
        total = self.getZeroMoneyInstance()
        for fo in fin_objs:
            if fo is not None:
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

    security.declarePublic('getGeographicScope')
    def getGeographicScope(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return pgi.getGeographicScopeValues()

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

    security.declarePublic('getProjectSummaryDescription')
    def getProjectSummaryDescription(self):
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return pgi.getSummaryDescription()

    security.declarePublic('getGEFid')
    def getGEFid(self):
        """
        """
        pgi = self.getProjectGeneralInformation()
        if pgi:
            return pgi.getGEFid()

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
import logging
from DateTime import DateTime

import transaction
from zope import event
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.content.folder import ATFolder
from Products.Archetypes.event import ObjectInitializedEvent

from Products.ProjectDatabase.content.ProjectDatabase import CSVImporter
from Products.ProjectDatabase.content.ProjectGeneralInformation import ProjectGeneralInformation
from Products.ProjectDatabase.content.FMIFolder import FMIFolder
from Products.ProjectDatabase.content.MandEfolder import MandEfolder
from Products.ProjectDatabase.content.Milestone import Milestone
from Products.ProjectDatabase.content.ProjectGeneralInformation import PGI_CSVImporter

class Project_CSVImporter(CSVImporter):
    def __init__(self, context, csvfile, coding, debug):
        CSVImporter.__init__(self, context, csvfile, coding, debug)
        self._LOGGER = logging.getLogger('[Project import]')
        self._projects_created     = 0
        self._projects_not_created = 0
        self._pgis_created         = 0
        self._pgis_not_created     = 0

    def importCSV(self):
        dict_reader = self.getDictReader()
        pgi_importer = PGI_CSVImporter(self._context,
                                       self._csvfile,
                                       self._coding,
                                       self._debug)
        rows = [row for row in dict_reader]
        del dict_reader
        self.writeProgressTemplate(len(rows))
        for row in rows:
            gef_id = row['GEFid']
            project = self.getProject(gef_id)
            if not project:
                self._projects_not_created += 1
                self.writeMessage('Could not create project:%s' % gef_id)
                continue

            if pgi_importer.importCSV(project, row):
                project.reindexObject()
                self._pgis_created += 1
            else:
                self._pgis_not_created += 1
            count = self._pgis_created + self._pgis_not_created
            self.writeProgressLine(count)
        
        msg = "Projects created:%s" % self._projects_created
        self._result_lines.append(msg)
        msg = "Projects: NOT created:%s" % self._projects_not_created
        self._result_lines.append(msg)
        msg = "PGI's created:%s" % self._pgis_created
        self._result_lines.append(msg)
        msg = "PGI's NOT created:%s" % self._pgis_not_created
        self._result_lines.append(msg)
        self.writeRedirectUrl()

    def projectExists(self, gef_id):
        '''
        Search for a project by GEFid.
        '''
        query = {'portal_type': 'Project',
                 'getGEFid': gef_id}
        brains = self._pc(**query)
        if len(brains):
            return True
        return False

    def getProject(self, gef_id):
        project = self.getProjectByGefId(gef_id) or \
                  self.createProject(self._projectdatabases)
        return project

    def createProject(self, context):
        '''
        Create a new project and all required sub objects.
        '''
        ## Create new project and add it to the context
        #project_id = context.getNextProjectId()
        #self.writeMessage('Creating project:%s' % project_id)
        #project = Project(project_id)
        #context._setOb(project_id, project)
        #new_project = context._getOb(project_id)

        ## Create the ProjectGeneralInformation and set it on the project
        #pgi_id='project_general_info'
        #pgi = ProjectGeneralInformation(pgi_id)
        #pgi.setTitle('Project General Information')
        #new_project._setOb(pgi_id, pgi)

        ## Create the FMIFolder and set it on the project
        ## Needs some more bootstrapping
        #fmi_id = 'fmi_folder'
        #fmi_folder = FMIFolder(fmi_id)
        #fmi_folder.setTitle('Financial Management Information')
        #new_project._setOb(fmi_id, fmi_folder)

        ## Create the MandEfolder and set it on the project
        #mne_id = 'mne_folder'
        #mne_folder = MandEfolder(mne_id)
        #mne_folder.setTitle('Monitoring and Evaluation Folder')
        #new_project._setOb(mne_id, mne_folder)
        #
        ## Create the Milestone folder and set it on the project
        ## Needs some more bootstrapping
        #milestone_id = 'milestones'
        #milestones = Milestone(milestone_id)
        #milestones.setTitle('Milestones')
        #new_project._setOb(milestone_id, milestones)

        ## Create the documents folder and set it on the project
        #docs_id = 'documents'
        #docs = ATFolder(docs_id)
        #docs.setTitle('Documents')
        #new_project._setOb(docs_id, docs)
        
        project_id = context.getNextProjectId()
        self.writeMessage('Creating project:%s' % project_id)
        context.invokeFactory(id=project_id, type_name='Project')
        transaction.commit()
        new_project = context._getOb(project_id)
        event.notify(ObjectInitializedEvent(new_project))
        self._projects_created += 1
        return new_project

##/code-section module-footer
