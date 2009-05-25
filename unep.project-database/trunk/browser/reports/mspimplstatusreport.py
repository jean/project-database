from Products.ProjectDatabase.reports.MSPImplStatusReportFactory \
    import MSPImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class MSPImplStatusReport(BaseReport):
    def getReport(self):
        factory = MSPImplementationStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
