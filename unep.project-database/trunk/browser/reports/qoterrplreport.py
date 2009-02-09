from Products.ProjectDatabase.reports.qoterrplReportFactory \
    import qoterrplReportFactory
from basereport import BaseReport

class qoterrplReport(BaseReport):
    def getReport(self):
        factory = qoterrplReportFactory(self.context)
        return factory.getReport()
