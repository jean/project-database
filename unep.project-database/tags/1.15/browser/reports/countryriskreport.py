from Products.ProjectDatabase.reports.CountryRiskReportFactory \
    import CountryRiskReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class CountryRiskReport(BaseReport):
    def getReport(self):
        factory = CountryRiskReportFactory(self.context, projects=self._projects)
        return factory.getReport()
