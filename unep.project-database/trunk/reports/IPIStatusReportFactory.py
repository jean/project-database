from Report import Report

class IPIStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('IPI Status Report')
        report.setReportHeaders((
            'IPI Status Report',
            ),)
        report.setTableHeaders(((
            'Dbase ID',
            'Focal Area',
            'Geographic Scope',
            'Country(ies)',
            'Project Title',
            'Executing Agency',
            'Total GEF Amount',
            'Project Summary',
            'SPO Approval Date',
            'Withdrawal Date'
            ),))
        report.setTableRows(self.getIPIData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getIPIData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            if not project.milestones.isConceptClearedBySPO():
                result.append((
                    project.getId(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.project_general_info.Title(),
                    project.project_general_info.getExecutingAgencyNames(),
                    project.getTotalGEFAmount(),
                    project.project_general_info.getSummaryDescription(),
                    project.milestones.getConceptDevelopmentDate('SPOClearance'),
                    project.milestones.getConceptDevelopmentDate('Withdrawal')
                    ))
        return result


