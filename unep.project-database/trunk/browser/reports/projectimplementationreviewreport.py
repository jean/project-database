from Products.ProjectDatabase.reports.ProjectImplementationReviewReportFactory \
    import ProjectImplementationReviewReportFactory
from basereport import BaseReport

class ProjectImplementationReviewReport(BaseReport):
    def getReport(self):
        factory = ProjectImplementationReviewReportFactory(self.context)
        return factory.getReport()
