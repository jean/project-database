from zope.publisher.interfaces.browser import IBrowserView
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

from Products.ProjectDatabase.reports.DummyReportFactory import getDummyReport


class DummyReport(BrowserView):
    implements(IBrowserView)

    __call__ = ViewPageTemplateFile("simplehtmlreport.pt")

    def getReport(self):
        return getDummyReport(self.context)
