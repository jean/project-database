from Products.ProjectDatabase.reports.MidTermEvaluationStatusReportFactory \
    import MidTermEvaluationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class MidTermEvaluationStatusReport(BaseReport):
    def getReport(self):
        factory = MidTermEvaluationStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
