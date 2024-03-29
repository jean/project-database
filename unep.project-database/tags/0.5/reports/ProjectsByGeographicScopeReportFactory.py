from Report import Report

class ProjectsByGeographicScopeReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Projects by Geographic Scope Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Focal Area',
            'Geographic scope',
            'Region',
            'Sub-region',
            'Participating countries',
            'Project title',
            'Status',
            'GEF amount',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
