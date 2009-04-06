from zope.interface import Interface

class IFilteredSearchView(Interface):
    """ Marker interface for the catalog searching browser view
    """

    def getSearchResults():
        """ return search results from the portal catalog
        """
