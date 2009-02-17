from zope.interface import implements

from Acquisition import aq_inner, aq_parent
from Acquisition import Implicit
from Products.CMFCore.utils import getToolByName
from ZPublisher.HTTPRequest import HTTPRequest

from plone.app.kss.interfaces import IPloneKSSView
from plone.app.kss.plonekssview import PloneKSSView


class UnepKSSView(Implicit, PloneKSSView):
    implements(IPloneKSSView)

    def hideWidgets(self):
        context = aq_inner(self.context)
        ksscore = self.getCommandSet('core')
        
        if not hasattr(context, 'getHideFieldNames'):
            return self.render()

        fieldnames = context.getHideFieldNames()
        for fieldname in fieldnames:
            selector = ksscore.getHtmlIdSelector(
                'archetypes-fieldname-%s' % fieldname)
            ksscore.addClass(selector, 'unep-theme-div-hidden') 

        return self.render()

    def toggleWidget(self, fieldname, value):
        context = aq_inner(self.context)
        ksscore = self.getCommandSet('core')
        
        if not hasattr(context, 'getToggleFieldNames'):
            return self.render()

        show, hide = context.getToggleFieldNames(fieldname, value)
        for fieldname in show:
            selector = ksscore.getHtmlIdSelector(
                'archetypes-fieldname-%s' % fieldname)
            ksscore.removeClass(selector, 'unep-theme-div-hidden') 

        for fieldname in hide:
            selector = ksscore.getHtmlIdSelector(
                'archetypes-fieldname-%s' % fieldname)
            ksscore.addClass(selector, 'unep-theme-div-hidden') 

        return self.render()

