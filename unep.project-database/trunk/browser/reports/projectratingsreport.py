from Products.ProjectDatabase.reports.ProjectRatingsReportFactory \
    import ProjectRatingsReportFactory
from basereport import BaseReport
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class ProjectRatingsReport(BaseReport):
    def getReport(self):
        factory = ProjectRatingsReportFactory(self.context)
        return factory.getReport()
