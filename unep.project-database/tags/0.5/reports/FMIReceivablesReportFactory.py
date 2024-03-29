from Report import Report

class FMIReceivablesReportFactory(object):

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
            'GEF Grant',
            'Total Disbursements',
            'Total Expenditures',
            'Receivable/ (Payable)',
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
                    ob.getCommittedGEFGrant(),
                    ob.getSumCashDisbursements(),
                    ob.getSumYearlyExpenditures(),
                    ob.getAmountReceivable(),
                    ))
        return result

