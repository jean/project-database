from Report import Report

class FMIImplementationStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self, name, type):
        # create and fill the report
        report = Report(name)
        report.setReportHeaders(( name,),)
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
        report.setTableRows(self.getReportData(type))
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self, type):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            ob = project.fmi_folder.get(type, None)
            if ob is not None:
                result.append((
                    ob.getIMISNumber(),
                    project.Title(),
                    project.project_general_info.getExecutingAgencyNames(),
                    'Unknown',
                    ob.getExpectedCompletionDate(),
                    ob.getRevisedCompletionDate(),
                    ob.getSumFinanceObjectAmount(),
                    ob.getSumCashDisbursements(),
                    ob.getSumYearlyExpenditures(),
                    ob.getTotalGEFAmount(),
                    ob.getLatestReportData('expenditure', 'report_received_date'),
                    ob.getLatestReportData('progress', 'report_received_date'),
                    ))
        return result
