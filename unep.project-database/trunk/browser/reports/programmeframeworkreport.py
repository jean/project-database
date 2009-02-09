from Products.ProjectDatabase.reports.ProgrammeFrameworkReportFactory \
    import ProgrammeFrameworkReportFactory
from basereport import BaseReport

class ProgrammeFrameworkReport(BaseReport):
    def getReport(self):
        factory = ProgrammeFrameworkReportFactory(self.context)
        return factory.getReport()
