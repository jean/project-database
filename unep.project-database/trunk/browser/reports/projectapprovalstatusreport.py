from Products.ProjectDatabase.reports.ProjectApprovalStatusReportFactory \
    import ProjectApprovalStatusReportFactory
from basereport import BaseReport

class ProjectApprovalStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = ProjectApprovalStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
