from Report import Report
from Products.ProjectDatabase.utils import inner_strip

class CancelledProjectsReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('Cancelled Projects Report')
        report.setReportHeaders((
            'Cancelled Projects Report',
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
            'Cancellation Date',
            'Reason',
            'Actual Expenditures',
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
                    ms.getProjectImplementationDate('Cancellation'):
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
                    ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual'),
                    ms.getProjectImplementationDate('Cancellation'),
                    mofu.getFinancialStatusRemarks(),
                    pgi.getTotalYearlyExpenditures()
                    ))
        return result
