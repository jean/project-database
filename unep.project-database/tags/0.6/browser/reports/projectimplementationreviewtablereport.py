from Products.ProjectDatabase.reports.ProjectImplementationReviewTableReportFactory import ProjectImplementationReviewTableReportFactory
from basereport import BaseReport

class ProjectImplementationReviewTableReport(BaseReport):
    def getReport(self):
        factory = ProjectImplementationReviewTableReportFactory(self.context)
        return factory.getReport()
