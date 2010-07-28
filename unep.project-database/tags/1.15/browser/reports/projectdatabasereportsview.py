from zope.interface import implements
from zope.publisher.interfaces.browser import IBrowserView
from Products.Five.browser import BrowserView

class ProjectDatabaseReportsView(BrowserView):
    implements(IBrowserView)
