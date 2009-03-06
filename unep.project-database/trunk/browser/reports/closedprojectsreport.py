from Products.ProjectDatabase.reports.ClosedProjectsReportFactory \
    import ClosedProjectsReportFactory
from basereport import BaseReport

class ClosedProjectsReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = ClosedProjectsReportFactory(self.context, projects=projects)
        return factory.getReport()
