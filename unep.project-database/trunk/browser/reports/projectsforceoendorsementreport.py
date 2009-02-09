from Products.ProjectDatabase.reports.ProjectsForCEOEndorsementReportFactory \
    import ProjectsForCEOEndorsementReportFactory
from basereport import BaseReport

class ProjectsForCEOEndorsementReport(BaseReport):
    def getReport(self):
        factory = ProjectsForCEOEndorsementReportFactory(self.context)
        return factory.getReport()
