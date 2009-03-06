from Products.ProjectDatabase.reports.ProjectsByExecutingAgencyReportFactory \
    import ProjectsByExecutingAgencyReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectsByExecutingAgencyReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = ProjectsByExecutingAgencyReportFactory(self.context, projects=projects)
        return factory.getReport()
