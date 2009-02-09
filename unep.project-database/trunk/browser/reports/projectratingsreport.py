from Products.ProjectDatabase.reports.ProjectRatingsReportFactory \
    import ProjectRatingsReportFactory
from basereport import BaseReport

class ProjectRatingsReport(BaseReport):
    def getReport(self):
        factory = ProjectRatingsReportFactory(self.context)
        return factory.getReport()
