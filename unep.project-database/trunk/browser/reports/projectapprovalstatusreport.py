from Products.ProjectDatabase.reports.ProjectApprovalStatusReportFactory \
    import ProjectApprovalStatusReportFactory
from basereport import BaseReport

class ProjectApprovalStatusReport(BaseReport):
    def getReport(self):
        factory = ProjectApprovalStatusReportFactory(self.context)
        return factory.getReport()
