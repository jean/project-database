from Products.ProjectDatabase.content.interfaces import IProject
from Products.ProjectDatabase.content.interfaces import IRatingTrackingSystem
from Products.ProjectDatabase.content.interfaces import IRTSFolder
from Products.ProjectDatabase.content.interfaces import IMonitoringAndEvaluation
from Products.ProjectDatabase.content.ProjectGeneralInformation import ProjectGeneralInformation
from Products.ProjectDatabase.content.MonitoringAndEvaluation import MonitoringAndEvaluation
from Products.ProjectDatabase.content.MilestoneFolder import MilestoneFolder
from Products.ProjectDatabase.content.FMIFolder import FMIFolder
from Products.ProjectDatabase.content.OtherProjectRatingsFolder import OtherProjectRatingsFolder
from Products.ProjectDatabase.content.RTSFolder import RTSFolder
from Products.ProjectDatabase.content.EvaluatorsInformation import EvaluatorsInformation
from Products.ProjectDatabase.content.RatingTrackingSystem import RatingTrackingSystem
from Products.UpfrontContacts.Organisation import Organisation

import logging
LOG = logging.getLogger('ProjectDatabase.events.events')

def projectInitialized(event):
    """ We are handling the object created event for 
        classes implementing the IProject interface
    """
    LOG.info('Handling ObjectInitialized for Project')

    ob = event.object
    if not IProject.providedBy(ob):
        return

    if ob.isTemporary():
        return

    if 'project_general_information' not in ob.objectIds():
        ob._setObject('project_general_information', ProjectGeneralInformation('project_general_information'))
        ob['project_general_information'].edit(title='Project General Information')
        ob['project_general_information'].reindexObject()
    ob['project_general_information'].reindexObject()
    if 'fmi_folder' not in ob.objectIds():
        ob._setObject('fmi_folder', FMIFolder('fmi_folder'))
        ob['fmi_folder'].edit(title='Financial Management Information')
    if 'monitoring_and_evaluation' not in ob.objectIds():
        ob._setObject('monitoring_and_evaluation', MonitoringAndEvaluation('monitoring_and_evaluation'))
        ob['monitoring_and_evaluation'].edit(title='Monitoring and Evaluation')
    if 'milestonesfolder' not in ob.objectIds():
        ob._setObject('milestonesfolder', MilestoneFolder('milestonesfolder'))
        ob['milestonesfolder'].edit(title='Milestones')
    if 'contacts-1' not in ob.objectIds():
        ob._setObject('contacts-1', Organisation('contacts-1'))
        ob['contacts-1'].edit(title='Contacts')

def ratingTrackingSystemInitialized(event):
    """ We are handling the object created event for 
        classes implementing the IRatingTrackingSystem interface
    """
    LOG.info('Handling ObjectInitialized for RatingTrackingSystem')

    ob = event.object
    if not IRatingTrackingSystem.providedBy(ob):
        return

    if ob.isTemporary():
        return

    #if 'pir_ratings' not in self.objectIds():
    #    self.invokeFactory('PIRRatingFolder', 'pir_ratings')
    #    self['pir_ratings'].setTitle('PIR Ratings')
    if 'other_project_ratings_folder' not in ob.objectIds():
        ob._setObject('other_project_ratings_folder', OtherProjectRatingsFolder('other_project_ratings_folder'))
        ob['other_project_ratings_folder'].edit(title='Other Project Ratings')
        ob['other_project_ratings_folder'].reindexObject()

def rtsFolderInitialized(event):
    """ We are handling the object created event for 
        classes implementing the IRTSFolder interface
    """
    LOG.info('Handling ObjectInitialized for RTSFolder')

    ob = event.object
    if not IRTSFolder.providedBy(ob):
        return

    if ob.isTemporary():
        return

    if 'rating_tracking_system' not in ob.objectIds():
        ob._setObject('rating_tracking_system', RatingTrackingSystem('rating_tracking_system'))
        ob['rating_tracking_system'].edit(title='Rating Tracking System')
        ob['rating_tracking_system'].reindexObject()

def monitoringAndEvaluationInitialized(event):
    """ We are handling the object created event for 
        classes implementing the IMonitoringAndEvaluation interface
    """
    LOG.info('Handling ObjectInitialized for MonitoringAndEvaluation')

    ob = event.object
    if not IMonitoringAndEvaluation.providedBy(ob):
        return

    if ob.isTemporary():
        return

    if 'rtsfolder' not in ob.objectIds():
        ob._setObject('rtsfolder', RTSFolder('rtsfolder'))
        ob['rtsfolder'].edit(title='Rating Tracking Systems')
    if 'evaluators_information' not in ob.objectIds():
        ob._setObject('evaluators_information', EvaluatorsInformation('evaluators_information'))
        ob['evaluators_information'].edit(title='Evaluators Information')
