from Report import Report
from Products.ProjectDatabase.utils import inner_strip, unep_report_format_date

class IPIStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('IPI List Report')
        report.setReportHeaders((
            'IPI List Report',
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
            'Withdrawal Date'
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            if not project.isTheProjectPublished():
                result.append((
                    project.getId(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.project_general_info.Title(),
                    project.project_general_info.getExecutingAgencyNames(),
                    inner_strip(project.project_general_info.getPIFTotalGEFAmount()),
                    project.project_general_info.getSummaryDescription(),
                    unep_report_format_date(self.projectdatabase, \
                            project.milestones.getConceptDevelopmentDate('Withdrawal'))
                    ))
        return result
