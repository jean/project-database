from Report import Report

class ProjectsAtRiskReportFactory(object):

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
            'IMIS No',
            'Focal Area',
            'Project type',
            'Finance object',
            'Project title',
            'Lead Executing Agency',
            'TM',
            'FMO',
            'Risk rating',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
