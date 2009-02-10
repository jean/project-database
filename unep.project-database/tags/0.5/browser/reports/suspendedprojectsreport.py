from Products.ProjectDatabase.reports.SuspendedProjectsReportFactory \
    import SuspendedProjectsReportFactory
from basereport import BaseReport

class SuspendedProjectsReport(BaseReport):
    def getReport(self):
        factory = SuspendedProjectsReportFactory(self.context)
        return factory.getReport()
