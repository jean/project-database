from Products.ProjectDatabase.reports.ProjectsAtRiskReportFactory \
    import ProjectsAtRiskReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectsAtRiskReport(BaseReport):
    def getReport(self):
        factory = ProjectsAtRiskReportFactory(self.context, projects=self._projects)
        return factory.getReport('Projects at Risk')
