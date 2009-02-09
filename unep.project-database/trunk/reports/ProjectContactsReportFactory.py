from Report import Report

class ProjectContactsReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Project Title',
            'FMO',
            'email',
            'Phone No',
            'TM',
            'email',
            'Phone No',
            'GEF Sec',
            'email',
            'Other IA',
            'email',
            'Phone No.',
            'Project Manager',
            'email',
            'Phone No.',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
