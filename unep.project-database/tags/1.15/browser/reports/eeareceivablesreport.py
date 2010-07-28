from Products.ProjectDatabase.reports.EEAReceivablesReportFactory import EEAReceivablesReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class EEAReceivablesReport(BaseReport):
    def getReport(self):
        factory = EEAReceivablesReportFactory(self.context, projects=self._projects)
        return factory.getReport()
