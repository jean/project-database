from Report import Report
from Products.ProjectDatabase.utils import unep_report_format_date

class TerminalEvaluationsComingUpReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Terminal Evaluations Coming Up Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'GEF ID',
            'Project title',
            'Focal Area',
            'Milestone date',
            'Task Manager',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        if projects is None:
            projects = self.context.objectValues(spec='Project')
        result = []
        for project in projects:
            ms = project.milestones
            if project.isTheProjectPublished() and \
                   ms.getEvaluationDatesDate('TerminalEvaluationExpected') and \
                   not ms.getEvaluationDatesDate('TerminalEvaluationActual'):
                pgi = project.project_general_info
                mande = project.mne_folder

                result.append((
                        pgi.getGEFid(),
                        pgi.Title(),
                        pgi.getFocalAreaNames(),
                        unep_report_format_date(self.context, \
                            ms.getEvaluationDatesDate('TerminalEvaluationExpected')),
                        pgi.getCurrentTM(),
                    ),)

        return result
