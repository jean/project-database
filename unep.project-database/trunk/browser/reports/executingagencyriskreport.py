from Products.ProjectDatabase.reports.ExecutingAgencyReportFactory \
    import ExecutingAgencyReportFactory
from basereport import BaseReport

class ExecutingAgencyReport(BaseReport):
    def getReport(self):
        factory = ExecutingAgencyReportFactory(self.context)
        return factory.getReport()
