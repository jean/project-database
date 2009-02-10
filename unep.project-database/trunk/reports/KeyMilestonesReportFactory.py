from Report import Report

class KeyMilestonesReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Key Milestones Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        # XXX Implement this
        #report.setTableHeaders(((
        #    ),))
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
