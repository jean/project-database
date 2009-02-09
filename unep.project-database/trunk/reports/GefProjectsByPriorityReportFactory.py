from Report import Report

class GefProjectsByPriorityReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
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
