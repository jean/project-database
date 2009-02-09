from Products.ProjectDatabase.reports.ProjectsByStaffReportFactory \
    import ProjectsByStaffReportFactory
from basereport import BaseReport

class ProjectsByStaffReport(BaseReport):
    def getReport(self):
        factory = ProjectsByStaffReportFactory(self.context)
        return factory.getReport()
