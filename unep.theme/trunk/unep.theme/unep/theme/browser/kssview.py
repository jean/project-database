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

    def toggleWidget(self, fieldname, value=None):
        context = aq_inner(self.context)
        ksscore = self.getCommandSet('core')
        
        if not hasattr(context, 'getToggleFieldNames'):
            return self.render()

        #clean up - ensure no duplicates
        kw = {}
        for k, v in context.REQUEST.form.items():
            if k not in ('fieldname', 'value'):
                kw[k] = v

        #clean up - if multi in-and-out select 
        if value == '>>' or value == '<<':
            if not kw.get('selection', None):
                value = []
            else:
                value = kw['selection']
                if not isinstance(value, (list, tuple)):
                    value = [value]

        show, hide = context.getToggleFieldNames(fieldname, value, **kw)
        for fieldname in show:
            selector = ksscore.getHtmlIdSelector(
                'archetypes-fieldname-%s' % fieldname)
            ksscore.removeClass(selector, 'unep-theme-div-hidden') 

        for fieldname in hide:
            selector = ksscore.getHtmlIdSelector(
                'archetypes-fieldname-%s' % fieldname)
            ksscore.addClass(selector, 'unep-theme-div-hidden') 

        return self.render()

