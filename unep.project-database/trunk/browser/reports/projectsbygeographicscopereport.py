from Products.ProjectDatabase.reports.ProjectsByGeographicScopeReportFactory \
    import ProjectsByGeographicScopeReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectsByGeographicScopeReport(BaseReport):
    def getReport(self):
        factory = ProjectsByGeographicScopeReportFactory(self.context, projects=self._projects)
        return factory.getReport()
