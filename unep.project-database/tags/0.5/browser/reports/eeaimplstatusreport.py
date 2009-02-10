from Products.ProjectDatabase.reports.EEAImplStatusReportFactory \
    import EEAImplementationStatusReportFactory
from basereport import BaseReport

class EEAImplStatusReport(BaseReport):
    def getReport(self):
        factory = EEAImplementationStatusReportFactory(self.context)
        return factory.getReport()
