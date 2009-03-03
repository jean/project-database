from interfaces import IFilteredSearchView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.interface import implements
from DateTime import DateTime

class FilteredSearchView(BrowserView):
    """ provides a filtered search view based on the input values
    """
    implements(IFilteredSearchView)

    def getSearchResults(self, request):
        """ return search results from the portal catalog
        """
        pc = getToolByName(self.context, 'portal_catalog')
        search_dict = {'portal_type':'Project'}

        country = request.get('country', None)
        if country:
            search_dict['getCountries'] = country 

        focal_area = request.get('focal_area', None)
        if focal_area:
            search_dict['getFocalAreas'] = focal_area

        project_type = request.get('project_type', None)
        if project_type:
            search_dict['getProjectType'] = project_type

        executing_agency = request.get('executing_agency', None)
        if executing_agency:
            search_dict['getLeadExecutingAgencies'] = executing_agency

        gef_from_month = request.get('gef_from_month', None)
        gef_from_year = request.get('gef_from_year', None)
        gef_to_month = request.get('gef_to_month', None)
        gef_to_year = request.get('gef_to_year', None)
        if (gef_from_month and gef_from_year) or \
                (gef_to_month and gef_to_year):
            if gef_from_year and not gef_to_year:
                range = 'min'
                query = DateTime('%s/%s/1' % (gef_from_year, gef_from_month))
            elif not gef_from_year and gef_to_year:
                range = 'max'
                query = getMonthEnd(gef_to_year, gef_to_month)
            else:
                range = 'minmax'
                query = [DateTime('%s/%s/1' % (gef_from_year, gef_from_month)), \
                        getMonthEnd(gef_to_year, gef_to_month)]
                search_dict['getGEFApprovalDate'] = {'range':range, 'query':query}

        unep_from_month = request.get('unep_from_month', None)
        unep_from_year = request.get('unep_from_year', None)
        unep_to_month = request.get('unep_to_month', None)
        unep_to_year = request.get('unep_to_year', None)
        if (unep_from_month and unep_from_year) or \
                (unep_to_month and unep_to_year):
            if unep_from_year and not unep_to_year:
                range = 'min'
                query = DateTime('%s/%s/1' % (unep_from_year, unep_from_month))
            elif not unep_from_year and unep_to_year:
                range = 'max'
                query = getMonthEnd(unep_to_year, unep_to_month)
            else:
                range = 'minmax'
                query = [DateTime('%s/%s/1' % (unep_from_year, unep_from_month)), \
                        getMonthEnd(unep_to_year, unep_to_month)]
                search_dict['getUNEPApprovalDate'] = {'range':range, 'query':query}

        project_title = request.get('project_title', None)
        if project_title:
            search_dict['getProjectTitle'] = project_title

        task_manager = request.get('task_manager', None)
        if task_manager:
            search_dict['getTaskManager'] = task_manager

        fund_manager = request.get('fund_manager', None)
        if fund_manager:
            search_dict['getFundManager'] = fund_manager

        print search_dict

        return pc.searchResults(**search_dict)

    __call__ = getSearchResults

    def getSearchYearVocabulary(self):
        now = DateTime()
        year = DateTime().year()
        startYear = year - 20
        endYear = year + 20
        result = []
        while startYear < endYear:
            result.append(str(startYear))
            startYear += 1
        return result

def getMonthEnd(year, month):
    next_month_start = DateTime('%s-01' % DateTime(DateTime('%s/%s/1' % (year, month))+32).strftime('%Y-%m'))
    return next_month_start-1
