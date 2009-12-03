from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Acquisition import aq_inner
from zope import event
from Products.Archetypes.event import ObjectInitializedEvent

class CountryCreation(BrowserView):
    """ View for creating a country classification
    """
    
    def __call__(self):
        """ return the view template
        """
        context = self.context
        id = context.generateUniqueId(type_name='CountryClassification')
        context.invokeFactory(id=id, type_name='CountryClassification')
        new_context = context[id]
        new_context_url = "%s/edit" % context[id].absolute_url()
        context.REQUEST.response.redirect(new_context_url)
      
