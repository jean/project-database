from Products.ProjectDatabase.reports.KeyMilestonesReportFactory \
    import KeyMilestonesReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class KeyMilestonesReport(BaseReport):

    def getReport(self):
        factory = KeyMilestonesReportFactory(self.context)
        return factory.getReport()
