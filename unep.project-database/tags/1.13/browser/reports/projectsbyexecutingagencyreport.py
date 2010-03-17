from Products.ProjectDatabase.reports.ProjectsByExecutingAgencyReportFactory \
    import ProjectsByExecutingAgencyReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectsByExecutingAgencyReport(BaseReport):
    def getReport(self):
        factory = ProjectsByExecutingAgencyReportFactory(self.context, projects=self._projects)
        return factory.getReport()
