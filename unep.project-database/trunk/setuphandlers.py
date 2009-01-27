# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
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


import logging
logger = logging.getLogger('ProjectDatabase: setuphandlers')
from Products.ProjectDatabase.config import PROJECTNAME
from Products.ProjectDatabase.config import DEPENDENCIES
import os
from config import product_globals
from Globals import package_home
from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD

def isNotProjectDatabaseProfile(context):
    return context.readDataFile("ProjectDatabase_marker.txt") is None

def installVocabularies(context):
    """creates/imports the atvm vocabs."""
    if isNotProjectDatabaseProfile(context): return 
    site = context.getSite()
    # Create vocabularies in vocabulary lib
    atvm = getToolByName(site, ATVOCABULARYTOOL)
    vocabmap = {'Category': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ProjectStatusses': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'StrategicPriority': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'GEFPhase': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ProjectCycleStage': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Scope': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ReviewEvaluation': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Assessment': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Status': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Division': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ProjectType': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'MilestoneName': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'EAPOP': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'UNEPThematicPriority': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'OperationalProgramme': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'FinanceCategory': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'FocalArea': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Country': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Region': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'EABiodiversity': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ProjectRevisionType': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'MultipleFocalAreas': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'LeadAgency': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'StrategicObjectives': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'InceptionRiskRating': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ExecutionMode': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'EAClimateChange': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'StrategicProgram': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'PhasedTranche': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        }
    for vocabname in vocabmap.keys():
        if not vocabname in atvm.contentIds():
            atvm.invokeFactory(vocabmap[vocabname][0], vocabname)

        if len(atvm[vocabname].contentIds()) < 1:
            if vocabmap[vocabname][0] == "VdexVocabulary":
                vdexpath = os.path.join(
                    package_home(product_globals), 'data', '%s.vdex' % vocabname)
                if not (os.path.exists(vdexpath) and os.path.isfile(vdexpath)):
                    logger.warn('No VDEX import file provided at %s.' % vdexpath)
                    continue
                try:
                    #read data
                    f = open(vdexpath, 'r')
                    data = f.read()
                    f.close()
                except:
                    logger.warn("Problems while reading VDEX import file "+\
                                "provided at %s." % vdexpath)
                    continue
                # this might take some time!
                atvm[vocabname].importXMLBinding(data)
            else:
                pass



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotProjectDatabaseProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()

def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotProjectDatabaseProfile(context): return
    shortContext = context._profile_path.split(os.path.sep)[-3]
    if shortContext != 'ProjectDatabase': # avoid infinite recursions
        return
    site = context.getSite()



##code-section FOOT
def installDataGridVocabularies(context):
    """ Install additional vocabularies needed by datagrid fields
        but that ArchenGenXML does not know about. """
    if isNotProjectDatabaseProfile(context): return 
    shortContext = context._profile_path.split(os.path.sep)[-3]
    if shortContext != 'ProjectDatabase': # avoid infinite recursions
        return
    site = context.getSite()
    # Create vocabularies in vocabulary lib
    atvm = getToolByName(site, ATVOCABULARYTOOL)
    vocabmap = {
        'OtherRatings': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'YesOrNo': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'Rating': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'EORatingElements': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'AgencyImplementation': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'DonorType': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'ReportType': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'MEMilestoneName': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'EvaluationTypeMilestone': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'ApprovalInitiationClosure': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'ProjectProcesses': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        }
    for vocabname in vocabmap.keys():
        if not vocabname in atvm.contentIds():
            atvm.invokeFactory(vocabmap[vocabname][0], vocabname)

        if len(atvm[vocabname].contentIds()) < 1:
            if vocabmap[vocabname][0] == "VdexVocabulary":
                vdexpath = os.path.join(
                    package_home(product_globals), 'data', '%s.vdex' % vocabname)
                if not (os.path.exists(vdexpath) and os.path.isfile(vdexpath)):
                    logger.warn('No VDEX import file provided at %s.' % vdexpath)
                    continue
                try:
                    #read data
                    f = open(vdexpath, 'r')
                    data = f.read()
                    f.close()
                except:
                    logger.warn("Problems while reading VDEX import file "+\
                                "provided at %s." % vdexpath)
                    continue
                # this might take some time!
                atvm[vocabname].importXMLBinding(data)
            else:
                pass
##/code-section FOOT
