from Products.ProjectDatabase.reports.FSPImplStatusReportFactory \
    import FSPImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class FSPImplStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = FSPImplementationStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
