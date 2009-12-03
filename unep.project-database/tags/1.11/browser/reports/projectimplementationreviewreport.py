from Products.ProjectDatabase.reports.ProjectImplementationReviewReportFactory \
    import ProjectImplementationReviewReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectImplementationReviewReport(BaseReport):
    def getReport(self):
        factory = ProjectImplementationReviewReportFactory(self.context, projects=self._projects)
        return factory.getReport()
