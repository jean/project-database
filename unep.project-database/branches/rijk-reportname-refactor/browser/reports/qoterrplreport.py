from Products.ProjectDatabase.reports.qoterrplReportFactory \
    import qoterrplReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class qoterrplReport(BaseReport):
    def getReport(self):
        factory = qoterrplReportFactory(self.context, projects=self._projects)
        return factory.getReport()
