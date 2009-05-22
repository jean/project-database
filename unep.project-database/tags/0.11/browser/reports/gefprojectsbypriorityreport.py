from Products.ProjectDatabase.reports.GefProjectsByPriorityReportFactory \
    import GefProjectsByPriorityReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class GefProjectsByPriorityReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = GefProjectsByPriorityReportFactory(self.context, projects=projects)
        return factory.getReport()
