from Products.ProjectDatabase.reports.FSPReceivablesReportFactory import FSPReceivablesReportFactory
from basereport import BaseReport

class FSPReceivablesReport(BaseReport):
    def getReport(self):
        factory = FSPReceivablesReportFactory(self.context)
        return factory.getReport()
