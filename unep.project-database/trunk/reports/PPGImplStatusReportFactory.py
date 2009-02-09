from Report import Report

class PPGImplementationStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('PPG Implementation Status Report')
        report.setReportHeaders((
            'PPG Implementation Status Report',
            ),)
        report.setTableHeaders(((
            'IMIS No.',
            'Project Title',
            'Executing Agency',
            'Start Date',
            'Expected Completion Date',
            'Revised Completion Date',
            'GEF Amount',
            'Total Disbursements',
            'Total Expenditures',
            'Last Expenditure Report',
            'Last Progress Report',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            ppg = project.fmi_folder.getattr('ppg', None)
            if ppg is not None:
                result.append((
                    ppg.getIMISNumber(),
                    project.Title(),
                    project.project_general_info.getExecutingAgencyNames(),
                    'Unknown',
                    ppg.getExpectedCompletionDate(),
                    ppg.getRevisedCompletionDate(),
                    ppg.getSumFinanceObjectAmount(),
                    ppg.getSumCashDisbursements(),
                    ppg.getSumYearlyExpenditures(),
                    ppg.getTotalGEFAmount(),
                    ppg.getLatestReportData('expenditure', 'report_received_date'),
                    ppg.getLatestReportData('progress', 'report_received_date'),
                    ))
        return result



