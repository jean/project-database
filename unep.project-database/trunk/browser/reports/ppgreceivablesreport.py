from Products.ProjectDatabase.reports.PPGReceivablesReportFactory import PPGReceivablesReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class PPGReceivablesReport(BaseReport):
    def getReport(self):
        # We probably don't need this anymore, but I'm keeping it here
        # _just-in-case_
        # Next time you refactor me please pull me inline with the rest
        # of me reporting brethren.
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            rc = getToolByName(self, 'reference_catalog')
            UIDs = UIDs.split('|')
            self._projects = [rc.lookupObject(UID) for UID in UIDs]

        # This is what most of the other reports do. 
        factory = PPGReceivablesReportFactory(self.context, 
                projects=self._projects)
        return factory.getReport()
