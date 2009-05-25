from Products.ProjectDatabase.reports.DonorReportFactory \
    import DonorReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class DonorReport(BaseReport):
    def getReport(self):
        factory = DonorReportFactory(self.context, projects=self._projects)
        return factory.getReport()
