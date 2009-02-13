from Products.ProjectDatabase.reports.TerminalEvaluationsComingUpReportFactory \
    import TerminalEvaluationsComingUpReportFactory
from basereport import BaseReport

class TerminalEvaluationsComingUpReport(BaseReport):
    def getReport(self):
        factory = TerminalEvaluationsComingUpReportFactory(self.context)
        return factory.getReport()
