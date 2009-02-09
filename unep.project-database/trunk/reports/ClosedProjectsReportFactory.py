from Report import Report

class ClosedProjectsReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('Closed Projects Report')
        report.setReportHeaders((
            'Closed Projects Report',
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
            'Actual Completion',
            'Terminal Evaluation',
            'Closing Revision',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            if project.milestones.getProjectImplementationDate('ClosureActual'):
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
                    project.milestones.getEvaluationDatesDate('MTERactual'),
                    project.milestones.getProjectImplementationDate('CompletionActual'),
                    project.milestones.getEvaluationDatesDate('TerminalEvaluationActual'),
                    'Unknown closing revision date',
                    ))
        return result
