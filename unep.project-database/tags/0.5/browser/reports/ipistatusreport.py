from Products.ProjectDatabase.reports.IPIStatusReportFactory import IPIStatusReportFactory
from basereport import BaseReport

class IPIStatusReport(BaseReport):
    def getReport(self):
        factory = IPIStatusReportFactory(self.context)
        return factory.getReport()
