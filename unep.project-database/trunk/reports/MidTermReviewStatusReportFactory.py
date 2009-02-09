from Report import Report

class MidTermReviewStatusReportFactory(object):

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
            'Review budget',
            'TM',
            'FMO',
            'MTR Status',
            'Lead Consultant',
            'email',
            'Phone No.',
            'Other Consultants',
            'Project Rating',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
