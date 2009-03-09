from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.formlib import form
from zope.interface import implements
from Products.CMFPlone import PloneMessageFactory as _

class IMyProjectsView(IPortletDataProvider):
    """Provides the overview menu on a site"""


class Assignment(base.Assignment):
    implements(IMyProjectsView)
    title = _(u'My Projects')

class Renderer(base.Renderer):
    available = True
    render = ViewPageTemplateFile('myprojects.pt')

class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()

