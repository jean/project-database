from Report import Report

class ProjectsByStaffReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Projects by Staff Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Staff Name',
            'Staff position',
            'Focal Area',
            'Project Title',
            'Project Cycle Stage',
            'Last milestone action',
            'Actual date',
            'Project Grant ',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
