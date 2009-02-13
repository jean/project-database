from Products.ProjectDatabase.reports.PPGReceivablesReportFactory import PPGReceivablesReportFactory
from basereport import BaseReport

class PPGReceivablesReport(BaseReport):
    def getReport(self):
        factory = PPGReceivablesReportFactory(self.context)
        return factory.getReport()
