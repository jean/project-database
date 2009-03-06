from Products.ProjectDatabase.reports.PPGAprAndImplStatusRepFactory import PPGApprovalAndImplementationStatusReportFactory
from basereport import BaseReport

class PPGApprovalAndImplementationStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = PPGApprovalAndImplementationStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
