from Products.ProjectDatabase.reports.ClosedProjectsReportFactory \
    import ClosedProjectsReportFactory
from basereport import BaseReport

class ClosedProjectsReport(BaseReport):
    def getReport(self):
        factory = ClosedProjectsReportFactory(self.context)
        return factory.getReport()
