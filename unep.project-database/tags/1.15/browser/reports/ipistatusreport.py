from Products.ProjectDatabase.reports.IPIStatusReportFactory import IPIStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class IPIStatusReport(BaseReport):
    def getReport(self):
        factory = IPIStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
