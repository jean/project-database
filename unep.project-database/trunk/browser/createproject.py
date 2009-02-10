from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Acquisition import aq_inner
from zope import event
from Products.Archetypes.event import ObjectInitializedEvent

class ProjectCreation(BrowserView):
    """ View for creating a project
    """
    
    def __call__(self):
        """ return the view template
        """
        context = self.context
        id = context.generateUniqueId(type_name='Project')
        context.invokeFactory(id=id, type_name='Project')
        new_context = context[id]
        event.notify(ObjectInitializedEvent(new_context))
        context.REQUEST.response.redirect(new_context.absolute_url())
      
