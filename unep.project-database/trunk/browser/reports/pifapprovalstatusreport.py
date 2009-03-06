from Products.ProjectDatabase.reports.PIFApprovalStatusReportFactory \
        import PIFApprovalStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class PIFApprovalStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = PIFApprovalStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
