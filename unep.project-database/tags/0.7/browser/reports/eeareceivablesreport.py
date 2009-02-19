from Products.ProjectDatabase.reports.EEAReceivablesReportFactory import EEAReceivablesReportFactory
from basereport import BaseReport

class EEAReceivablesReport(BaseReport):
    def getReport(self):
        factory = EEAReceivablesReportFactory(self.context)
        return factory.getReport()
