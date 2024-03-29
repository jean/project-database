from Report import Report

class ProjectsDueForClosureReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Projects Due for Closure"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'IMIS No.',
            'Project Title',
            'Finance Object',
            'Actual Completion Date',
            'Outputs',
            'Terminal report',
            'Final Expenditure report',
            'Audit report',
            'Inventory',
            'Co-financing report',
            'Terminal Evaluation',
            ),))
        # XXX Implement this
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

            for fo in project.fmi_folder.getAllFinanceObjects():

                if fo.getFinanceCategory() == 'ppg' and \
                        project.milestones.getPPGImplementationDate('CompletionActual') and \
                        not project.milestones.getPPGImplementationDate('ClosureActual'):

                    result.append((
                        fo.getIMISNumber(),
                        project.project_general_info.Title(),
                        fo.getId(),
                        project.milestones.getPPGImplementationDate('CompletionActual'),
                        'Unknown',
                        fo.getLatestReportData('terminal', 'report_received_date'),
                        fo.getLatestReportData('expenditure', 'report_received_date'),
                        fo.getLatestReportData('audit', 'report_received_date'),
                        fo.getLatestReportData('inventory', 'report_received_date'),
                        fo.getLatestReportData('cofinance', 'report_received_date'),
                        project.milestones.getEvaluationDatesDate('TerminalEvaluationActual')
                        ))

                elif fo.getFinanceCategory() in ['eea', 'fsp', 'msp'] and \
                        project.milestones.getProjectImplementationDate('CompletionActual') and \
                        not project.milestones.getProjectImplementationDate('ClosureActual'):
                    result.append((
                        fo.getIMISNumber(),
                        project.project_general_info.Title(),
                        fo.getId(),
                        project.milestones.getProjectImplementationDate('CompletionActual'),
                        'Unknown',
                        fo.getLatestReportData('terminal', 'report_received_date'),
                        fo.getLatestReportData('expenditure', 'report_received_date'),
                        fo.getLatestReportData('audit', 'report_received_date'),
                        fo.getLatestReportData('inventory', 'report_received_date'),
                        fo.getLatestReportData('cofinance', 'report_received_date'),
                        project.milestones.getEvaluationDatesDate('TerminalEvaluationActual')
                        ))

                elif fo.getFinanceCategory() in ['phase', 'addon', 'tranche'] and \
                        project.milestones.getNewPhaseImplementationDate('Completion') and \
                        not project.milestones.getNewPhaseImplementationDate('Closure'):
                    result.append((
                        fo.getIMISNumber(),
                        project.project_general_info.Title(),
                        fo.getId(),
                        project.milestones.getNewPhaseImplementationDate('Completion'),
                        'Unknown',
                        fo.getLatestReportData('terminal', 'report_received_date'),
                        fo.getLatestReportData('expenditure', 'report_received_date'),
                        fo.getLatestReportData('audit', 'report_received_date'),
                        fo.getLatestReportData('inventory', 'report_received_date'),
                        fo.getLatestReportData('cofinance', 'report_received_date'),
                        project.milestones.getEvaluationDatesDate('TerminalEvaluationActual')
                        ))

        return result
