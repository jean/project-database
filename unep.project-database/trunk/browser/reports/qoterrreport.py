from Products.ProjectDatabase.reports.qoterrReportFactory \
    import qoterrReportFactory
from basereport import BaseReport
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class qoterrReport(BaseReport):
    def getReport(self):
        factory = qoterrReportFactory(self.context)
        return factory.getReport()
