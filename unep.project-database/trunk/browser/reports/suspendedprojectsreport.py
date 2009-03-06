from Products.ProjectDatabase.reports.SuspendedProjectsReportFactory \
    import SuspendedProjectsReportFactory
from basereport import BaseReport

class SuspendedProjectsReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = SuspendedProjectsReportFactory(self.context, projects=projects)
        return factory.getReport()
