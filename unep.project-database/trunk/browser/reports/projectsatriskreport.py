from Products.ProjectDatabase.reports.ProjectsAtRiskReportFactory \
    import ProjectsAtRiskReportFactory
from basereport import BaseReport

class ProjectsAtRiskReport(BaseReport):
    def getReport(self):
        factory = ProjectsAtRiskReportFactory(self.context)
        return factory.getReport('Projects at Risk')
