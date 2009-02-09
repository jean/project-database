from Products.ProjectDatabase.reports.PPGAprAndImplStatusRepFactory import PPGApprovalAndImplementationStatusReportFactory
from basereport import BaseReport

class PPGApprovalAndImplementaionStatusReport(BaseReport):
    def getReport(self):
        factory = PPGApprovalAndImplementationStatusReportFactory(self.context)
        return factory.getReport()
