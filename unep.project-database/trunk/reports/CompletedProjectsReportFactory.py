from Report import Report

class CompletedProjectsReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('Completed Projects Report')
        report.setReportHeaders((
            'Completed Projects Report',
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
            'Mid-term Review',
            'Last Revision Date',
            'Actual Completion',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            pgi = project.project_general_info
            ms = project.milestones
            mofu = project.fmi_folder.getMainFinanceObject()

            if mofu and project.isTheProjectPublished() and \
                ms.getProjectImplementationDate('CompletionActual'):
                result.append((
                    project.getId(),
                    pgi.getGEFid(),
                    mofu.getIMISNumber(),
                    pgi.getFocalAreaNames(),
                    pgi.getProjectTypeName(),
                    pgi.getGeographicScopeValues(),
                    pgi.getCountryNames(),
                    pgi.Title(),
                    project.getTotalGEFAmount(),
                    project.getTotalUNEPGEFAmount(),
                    project.getTotalUNEPFee(),
                    ms.getProjectImplementationDate('SignatureOfLegalInstrumentActual'),
                    ms.getEvaluationDatesDate('MTERactual'),
                    mofu.getLastestRevisionDate(),
                    ms.getProjectImplementationDate('CompletionActual'),
                    ))
        return result
