from Products.ProjectDatabase.reports.GefProjectsByPriorityReportFactory \
    import GefProjectsByPriorityReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class GefProjectsByPriorityReport(BaseReport):
    def getReport(self):
        factory = GefProjectsByPriorityReportFactory(self.context, projects=self._projects)
        return factory.getReport()
