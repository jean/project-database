from Products.ProjectDatabase.reports.RosterOfEvaluatorsReportFactory \
    import RosterOfEvaluatorsReportFactory
from basereport import BaseReport

class RosterOfEvaluatorsReport(BaseReport):
    def getReport(self):
        factory = RosterOfEvaluatorsReportFactory(self.context)
        return factory.getReport()
