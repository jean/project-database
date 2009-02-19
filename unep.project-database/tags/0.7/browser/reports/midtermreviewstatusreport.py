from Products.ProjectDatabase.reports.MidTermReviewStatusReportFactory \
    import MidTermReviewStatusReportFactory
from basereport import BaseReport

class MidTermReviewStatusReport(BaseReport):
    def getReport(self):
        factory = MidTermReviewStatusReportFactory(self.context)
        return factory.getReport()
