from Report import Report

class MidTermReviewStatusReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Mid-term Review Status Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'IMIS No.',
            'Project title',
            'Focal area',
            'Review budget',
            'TM',
            'FMO',
            'MTR Status',
            'Lead Consultant',
            'email',
            'Phone No.',
            'Other Consultants',
            'Project Rating',
            ),))
        # XXX Implement this
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        # for project in projects:

        #     for me in project.bbb:

        #         if fo.getFinanceCategory() == 'ppg' and \
        #                 project.milestones.getPPGImplementationDates('CompletionActual') and \
        #                 not project.milestones.getPPGImplementationDates('ClosureActual'):
        #             result.append((
        #                 fo.getIMISNumber(),
        #                 project.project_general_info.Title(),
        #                 fo.getId(),
        #                 project.milestones.getPPGImplementationDates('CompletionActual'),
        #                 'Unknown',
        #                 fo.getLatestReportData('terminal', 'report_received_date'),
        #                 fo.getLatestReportData('expenditure', 'report_received_date'),
        #                 fo.getLatestReportData('audit', 'report_received_date'),
        #                 fo.getLatestReportData('inventory', 'report_received_date'),
        #                 fo.getLatestReportData('cofinance', 'report_received_date'),
        #                 project.milestones.getEvaluationDatesDate('TerminalEvaluationActual')
        #                 ))

        #         elif fo.getFinanceCategory() in ['eea', 'fsp', 'msp'] and \
        #                 project.milestones.getProjectImplementationDates('CompletionActual') and \
        #                 not project.milestones.getProjectImplementationDates('ClosureActual'):
        #             result.append((
        #                 fo.getIMISNumber(),
        #                 project.project_general_info.Title(),
        #                 fo.getId(),
        #                 project.milestones.getProjectImplementationDates('CompletionActual'),
        #                 'Unknown',
        #                 fo.getLatestReportData('terminal', 'report_received_date'),
        #                 fo.getLatestReportData('expenditure', 'report_received_date'),
        #                 fo.getLatestReportData('audit', 'report_received_date'),
        #                 fo.getLatestReportData('inventory', 'report_received_date'),
        #                 fo.getLatestReportData('cofinance', 'report_received_date'),
        #                 project.milestones.getEvaluationDatesDate('TerminalEvaluationActual')
        #                 ))

        #         elif fo.getFinanceCategory() in ['phase', 'addon', 'tranche'] and \
        #                 project.milestones.getNewPhaseImplementationDate('Completion') and \
        #                 not project.milestones.getNewPhaseImplementationDate('Closure'):
        #             result.append((
        #                 fo.getIMISNumber(),
        #                 project.project_general_info.Title(),
        #                 fo.getId(),
        #                 project.milestones.getNewPhaseImplementationDate('Completion'),
        #                 'Unknown',
        #                 fo.getLatestReportData('terminal', 'report_received_date'),
        #                 fo.getLatestReportData('expenditure', 'report_received_date'),
        #                 fo.getLatestReportData('audit', 'report_received_date'),
        #                 fo.getLatestReportData('inventory', 'report_received_date'),
        #                 fo.getLatestReportData('cofinance', 'report_received_date'),
        #                 project.milestones.getEvaluationDatesDate('TerminalEvaluationActual')
        #                 ))

        return result
