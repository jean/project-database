from Report import Report

class ProjectCycleStageStatusReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Dbase ID',
            'GEF ID',
            'IMIS No.',
            'Project title',
            'Project Cycle Stage',
            'Milestone action',
            'Date',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
