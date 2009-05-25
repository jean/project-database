from Products.ProjectDatabase.reports.CancelledProjectsReportFactory \
    import CancelledProjectsReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class CancelledProjectsReport(BaseReport):
    def getReport(self):
        factory = CancelledProjectsReportFactory(self.context, projects=self._projects)
        return factory.getReport()
