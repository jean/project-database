from Products.ProjectDatabase.reports.qoterrplReportFactory \
    import qoterrplReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class qoterrplReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = qoterrplReportFactory(self.context, projects=projects)
        return factory.getReport()
