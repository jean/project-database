from Products.ProjectDatabase.reports.ProjectContactsReportFactory \
    import ProjectContactsReportFactory
from basereport import BaseReport

class ProjectContactsReport(BaseReport):
    def getReport(self):
        factory = ProjectContactsReportFactory(self.context)
        return factory.getReport()
