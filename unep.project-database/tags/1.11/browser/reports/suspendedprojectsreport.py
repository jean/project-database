from Products.ProjectDatabase.reports.SuspendedProjectsReportFactory \
    import SuspendedProjectsReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class SuspendedProjectsReport(BaseReport):
    def getReport(self):
        factory = SuspendedProjectsReportFactory(self.context, projects=self._projects)
        return factory.getReport()
