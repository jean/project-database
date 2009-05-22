from Products.ProjectDatabase.reports.ProgrammeFrameworkReportFactory \
    import ProgrammeFrameworkReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProgrammeFrameworkReport(BaseReport):
    def getReport(self):
        factory = ProgrammeFrameworkReportFactory(self.context)
        return factory.getReport()
