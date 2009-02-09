from Products.ProjectDatabase.reports.ExecutingAgencyRiskReportFactory \
    import ExecutingAgencyRiskReportFactory
from basereport import BaseReport

class ExecutingAgencyRiskReport(BaseReport):
    def getReport(self):
        factory = ExecutingAgencyRiskReportFactory(self.context)
        return factory.getReport()
