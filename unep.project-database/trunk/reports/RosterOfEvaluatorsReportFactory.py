from Report import Report

class RosterOfEvaluatorsReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
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
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
