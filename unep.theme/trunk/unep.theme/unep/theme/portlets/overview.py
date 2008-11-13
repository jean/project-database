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

    title = _(u'Overview')

class Renderer(base.Renderer):

    @property
    def available(self):
        return True

    def render(self):
        return ViewPageTemplateFile('overview.pt')

class AddForm(base.AddForm):
    form_fields = form.Fields(IOverviewPortlet)
    label = _(u"Add Overview Portlet")
    description = _(u"This portlet display a overview menu.")

    def create(self):
        return Assignment()

class EditForm(base.EditForm):
    form_fields = form.Fields(IOverviewPortlet)
    label = _(u"Edit Overview Portlet")
    description = _(u"This portlet display a overview menu.")
