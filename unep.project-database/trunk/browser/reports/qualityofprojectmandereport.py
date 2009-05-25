from Products.ProjectDatabase.reports.QualityOfProjectMandEReportFactory \
    import QualityOfProjectMandEReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class QualityOfProjectMandEReport(BaseReport):
    def getReport(self):
        factory = QualityOfProjectMandEReportFactory(self.context, projects=self._projects)
        return factory.getReport()
