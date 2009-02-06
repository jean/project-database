from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.formlib import form
from zope.interface import implements
from Products.CMFPlone import PloneMessageFactory as _

class IOverviewPortlet(IPortletDataProvider):
    """Provides the overview menu on a site"""


class Assignment(base.Assignment):
    implements(IOverviewPortlet)
    title = _(u'Projects Overview')

class Renderer(base.Renderer):
    available = True
    render = ViewPageTemplateFile('overview.pt')

class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
