from Products.ProjectDatabase.content.interfaces import IProject
from Products.ProjectDatabase.content.ProjectGeneralInformation import ProjectGeneralInformation
from Products.ProjectDatabase.content.MonitoringAndEvaluation import MonitoringAndEvaluation
from Products.ProjectDatabase.content.MilestoneFolder import MilestoneFolder
from Products.ProjectDatabase.content.FMIFolder import FMIFolder
from Products.UpfrontContacts.Organisation import Organisation

def projectInitialized(event):
    """ We are handling the object created event for 
        classes implementing the IProject interface
    """
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
