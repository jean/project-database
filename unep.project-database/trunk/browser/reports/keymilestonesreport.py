from Products.ProjectDatabase.reports.KeyMilestonesReportFactory \
    import KeyMilestonesReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class KeyMilestonesReport(BaseReport):
    def getReport(self):
        factory = KeyMilestonesReportFactory(self.context, projects=self._projects)
        return factory.getReport()
