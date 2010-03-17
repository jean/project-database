from Products.ProjectDatabase.reports.FSPReceivablesReportFactory import FSPReceivablesReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class FSPReceivablesReport(BaseReport):
    def getReport(self):
        factory = FSPReceivablesReportFactory(self.context, projects=self._projects)
        return factory.getReport()
