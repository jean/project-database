from Report import Report
from Products.ProjectDatabase.utils import inner_strip, unep_report_format_date

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
            pgi = project.project_general_info
            ms = project.milestones
            if type == 'ppg':
                start_date = ms.getPPGImplementationDate('SignatureOfLegalInstrumentActual')
            else:
                start_date = ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual')
            if ob is not None:
                result.append((
                    ob.getIMISNumber(),
                    pgi.Title(),
                    pgi.getExecutingAgencyNames(),
                    unep_report_format_date(
                        self.projectdatabase,
                        start_date),
                    unep_report_format_date(
                        self.projectdatabase,
                        ob.getExpectedCompletionDate()),
                    unep_report_format_date(
                        self.projectdatabase,
                        ob.getRevisedCompletionDate()),
                    inner_strip(ob.getTotalGEFAmount()),
                    inner_strip(ob.getSumCashDisbursements()),
                    inner_strip(ob.getSumYearlyExpenditures()),
                    unep_report_format_date(
                        self.projectdatabase,
                        ob.getLatestReportData(
                            'expenditure', 'report_received_date')),
                    unep_report_format_date(
                        self.projectdatabase,
                        ob.getLatestReportData(
                            'progress', 'report_received_date')),
                    ))
        return result
