from Products.ProjectDatabase.reports.ProjectsByGeographicScopeReportFactory \
    import ProjectsByGeographicScopeReportFactory
from basereport import BaseReport

class ProjectsByGeographicScopeReport(BaseReport):
    def getReport(self):
        factory = ProjectsByGeographicScopeReportFactory(self.context)
        return factory.getReport()
