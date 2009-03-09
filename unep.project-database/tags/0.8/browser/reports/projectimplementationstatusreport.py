from Products.ProjectDatabase.reports.ProjectImplStatusReportFactory \
    import ProjectImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectImplementationStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = ProjectImplementationStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
