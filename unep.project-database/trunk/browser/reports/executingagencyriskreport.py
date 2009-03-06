from Products.ProjectDatabase.reports.ExecutingAgencyRiskReportFactory \
    import ExecutingAgencyRiskReportFactory
from basereport import BaseReport

class ExecutingAgencyRiskReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = ExecutingAgencyRiskReportFactory(self.context, projects=projects)
        return factory.getReport()
