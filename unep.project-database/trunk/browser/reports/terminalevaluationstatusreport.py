from Products.ProjectDatabase.reports.TerminalEvaluationStatusReportFactory \
    import TerminalEvaluationStatusReportFactory
from basereport import BaseReport

class TerminalEvaluationStatusReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = TerminalEvaluationStatusReportFactory(self.context, projects=projects)
        return factory.getReport()
