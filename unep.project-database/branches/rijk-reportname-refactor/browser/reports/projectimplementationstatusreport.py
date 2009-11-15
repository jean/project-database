from Products.ProjectDatabase.reports.ProjectImplStatusReportFactory \
    import ProjectImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectImplementationStatusReport(BaseReport):
    def getReport(self):
        factory = ProjectImplementationStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
