from Products.ProjectDatabase.reports.RosterOfEvaluatorsReportFactory \
    import RosterOfEvaluatorsReportFactory
from basereport import BaseReport

class RosterOfEvaluatorsReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = RosterOfEvaluatorsReportFactory(self.context, projects=projects)
        return factory.getReport()
