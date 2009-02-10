from Products.ProjectDatabase.reports.FSPImplStatusReportFactory \
    import FSPImplementationStatusReportFactory
from basereport import BaseReport

class FSPImplStatusReport(BaseReport):
    def getReport(self):
        factory = FSPImplementationStatusReportFactory(self.context)
        return factory.getReport()
