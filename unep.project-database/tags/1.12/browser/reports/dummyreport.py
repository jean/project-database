from Products.ProjectDatabase.reports.DummyReportFactory import getDummyReport
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName


class DummyReport(BaseReport):
    def getReport(self):
        return getDummyReport(self.context)
