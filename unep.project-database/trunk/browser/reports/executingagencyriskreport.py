from Products.ProjectDatabase.reports.ExecutingAgencyRiskReportFactory \
    import ExecutingAgencyRiskReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ExecutingAgencyRiskReport(BaseReport):
    def getReport(self):
        factory = ExecutingAgencyRiskReportFactory(self.context, projects=self.projects)
        return factory.getReport()
