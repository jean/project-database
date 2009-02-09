from Report import Report

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
            if project.milestones.getProjectImplementationDate('Cancellation'):
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    'Unknown IMIS No',
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getProjectTypeName(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.Title(),
                    project.getTotalGEFAmount(),
                    project.getTotalUNEPGEFAmount(),
                    project.getTotalUNEPFee(),
                    project.milestones.getProjectImplementationDate('SignatureOfLegalInstrumentActual'),
                    project.milestones.getProjectImplementationDate('Cancellation'),
                    'Unknown reason',
                    project.project_general_info.getTotalYearlyExpenditures()
                    ))
        return result
