from Products.ProjectDatabase.reports.FSPReceivablesReportFactory import FSPReceivablesReportFactory
from basereport import BaseReport
from Products.CMFCore.utils import getToolByName

class FSPReceivablesReport(BaseReport):
    def getReport(self):
        # Since this is an FSP report and FSP finance objects can contain
        # subprojects, we extend the _projects property with those.
        projects = []
        for project in self._projects:
            fmi = project.getFMIFolder()
            if 'fsp' in fmi.objectIds():
                projects.append(project)
                sub_projects = fmi.getFspSubProjects()
                projects.extend(sub_projects)
        self._projects = projects
        factory = FSPReceivablesReportFactory(self.context, projects=self._projects)
        return factory.getReport()
