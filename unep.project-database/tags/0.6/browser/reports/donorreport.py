from Products.ProjectDatabase.reports.DonorReportFactory \
    import DonorReportFactory
from basereport import BaseReport

class DonorReport(BaseReport):
    def getReport(self):
        factory = DonorReportFactory(self.context)
        return factory.getReport()
