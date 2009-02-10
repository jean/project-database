from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Acquisition import aq_inner


class MyProjectsA2ZlistView(BrowserView):
    """ View for showing the member's current projects
    """
    
    template = ViewPageTemplateFile('myprojectlist.pt')

    def __call__(self):
        """ return the view template
        """
        return self.template()

    def my_project_list(self, memberId):
        """ return a list of the member's personal projects
        """
        context = aq_inner(self.context)

        pc = getToolByName(context, 'portal_catalog')
        query = {
                'portal_type': 'Project',
                'Creator': memberId
                }
        myprojects = pc(query)
        result = []
        for project in myprojects:
            result.append({
                'id':       project.getId,
                'title':    project.Title,
                'link':     project.getURL()
                })

        return result


class MyProjectsSectionListView(BrowserView):
    """ View for showing sections of the member's current projects
    """
    
    template = ViewPageTemplateFile('myprojectsection.pt')

    def __call__(self):
        """ return the view template
        """
        return self.template()

    def my_project_sections(self, memberId):
        """ return a list of the member's projects
        """
        context = aq_inner(self.context)

        pc = getToolByName(context, 'portal_catalog')
        query = {
                'portal_type': 'Project',
                'Creator': memberId
                }
        myprojects = pc(query)
        result = []
        for project in myprojects:
            result.append({
                'id':       project.getId,
                'title':    project.Title,
                'link':     '%s/%s' % (project.getURL(), self.sectionLink())
                })

        return result

    def sectionLink(self):
        return 'general'
    
    def sectionName(self):
        return 'General Information'



class MyProjectsGeneralListView(MyProjectsSectionListView):

    def sectionLink(self):
        return 'project_general_info'
    
    def sectionName(self):
        return 'General Information'


class MyProjectsFinancialListView(MyProjectsSectionListView):

    def sectionLink(self):
        return 'fmi_folder'
    
    def sectionName(self):
        return 'Financial Management Information'


class MyProjectsDocumentsListView(MyProjectsSectionListView):

    def sectionLink(self):
        return 'documents'
    
    def sectionName(self):
        return 'Documents'


class MyProjectsMilestonesListView(MyProjectsSectionListView):

    def sectionLink(self):
        return 'milestonesfolder'
    
    def sectionName(self):
        return 'Milestones'


class MyProjectsMonitoringListView(MyProjectsSectionListView):

    def sectionLink(self):
        return 'monitoring_and_evaluation'
    
    def sectionName(self):
        return 'Monitoring and Evaluation'
