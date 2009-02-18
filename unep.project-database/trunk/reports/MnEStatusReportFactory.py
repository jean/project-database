from Report import Report
from Products.ProjectDatabase.utils import inner_strip, unep_report_format_date

class MnEStatusReportFactory(object):

    def __init__(self, context):
        self.context = context
        self.evaluationType = ''
        self.name = ''

    def getReport(self):
        # create and fill the report
        report = Report(self.name)
        report.setReportHeaders(( self.name,),)
        report.setTableHeaders(((
            'IMIS No.',
            'Project title',
            'Focal area',
            'Review budget',
            'TM',
            'FMO',
            '%s Status' % self.evaluationType,
            'Lead Consultant',
            'email',
            'Phone No.',
            'Other Consultants',
            'Project Rating',
            ),))
        # XXX Implement this
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []

        for project in projects:
            pgi = project.project_general_info
            ms = project.milestones
            mofu = project.fmi_folder.getMainFinanceObject()
            mande = project.mne_folder

            if mofu and project.isTheProjectPublished() and \
                    not ms.getProjectImplementationDate('Cancellation') and \
                    not ms.getProjectImplementationDate('Termination'):
                for mne in mande.objectValues(spec='MonitoringAndEvaluation'):
                    if mne.getEvaluationType() == self.evaluationType:
                        result.append((
                            mofu.getIMISNumber(),
                            pgi.Title(),
                            pgi.getFocalAreaNames(),
                            inner_strip(mofu.getEvaluationAmount(self.evaluationType)),
                            pgi.getCurrentTM(),
                            mofu.getCurrentFMO(),
                            mne.getLatestEvaluationProcessStatus(),
                            mne.getLeadEvaluator(),
                            'Unknown',
                            'Unknown',
                            mne.getOtherEvaluators(),
                            'Unknown',
                            ))

        return result
