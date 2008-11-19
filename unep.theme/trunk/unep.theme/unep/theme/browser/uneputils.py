from interfaces import IUnepViewUtils
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_parent
from Products.CMFCore.interfaces import ISiteRoot
from Products.ProjectDatabase.content.interfaces import IProject
from zope.interface import implements

class UnepViewUtils:
    implements(IUnepViewUtils)

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

    def projectParentURL(self):
        """ return the URL of the parent Project object
            if it exists.
        """
        ob = aq_inner(self.context)
        while ob is not None:
            if ISiteRoot.providedBy(ob):
                break
            if IProject.providedBy(ob):
                break
            ob = aq_parent(ob)

        if IProject.providedBy(ob):
            return ob.absolute_url()

        return None
