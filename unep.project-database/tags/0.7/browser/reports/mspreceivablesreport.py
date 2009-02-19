from Products.ProjectDatabase.reports.MSPReceivablesReportFactory import MSPReceivablesReportFactory
from basereport import BaseReport

class MSPReceivablesReport(BaseReport):
    def getReport(self):
        factory = MSPReceivablesReportFactory(self.context)
        return factory.getReport()
