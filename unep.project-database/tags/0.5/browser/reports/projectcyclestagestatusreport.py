from Products.ProjectDatabase.reports.ProjectCycleStageStatusReportFactory \
    import ProjectCycleStageStatusReportFactory
from basereport import BaseReport

class ProjectCycleStageStatusReport(BaseReport):
    def getReport(self):
        factory = ProjectCycleStageStatusReportFactory(self.context)
        return factory.getReport()
