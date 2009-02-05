from Report import Report

class IPIStatusReport(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def __call__(self):
        # create and fill the report
        report = Report('IPI Status Report')
        report.setReportHeaders((
            'IPI Status Report',
            ),)
        report.setTableHeaders((
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
            ),)
        report.setTableRows(self.getIPIData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getIPIData(self):
        projects = self.projectdatabase.getFolderContents(
                full_objects=True, 
                contentFilter={'portal_type':'Project'}
                )
        result = []
        for project in projects:
            if not project.milestones.getIsClearedBySPO():
                result.append((
                    project.getId(),
                    project.pgi.getFocalAreaNames(),
                    project.pgi.getScopeValues(),
                    project.pgi.getCountryNames(),
                    project.Title(),
                    project.pgi.getExecutingAgencyNames(),
                    project.pgi.getTotalGEFAmount(),
                    project.pgi.getSummaryDescription(),
                    project.milestones.getConceptDevelopmentDate('SPOClearance'),
                    project.milestones.getConceptDevelopmentDate('Withdrawal')
                    ))
        return result


