from Products.ProjectDatabase.reports.CompletedProjectsReportFactory \
    import CompletedProjectsReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class CompletedProjectsReport(BaseReport):
    def getReport(self):
        factory = CompletedProjectsReportFactory(self.context, projects=self._projects)
        return factory.getReport()
