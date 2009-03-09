from Products.ProjectDatabase.reports.CountryRiskReportFactory \
    import CountryRiskReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class CountryRiskReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = CountryRiskReportFactory(self.context, projects=projects)
        return factory.getReport()
