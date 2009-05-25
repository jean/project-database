from Products.ProjectDatabase.reports.ProjectCycleStageStatusReportFactory \
    import ProjectCycleStageStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectCycleStageStatusReport(BaseReport):
    def getReport(self):
        factory = ProjectCycleStageStatusReportFactory(self.context, projects=self._projects)
        return factory.getReport()
