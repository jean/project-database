from Products.ProjectDatabase.content.interfaces import IProject
from Products.ProjectDatabase.content.interfaces import IRatingTrackingSystem
from Products.ProjectDatabase.content.interfaces import IRTSFolder
from Products.ProjectDatabase.content.interfaces import IMonitoringAndEvaluation

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

    if 'project_general_info' not in ob.objectIds():
        ob.invokeFactory('ProjectGeneralInformation', 'project_general_info')
        ob['project_general_info'].edit(title='Project General Information')
    if 'fmi_folder' not in ob.objectIds():
        ob.invokeFactory('FMIFolder', 'fmi_folder')
        ob['fmi_folder'].edit(title='Financial Management Information')
    if 'monitoring_and_evaluation' not in ob.objectIds():
        ob.invokeFactory('MonitoringAndEvaluation', 'monitoring_and_evaluation')
        ob['monitoring_and_evaluation'].edit(title='Monitoring and Evaluation')
    if 'milestonesfolder' not in ob.objectIds():
        ob.invokeFactory('MilestoneFolder', 'milestonesfolder')
        ob['milestonesfolder'].edit(title='Milestones')
    if 'documents' not in ob.objectIds():
        ob.invokeFactory('Folder', 'documents')
        ob['documents'].edit(title='Documents')

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

    if 'other_project_ratings_folder' not in ob.objectIds():
        ob.invokeFactory('OtherProjectRatingsFolder', 'other_project_ratings_folder')
        ob['other_project_ratings_folder'].edit(title='Other Project Ratings')

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
        ob.invokeFactory('RatingTrackingSystem', 'rating_tracking_system')
        ob['rating_tracking_system'].edit(title='Rating Tracking System')

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
        ob.invokeFactory('RTSFolder', 'rtsfolder')
        ob['rtsfolder'].edit(title='Rating Tracking Systems')
    if 'evaluators_information' not in ob.objectIds():
        ob.invokeFactory('EvaluatorsInformation', 'evaluators_information')
        ob['evaluators_information'].edit(title='Evaluators Information')
