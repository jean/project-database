from Report import Report
from Products.ProjectDatabase.utils import unep_report_format_date

class MidTermEvaluationsComingUpReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Mid-term Evaluations Coming Up Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'GEF ID',
            'Project title',
            'Focal Area',
            'Milestone date',
            'Task Manager',
            ),))
        # XXX Implement this
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
                   ms.getEvaluationDatesDate('MTERexpected') and \
                   not ms.getEvaluationDatesDate('MTERactual'):
                pgi = project.project_general_info
                mande = project.mne_folder

                result.append((
                        pgi.getGEFid(),
                        pgi.Title(),
                        pgi.getFocalAreaNames(),
                        unep_report_format_date(self.context, \
                            ms.getEvaluationDatesDate('MTERexpected')),
                        pgi.getCurrentTM(),
                    ),)

        return result
