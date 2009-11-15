from Products.ProjectDatabase.reports.MidTermEvaluationsComingUpReportFactory \
    import MidTermEvaluationsComingUpReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class MidTermEvaluationsComingUpReport(BaseReport):
    def getReport(self):
        factory = MidTermEvaluationsComingUpReportFactory(self.context, projects=self._projects)
        return factory.getReport()
