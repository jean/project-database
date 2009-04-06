from Products.ProjectDatabase.reports.xxxzFactory \
    import xxxzFactory
from basereport import BaseReport

class xxxz(BaseReport):
    def getReport(self):
        factory = xxxzFactory(self.context)
        return factory.getReport()
