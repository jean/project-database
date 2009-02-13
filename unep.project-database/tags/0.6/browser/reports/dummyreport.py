from Products.ProjectDatabase.reports.DummyReportFactory import getDummyReport
from basereport import BaseReport


class DummyReport(BaseReport):
    def getReport(self):
        return getDummyReport(self.context)
