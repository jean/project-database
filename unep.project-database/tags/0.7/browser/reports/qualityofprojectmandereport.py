from Products.ProjectDatabase.reports.QualityOfProjectMandEReportFactory \
    import QualityOfProjectMandEReportFactory
from basereport import BaseReport

class QualityOfProjectMandEReport(BaseReport):
    def getReport(self):
        factory = QualityOfProjectMandEReportFactory(self.context)
        return factory.getReport()
