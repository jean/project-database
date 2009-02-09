from Products.ProjectDatabase.reports.ProjectImplementationStatusReportFactory \
    import ProjectImplementationStatusReportFactory
from basereport import BaseReport

class ProjectImplementationStatusReport(BaseReport):
    def getReport(self):
        factory = ProjectImplementationStatusReportFactory(self.context)
        return factory.getReport()
