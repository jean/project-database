from Products.ProjectDatabase.reports.MidTermReviewStatusReportFactory \
    import MidTermReviewStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class MidTermReviewStatusReport(BaseReport):
    def getReport(self):
        factory = MidTermReviewStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
