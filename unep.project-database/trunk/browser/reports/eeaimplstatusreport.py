from Products.ProjectDatabase.reports.EEAImplStatusReportFactory \
    import EEAImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class EEAImplStatusReport(BaseReport):
    def getReport(self):
        factory = EEAImplementationStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
