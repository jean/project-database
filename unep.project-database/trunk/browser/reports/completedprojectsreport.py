from Products.ProjectDatabase.reports.CompletedProjectsReportFactory \
    import CompletedProjectsReportFactory
from basereport import BaseReport

class CompletedProjectsReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = CompletedProjectsReportFactory(self.context, projects=projects)
        return factory.getReport()
