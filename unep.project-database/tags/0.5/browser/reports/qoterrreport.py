from Products.ProjectDatabase.reports.qoterrReportFactory \
    import qoterrReportFactory
from basereport import BaseReport

class qoterrReport(BaseReport):
    def getReport(self):
        factory = qoterrReportFactory(self.context)
        return factory.getReport()
