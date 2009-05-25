from Products.ProjectDatabase.reports.ProjectsByStaffReportFactory \
    import ProjectsByStaffReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectsByStaffReport(BaseReport):
    def getReport(self):
        factory = ProjectsByStaffReportFactory(self.context, projects=self._projects)
        return factory.getReport()
