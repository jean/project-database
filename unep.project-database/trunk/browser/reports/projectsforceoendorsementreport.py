from Products.ProjectDatabase.reports.ProjectsForCEOEndorsementReportFactory \
    import ProjectsForCEOEndorsementReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectsForCEOEndorsementReport(BaseReport):
    def getReport(self):
        factory = ProjectsForCEOEndorsementReportFactory(self.context, projects=self._projects)
        return factory.getReport()
