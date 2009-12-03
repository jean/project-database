from Products.ProjectDatabase.reports.TerminalEvaluationStatusReportFactory \
    import TerminalEvaluationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class TerminalEvaluationStatusReport(BaseReport):
    def getReport(self):
        factory = TerminalEvaluationStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
