from Products.ProjectDatabase.content.interfaces import IProject
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
    if 'mne_folder' not in ob.objectIds():
        ob.invokeFactory('MandEfolder', 'mne_folder')
        mne_folder = ob['mne_folder']
        mne_folder.edit(title='Monitoring and Evaluation Folder')
        mne_folder.invokeFactory('MonitoringAndEvaluation', 'monitoring_and_evaluation')
        mne_folder['monitoring_and_evaluation'].edit(title='Monitoring and Evaluation')
    if 'milestones' not in ob.objectIds():
        ob.invokeFactory('Milestone', 'milestones')
        ob['milestones'].edit(title='Milestones')
    if 'documents' not in ob.objectIds():
        ob.invokeFactory('Folder', 'documents')
        ob['documents'].edit(title='Documents')
