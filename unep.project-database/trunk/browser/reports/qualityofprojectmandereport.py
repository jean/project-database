from Products.ProjectDatabase.reports.QualityOfProjectMandEReportFactory \
    import QualityOfProjectMandEReportFactory
from basereport import BaseReport

class QualityOfProjectMandEReport(BaseReport):
    def getReport(self):
        rc = getToolByName(self, 'reference_catalog')
        projects = []
        UIDs = self.context.REQUEST.get('projects', None)
        if UIDs:
            UIDs = UIDs.split('|')
            projects = [rc.lookupObject(UID) for UID in UIDs]
        factory = QualityOfProjectMandEReportFactory(self.context, projects=projects)
        return factory.getReport()
