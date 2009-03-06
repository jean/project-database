from Products.ProjectDatabase.reports.MSPImplStatusReportFactory \
    import MSPImplementationStatusReportFactory
from basereport import BaseReport

class MSPImplStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = MSPImplementationStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
