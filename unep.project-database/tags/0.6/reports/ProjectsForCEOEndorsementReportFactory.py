from Report import Report

class ProjectsForCEOEndorsementReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Projects for CEO Endorsement Report"
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
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
