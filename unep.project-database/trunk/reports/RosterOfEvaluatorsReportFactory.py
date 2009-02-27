from Report import Report

class RosterOfEvaluatorsReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = 'Roster of Evaluators Report'
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Project title',
            'Focal Area',
            'Evaluation type',
            'EOU/TM Ratings of quality of evaluation report',
            'Date',
            'Evaluator',
            'Nationality',
            'Area of Expertise',
            'email',
            'Cell Phone',
            'Phone No.',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []
        for project in projects:
            if project.isTheProjectPublished():
                pgi = project.project_general_info
                mnes = \
                    project.mne_folder.objectValues(spec='MonitoringAndEvaluation')
                for mne in mnes:
                    evaluator, nationality, expertise, email, cell, phone = \
                        mne.getLeadEvaluatorDetails()
                    result.append((
                        pgi.Title(),
                        pgi.getFocalAreaNames(),
                        mne.getEvaluationType(),
                        mne.getEOUTerminalEvaluationReportQuality(),
                        "Unknown",
                        evaluator, 
                        nationality, 
                        expertise, 
                        email, 
                        cell, 
                        phone,
                        ))
        return result
