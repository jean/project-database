from Products.ProjectDatabase.reports.ClosedProjectsReportFactory \
    import ClosedProjectsReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ClosedProjectsReport(BaseReport):
    def getReport(self):
        factory = ClosedProjectsReportFactory(self.context, projects=self._projects)
        return factory.getReport()
