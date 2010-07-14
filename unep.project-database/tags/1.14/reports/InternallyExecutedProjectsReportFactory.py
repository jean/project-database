from Report import Report
from Products.ProjectDatabase.utils import \
        inner_strip, getVocabularyValue

class InternallyExecutedProjectsReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Internally Executed Projects Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Division',
            'Project title',
            'Focal Area',
            'Status',
            'GEF amount',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        result = []

        for project in projects:
            pgi = project.project_general_info
            if pgi.getExecutionMode() == 'Internal':
                mofu = project.fmi_folder.getMainFinanceObject()
                if project.isTheProjectPublished():
                    mofu_Status = 'Unspecified'
                    if mofu is not None:
                        mofu_Status = getVocabularyValue(self.context,
                                'Status', mofu.getStatus())
                    result.append((
                        getVocabularyValue(self.context, \
                                'Division', pgi.getLeadDivision()),
                        pgi.Title(),
                        pgi.getFocalAreaNames(),
                        mofu_Status,
                        inner_strip(project.getTotalGEFAmount()),
                    ))
        return result 
