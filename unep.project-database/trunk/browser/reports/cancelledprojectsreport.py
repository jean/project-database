from Products.ProjectDatabase.reports.CancelledProjectsReportFactory \
    import CancelledProjectsReportFactory
from basereport import BaseReport

class CancelledProjectsReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = CancelledProjectsReportFactory(self.context, projects=projects)
        return factory.getReport()
