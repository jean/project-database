from Products.ProjectDatabase.reports.MidTermEvaluationStatusReportFactory \
    import MidTermEvaluationStatusReportFactory
from basereport import BaseReport

class MidTermEvaluationStatusReport(BaseReport):
    def getReport(self):
        factory = MidTermEvaluationStatusReportFactory(self.context)
        return factory.getReport()
