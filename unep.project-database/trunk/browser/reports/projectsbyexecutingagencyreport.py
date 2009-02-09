from Products.ProjectDatabase.reports.ProjectsByExecutingAgencyReportFactory \
    import ProjectsByExecutingAgencyReportFactory
from basereport import BaseReport

class ProjectsByExecutingAgencyReport(BaseReport):
    def getReport(self):
        factory = ProjectsByExecutingAgencyReportFactory(self.context)
        return factory.getReport()
