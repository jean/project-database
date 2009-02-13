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
        ob.invokeFactory('ProjectGeneralInformation', 'project_general_info',
            title='Project General Information')
    if 'fmi_folder' not in ob.objectIds():
        ob.invokeFactory('FMIFolder', 'fmi_folder',
            title='Financial Management Information')
    if 'mne_folder' not in ob.objectIds():
        ob.invokeFactory('MandEfolder', 'mne_folder',
            title='Monitoring and Evaluation Folder')
    if 'milestones' not in ob.objectIds():
        ob.invokeFactory('Milestone', 'milestones',
            title='Milestones')
    if 'documents' not in ob.objectIds():
        ob.invokeFactory('Folder', 'documents', title='Documents')
