from Products.ProjectDatabase.reports.PIFApprovalStatusReportFactory \
        import PIFApprovalStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class PIFApprovalStatusReport(BaseReport):
    def getReport(self):
        factory = PIFApprovalStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
