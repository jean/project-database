from Products.ProjectDatabase.reports.PIFApprovalStatusReportFactory \
        import PIFApprovalStatusReportFactory
from basereport import BaseReport

class PIFApprovalStatusReport(BaseReport):
    def getReport(self):
        factory = PIFApprovalStatusReportFactory(self.context)
        return factory.getReport()
