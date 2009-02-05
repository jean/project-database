from zope.publisher.interfaces.browser import IBrowserView
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

from Products.ProjectDatabase.reports.DummyReportFactory import getDummyReport


class DummyReport(BrowserView):
    implements(IBrowserView)

    pt = ViewPageTemplateFile("simplehtmlreport.pt")

    def csv(self):
        report = self.getReport()
        return "hello,csv,world"

    def pdf(self):
        return "I am not a pdf, but I can fake it"

    def __call__(self, format=None):
        if format is None:
            format = self.request.get('format', None)

        if format == 'csv':
            return self.csv()

        if format == 'pdf':
            return self.pdf()

        return self.pt()
        
    def getReport(self):
        return getDummyReport(self.context)

    def getCSVReport(self):
        return self.__call__(format="csv")
