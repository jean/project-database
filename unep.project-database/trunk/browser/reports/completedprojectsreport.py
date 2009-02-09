from Products.ProjectDatabase.reports.CompletedProjectsReportFactory \
    import CompletedProjectsReportFactory
from basereport import BaseReport

class CompletedProjectsReport(BaseReport):
    def getReport(self):
        factory = CompletedProjectsReportFactory(self.context)
        return factory.getReport()
