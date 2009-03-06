from Products.ProjectDatabase.reports.EEAReceivablesReportFactory import EEAReceivablesReportFactory
from basereport import BaseReport

class EEAReceivablesReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = EEAReceivablesReportFactory(self.context, projects=projects)
        return factory.getReport()
