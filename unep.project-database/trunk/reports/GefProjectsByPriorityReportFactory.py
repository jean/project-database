from Report import Report
from Products.ProjectDatabase.utils import \
        inner_strip, amount2millions, unep_report_format_date, getVocabularyValue

class GefProjectsByPriorityReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "GEF Projects by Priority Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'MTS priority',
            'Project title',
            'Focal Area',
            'Task Manager',
            'Mode of execution',
            'Division',
            'Status',
            'GEF amount',
            ),))
        #        
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []

        for project in projects:
            pgi = project.project_general_info
            mofu = project.fmi_folder.getMainFinanceObject()
            if project.isTheProjectPublished():
                mofu_Status = 'Unspecified'
                if mofu is not None:
                    mofu_Status = getVocabularyValue(self.context,
                            'Status', mofu.getStatus())

                result.append((
                    ', '.join([getVocabularyValue(self.context, \
                            'UNEPThematicPriority', priority) \
                            for priority in pgi.getUNEPThematicPriority()]),
                    pgi.Title(),
                    pgi.getFocalAreaNames(),
                    pgi.getCurrentTM(),
                    getVocabularyValue(self.context, \
                            'ExecutionMode', pgi.getExecutionMode()),
                    getVocabularyValue(self.context, \
                            'Division', pgi.getLeadDivision()),
                    mofu_Status,
                    inner_strip(project.getTotalGEFAmount()),
                ))
        return result 
