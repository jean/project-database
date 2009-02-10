from Products.ProjectDatabase.reports.ProjectImplStatusReportFactory \
    import ProjectImplementationStatusReportFactory
from basereport import BaseReport

class ProjectImplementationStatusReport(BaseReport):
    def getReport(self):
        factory = ProjectImplementationStatusReportFactory(self.context)
        return factory.getReport()
