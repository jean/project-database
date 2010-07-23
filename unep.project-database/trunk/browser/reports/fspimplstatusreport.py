from Products.ProjectDatabase.reports.FSPImplStatusReportFactory \
    import FSPImplementationStatusReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class FSPImplStatusReport(BaseReport):
    def getReport(self):
        # Not sure that the UIDs thing is still necessary.
        # Refactor this to look like most of the other reports here.
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            rc = getToolByName(self, 'reference_catalog')
            UIDs = UIDs.split('|')
            self._projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = FSPImplementationStatusReportFactory(self.context, 
                projects=self._projects)
        return factory.getReport()
