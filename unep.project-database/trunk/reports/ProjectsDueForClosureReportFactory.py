from Report import Report

class ProjectsDueForClosureReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'IMIS No.',
            'Project Title',
            'Finance Object',
            'Actual Completion Date',
            'Outputs',
            'Terminal report',
            'Final Expenditure report',
            'Audit report',
            'Inventory',
            'Co-financing report',
            'Terminal Evaluation',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

