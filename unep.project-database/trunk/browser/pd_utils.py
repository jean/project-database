from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MyProjectsA2ZlistView(BrowserView):
    """ View for showing the member's current projects
    """
    
    template = ViewPageTemplateFile('myprojectlist.pt')

    def __call__(self):
        """ return a list of the member's personal projects
        """
        # pc = getToolByName(self, 'portal_catalog')
        # query = {
        #         'portal_type':'Project',
        #         'Creator':memberId
        #         }
        # myprojects = pc(query)
        # result = []
        # for project in myprojects:
        #     result.append({
        #         'id':       project.getId,
        #         'title':    project.Title,
        #         'link':     project.getURL()
        #         })

        return self.template()
