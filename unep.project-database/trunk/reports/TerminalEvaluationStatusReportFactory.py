from Report import Report

class TerminalEvaluationStatusReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
                        'IMIS No.',
                        'Project title',
                        'Focal area',
                        'Evaluation budget',
                        'TM',
                        'FMO',
                        'TE Status',
                        'Lead Evaluator',
                        'email',
                        'Phone No.',
                        'Other Evaluators',
                        'Project Rating',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
