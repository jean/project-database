from Products.ProjectDatabase.reports.CancelledProjectsReportFactory \
    import CancelledProjectsReportFactory
from basereport import BaseReport

class CancelledProjectsReport(BaseReport):
    def getReport(self):
        factory = CancelledProjectsReportFactory(self.context)
        return factory.getReport()
