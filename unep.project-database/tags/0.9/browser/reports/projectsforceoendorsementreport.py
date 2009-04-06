from Products.ProjectDatabase.reports.ProjectsForCEOEndorsementReportFactory \
    import ProjectsForCEOEndorsementReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class ProjectsForCEOEndorsementReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = ProjectsForCEOEndorsementReportFactory(self.context, projects=projects)
        return factory.getReport()
