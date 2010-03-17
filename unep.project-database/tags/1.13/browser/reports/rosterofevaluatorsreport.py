from Products.ProjectDatabase.reports.RosterOfEvaluatorsReportFactory \
    import RosterOfEvaluatorsReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class RosterOfEvaluatorsReport(BaseReport):
    def getReport(self):
        factory = RosterOfEvaluatorsReportFactory(self.context, projects=self._projects)
        return factory.getReport()
