from Products.ProjectDatabase.reports.ProjectsDueForClosureReportFactory \
    import ProjectsDueForClosureReportFactory
from basereport import BaseReport

class ProjectsDueForClosureReport(BaseReport):
    def getReport(self):
        factory = ProjectsDueForClosureReportFactory(self.context)
        return factory.getReport()
