from Products.ProjectDatabase.reports.ProjectContactsReportFactory \
    import ProjectContactsReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectContactsReport(BaseReport):
    def getReport(self):
        factory = ProjectContactsReportFactory(self.context, projects=self._projects)
        return factory.getReport()
