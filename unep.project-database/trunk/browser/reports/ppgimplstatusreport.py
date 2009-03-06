from Products.ProjectDatabase.reports.PPGImplStatusReportFactory \
    import PPGImplementationStatusReportFactory
from basereport import BaseReport

class PPGImplStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = PPGImplementationStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
