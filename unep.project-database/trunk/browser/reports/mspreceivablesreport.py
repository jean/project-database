from Products.ProjectDatabase.reports.MSPReceivablesReportFactory import MSPReceivablesReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class MSPReceivablesReport(BaseReport):
    def getReport(self):
        factory = MSPReceivablesReportFactory(self.context, projects=self._projects)
        return factory.getReport()
