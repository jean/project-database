from Report import Report

class MidTermEvaluationStatusReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Mid-term Evaluation Status Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
			'IMIS No.',
			'Project title',
			'Focal area',
			'Evaluation budget',
			'TM',
			'FMO',
			'MTE Status',
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
