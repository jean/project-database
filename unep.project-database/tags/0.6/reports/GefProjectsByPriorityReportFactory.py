from Report import Report

class GefProjectsByPriorityReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "GEF Projects by Priority Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'MTS priority',
            'Project title',
            'Focal Area',
            'Task Manager',
            'Mode of execution',
            'Division',
            'Status',
            'GEF amount',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
