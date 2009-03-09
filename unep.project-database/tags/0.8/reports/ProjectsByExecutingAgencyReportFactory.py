from Report import Report
from Products.ProjectDatabase.utils import \
        inner_strip, getVocabularyValue

class ProjectsByExecutingAgencyReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Projects By Executing Agency Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Executing agency',
            'Project Title',
            'Status',
            'Focal Area',
            'GEF amount',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        if projects is None:
            projects = self.context.objectValues(spec='Project')
        result = []

        for project in projects:
            pgi = project.project_general_info
            if pgi.getExecutionMode() == 'External':
                mofu = project.fmi_folder.getMainFinanceObject()
                if project.isTheProjectPublished():
                    result.append((
                        pgi.getLeadExecutingAgencyNames(),
                        pgi.Title(),
                        getVocabularyValue(self.context, \
                                'Status', mofu.getStatus()),
                        pgi.getFocalAreaNames(),
                        inner_strip(project.getTotalGEFAmount()),
                    ))
        return result 
