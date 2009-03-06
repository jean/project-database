from Products.ProjectDatabase.reports.ProjectsDueForClosureReportFactory \
    import ProjectsDueForClosureReportFactory
from basereport import BaseReport

class ProjectsDueForClosureReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = ProjectsDueForClosureReportFactory(self.context, projects=projects)
        return factory.getReport()
