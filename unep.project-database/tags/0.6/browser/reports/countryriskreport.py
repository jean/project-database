from Products.ProjectDatabase.reports.CountryRiskReportFactory \
    import CountryRiskReportFactory
from basereport import BaseReport

class CountryRiskReport(BaseReport):
    def getReport(self):
        factory = CountryRiskReportFactory(self.context)
        return factory.getReport()
