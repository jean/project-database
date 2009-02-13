from Products.ProjectDatabase.reports.PPGImplStatusReportFactory \
    import PPGImplementationStatusReportFactory
from basereport import BaseReport

class PPGImplStatusReport(BaseReport):
    def getReport(self):
        factory = PPGImplementationStatusReportFactory(self.context)
        return factory.getReport()
