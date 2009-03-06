from Products.ProjectDatabase.reports.FSPReceivablesReportFactory import FSPReceivablesReportFactory
from basereport import BaseReport

class FSPReceivablesReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = FSPReceivablesReportFactory(self.context, projects=projects)
        return factory.getReport()
