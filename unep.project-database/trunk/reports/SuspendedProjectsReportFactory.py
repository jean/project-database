from Report import Report
from Products.ProjectDatabase.utils import inner_strip, unep_report_format_date

class SuspendedProjectsReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('Suspended Projects Report')
        report.setReportHeaders((
            'Suspended Projects Report',
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
            'Suspension Date',
            'Reason',
            'Expected Date of Resuming Activities',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            mofu = project.fmi_folder.getMainFinanceObject()
            ms = project.milestones
            pgi = project.project_general_info
            if mofu and project.isTheProjectPublished() and \
                    not ms.getProjectImplementationDate('Cancellation') and \
                    not ms.getProjectImplementationDate('Termination') and \
                    ms.getProjectImplementationDate('Suspension') and \
                    not ms.getProjectImplementationDate('Reinitiation'):
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
                        ms.getProjectImplementationDate('Suspension')),
                    unep_report_format_date(self.projectdatabase, \
                        mofu.getFinancialStatusRemarks()),
                    unep_report_format_date(self.projectdatabase, \
                        ms.getProjectImplementationDate('Reinitiation')),
                    ))
        return result
