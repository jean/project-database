from Products.ProjectDatabase.reports.TerminalEvaluationsComingUpReportFactory \
    import TerminalEvaluationsComingUpReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class TerminalEvaluationsComingUpReport(BaseReport):
    def getReport(self):
        factory = TerminalEvaluationsComingUpReportFactory(self.context, projects=self._projects)
        return factory.getReport()
