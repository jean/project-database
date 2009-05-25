from Products.ProjectDatabase.reports.PPGImplStatusReportFactory \
    import PPGImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class PPGImplStatusReport(BaseReport):
    def getReport(self):
        factory = PPGImplementationStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
