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
         'StrategicPriority': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'GEFPhase': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Scope': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Status': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Division': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ProjectType': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'EvaluationType': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'EAPOP': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'UNEPThematicPriority': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'OperationalProgramme': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'FinanceCategory': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'LeadAgency': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Country': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'Region': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'EABiodiversity': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'MultipleFocalAreas': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'FocalArea': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'StrategicObjectives': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'InceptionRiskRating': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'TrustFund': ('VdexVocabulary', 'SimpleVocabularyTerm'),
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
def _defaultSkinDefinition(skin_prefix):
    """
    Useful method to avoid lots of typing
    """
    return {'Plone Default':
            ['%s_images'%skin_prefix,'%s_styles'%skin_prefix,'%s_templates'%skin_prefix]}

def _setupSkins(context, skin_prefix, definition=None):
    """
    GS ignores the 'insert-after' directive in skins.xml and ArchgenXML does not provide
    for multiple skins in skins.xml.

    Parameter definition has form eg. 
        {'Plone Default':
            ['plone4radioblog_common','plone4radioblog_admin','plone4radioblog_admin_plone']}

    Parameter skin_prefix is eg. plone4radioblog.

    This function ensures that only desirable layers are present in the skin. It does not 
    add any new layers - that is handled by GS. It changes layers and their order.

    The layers are hard-coded to appear after custom.
    """
    portal = context.getSite()
    ps = portal.portal_skins
    skins = ps._getSelections()

    if definition is None:
        definition = _defaultSkinDefinition(skin_prefix)

    for skin, layers in definition.items():
        if not skin in skins: continue
        new_layers = []
        current_layers = skins[skin].split(',')
        for current_layer in current_layers:
            if current_layer.startswith(skin_prefix) and (current_layer not in layers):
                # This layer must be removed from the skin
                pass
            else:
                new_layers.append(current_layer)

        # Change the layer order
        layers.reverse()
        for layer in layers:
            if layer in new_layers:
                new_layers.remove(layer)
                new_layers.insert(1, layer)
            else:
                new_layers.insert(1, layer)

        skins[skin] = ','.join(new_layers)

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
        'MEProcessStep': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'EvaluationTypeMilestone': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'ApprovalInitiationClosure': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'ProjectProcesses': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'TMCategory': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'ProjectExecutingAgencyDescription': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        #'EvaluationType': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'TrustFund': ('VdexVocabulary', 'SimpleVocabularyTerm'),
        'ConceptDevelopmentActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'PIFApprovalActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'PPGApprovalActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'PPGImplementationActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'ProjectImplementationActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'ProjectApprovalActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'NewPhaseApprovalActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'NewPhaseImplementationActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'EvaluationDatesActions': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'MilestoneResult': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'ProjectRevisionType': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'RiskLevel': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'PIFStage': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'EvaluationCriteria': ('VdexVocabulary', 'SimpleVocabularyterm'),
        'EvaluatorRole': ('VdexVocabulary', 'SimpleVocabularyterm'),
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
                print vocabname
                atvm[vocabname].importXMLBinding(data)
            else:
                pass

    # todo: move this to another method                
    _setupSkins(context, 'projectdatabase')
                
##/code-section FOOT
