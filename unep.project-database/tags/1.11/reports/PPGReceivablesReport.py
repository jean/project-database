from Report import Report

class PPGReceivablesReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('PPG Recievables Report')
        report.setReportHeaders((
            'PPG Recievables Report',
            ),)
        report.setTableHeaders(((
            'IMIS No.',
            'Project Title',
            'Executing Agency',
            'GEF Grant',
            'Total Disbursements',
            'Total Expenditures',
            'Receivable/(Payable)',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        result = []
        for project in projects:
            ppg = project.fmi_folder.get('ppg', None)
            if ppg is not None:
                result.append((
                    ppg.getIMISNumber(),
                    project.project_general_info.Title(),
                    project.project_general_info.getLeadExecutingAgencyNames(),
                    ppg.getCommittedGEFGrant(),
                    ppg.getSumCashDisbursements(),
                    ppg.getSumYearlyExpenditures(),
                    ppg.getAmountReceivable(),
                    ))
        return result
