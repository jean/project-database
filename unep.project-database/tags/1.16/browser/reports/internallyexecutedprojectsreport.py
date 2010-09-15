from Products.ProjectDatabase.reports.InternallyExecutedProjectsReportFactory \
    import InternallyExecutedProjectsReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class InternallyExecutedProjectsReport(BaseReport):
    def getReport(self):
        factory = InternallyExecutedProjectsReportFactory(self.context, projects=self._projects)
        return factory.getReport()
