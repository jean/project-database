from Products.ProjectDatabase.reports.InternallyExecutedProjectsReportFactory \
    import InternallyExecutedProjectsReportFactory
from basereport import BaseReport

class InternallyExecutedProjectsReport(BaseReport):
    def getReport(self):
        factory = InternallyExecutedProjectsReportFactory(self.context)
        return factory.getReport()
