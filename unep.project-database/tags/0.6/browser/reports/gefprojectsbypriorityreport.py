from Products.ProjectDatabase.reports.GefProjectsByPriorityReportFactory \
    import GefProjectsByPriorityReportFactory
from basereport import BaseReport

class GefProjectsByPriorityReport(BaseReport):
    def getReport(self):
        factory = GefProjectsByPriorityReportFactory(self.context)
        return factory.getReport()
