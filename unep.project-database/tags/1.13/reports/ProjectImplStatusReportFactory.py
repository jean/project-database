from Report import Report
from Products.ProjectDatabase.utils import inner_strip, unep_report_format_date

class ProjectImplementationStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('Project Implementation Status Report')
        report.setReportHeaders((
            'Project Implementation Status Report',
            ),)
        report.setTableHeaders(((
            'Dbase ID.',
            'GEF ID',
            'IMIS No.',
            'Focal Area',
            'Project Type',
            'Geographic Scope',
            'Country(ies)',
            'Project Title',
            'Total GEF Amount',
            'UNEP GEF Amount',
            'UNEP Fee',
            'Signature',
            'Mid-term Review',
            'Last Revision Date',
            'Expected Completion',
            'Revised Completion',
            'Terminal Evaluation',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        result = []
        projects = self.params.get('projects', None)
        for project in projects:
            mofu = project.fmi_folder.getMainFinanceObject()
            ms = project.milestones
            pgi = project.project_general_info
            if mofu and project.isTheProjectPublished() and \
                    ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual') and \
                    not ms.getProjectImplementationDate('CompletionActual') and \
                    not ms.getProjectImplementationDate('ClosureActual') and \
                    not ms.getProjectImplementationDate('Cancellation') and \
                    not ms.getProjectImplementationDate('Termination'):
                result.append((
                    project.getId(),
                    pgi.getGEFid(),
                    mofu.getIMISNumber(),
                    pgi.getFocalAreaNames(),
                    pgi.getProjectTypeName(),
                    pgi.getGeographicScopeValues(),
                    pgi.getCountryNames(),
                    pgi.Title(),
                    inner_strip(project.getTotalGEFAmount()),
                    inner_strip(project.getTotalUNEPGEFAmount()),
                    inner_strip(project.getTotalUNEPFee()),
                    unep_report_format_date(self.projectdatabase, \
                        ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual')),
                    unep_report_format_date(self.projectdatabase, \
                        ms.getEvaluationDatesDate('MTERactual')),
                    unep_report_format_date(self.projectdatabase, \
                        mofu.getLastestRevisionDate()),
                    unep_report_format_date(self.projectdatabase, \
                        ms.getProjectImplementationDate('CompletionExpected')),
                    unep_report_format_date(self.projectdatabase, \
                        ms.getProjectImplementationDate('CompletionRevised')),
                    unep_report_format_date(self.projectdatabase, \
                        ms.getEvaluationDatesDate('TerminalEvaluationActual')),
                    ))
        return result
