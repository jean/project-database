from Products.ProjectDatabase.reports.PPGAprAndImplStatusRepFactory import PPGApprovalAndImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class PPGApprovalAndImplementationStatusReport(BaseReport):
    def getReport(self):
        factory = PPGApprovalAndImplementationStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
