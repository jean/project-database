from Products.ProjectDatabase.reports.TerminalEvaluationStatusReportFactory \
    import TerminalEvaluationStatusReportFactory
from basereport import BaseReport

class TerminalEvaluationStatusReport(BaseReport):
    def getReport(self):
        factory = TerminalEvaluationStatusReportFactory(self.context)
        return factory.getReport()
