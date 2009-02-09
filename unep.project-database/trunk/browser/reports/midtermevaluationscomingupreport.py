from Products.ProjectDatabase.reports.MidTermEvaluationsComingUpReportFactory \
    import MidTermEvaluationsComingUpReportFactory
from basereport import BaseReport

class MidTermEvaluationsComingUpReport(BaseReport):
    def getReport(self):
        factory = MidTermEvaluationsComingUpReportFactory(self.context)
        return factory.getReport()
