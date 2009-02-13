from Products.ProjectDatabase.reports.MSPImplStatusReportFactory \
    import MSPImplementationStatusReportFactory
from basereport import BaseReport

class MSPImplStatusReport(BaseReport):
    def getReport(self):
        factory = MSPImplementationStatusReportFactory(self.context)
        return factory.getReport()
