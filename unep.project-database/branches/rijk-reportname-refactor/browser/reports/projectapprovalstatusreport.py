from Products.ProjectDatabase.reports.ProjectApprovalStatusReportFactory \
    import ProjectApprovalStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectApprovalStatusReport(BaseReport):
    def getReport(self):
        factory = ProjectApprovalStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
