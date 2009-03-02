from interfaces import IFilteredSearchView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.interface import implements

class FilteredSearchView(BrowserView):
    """ provides a filtered search view based on the input values
    """
    implements(IFilteredSearchView)

    def getSearchResults(self, country, focal_area, project_type, project_title, task_manager, fund_mananger):
        """ return search results from the portal catalog
        """
        import pdb; pdb.set_trace()
        pc = getToolByName(self.context, 'portal_catalog')
        search_dict = {'portal_type':'Project'}
        if country:
            search_dict['getCountries'] = country 
        if focal_area:
            search_dict['getFocalAreas'] = focal_area
        if project_type:
            search_dict['getProjectType'] = project_type
        if lead_agency:
            search_dict['getLeadExecutingAgencies'] = lead_agency
        if project_title:
            search_dict['getProjectTitle'] = project_title
        if task_manager:
            search_dict['getTaskManager'] = task_manager
        if fund_manager:
            search_dict['getFundManager'] = fund_mananger
        return pc.searchResults(**search_dict)
