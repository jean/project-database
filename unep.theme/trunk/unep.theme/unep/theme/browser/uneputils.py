from interfaces import IUnepViewUtils
from Products.CMFCore.utils import getToolByName

class UnepViewUtils:

    def projectDatabasesURL(self):
        """ return the URL of the project databases folder
        """
        return self.context.projectdatabases.absolute_url()

    def contactsURL(self):
        """ return the URL of the contacts manager
        """
        pct = getToolByName(self.context, 'portal_catalog')
        brains = pct(portal_type='ContactManager')
        if brains:
            return brains[0].getURL()
        else:
            return self.context.absolute_url()
