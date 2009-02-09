from Report import Report

class ProjectsDueForClosureReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
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
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:

            for fo in project.fmi_folder:

                if fo.getFinanceCategory() == 'ppg' and \
                        project.milestones.getPPGImplementationDates('CompletionActual') and \
                        not project.milestones.getPPGImplementationDates('ClosureActual'):
                    result.append((
                        fo.getIMISNumber(),
                        project.Title(),
                        fo.getId(),
                        project.milestones.getPPGImplementationDates('CompletionActual'),
                        'Unknown',
                        fo.getLatestReportData('terminal', 'report_received_date'),
                        fo.getLatestReportData('expenditure', 'report_received_date'),
                        fo.getLatestReportData('audit', 'report_received_date'),
                        fo.getLatestReportData('inventory', 'report_received_date'),
                        fo.getLatestReportData('cofinance', 'report_received_date'),
                        project.milestones.getEvaluationDatesDate('TerminalEvaluationActual')
                        ))

                elif fo.getFinanceCategory() in ['eea', 'fsp', 'msp'] and \
                        project.milestones.getProjectImplementationDates('CompletionActual') and \
                        not project.milestones.getProjectImplementationDates('ClosureActual'):
                    result.append((
                        fo.getIMISNumber(),
                        project.Title(),
                        fo.getId(),
                        project.milestones.getProjectImplementationDates('CompletionActual'),
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
                        project.Title(),
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
