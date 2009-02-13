from Report import Report
from Products.ProjectDatabase.utils import inner_strip

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
            pgi = project.project_general_info
            ms = project.milestones
            mofu = project.fmi_folder.getMainFinanceObject()

            if mofu and project.isTheProjectPublished() and \
                    ms.getProjectImplementationDate('ClosureActual') and \
                    not ms.getProjectImplementationDate('Cancellation') and \
                    not ms.getProjectImplementationDate('Termination') and \
                    not ms.getProjectImplementationDate('Suspension'):
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
                    ms.getEvaluationDatesDate('MTERactual'),
                    ms.getProjectImplementationDate('CompletionActual'),
                    ms.getEvaluationDatesDate('TerminalEvaluationActual'),
                    mofu.getLastestRevisionDate(type='Closure'),
                    ))
        return result
