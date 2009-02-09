from Products.ProjectDatabase.reports.ProductRatingsReportFactory \
    import ProductRatingsReportFactory
from basereport import BaseReport

class ProductRatingsReport(BaseReport):
    def getReport(self):
        factory = ProductRatingsReportFactory(self.context)
        return factory.getReport()
