from Report import Report

class CountryRiskReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Country Risk Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Country',
            'Year',
            'Risk Rating',
            ),))
        # XXX Implement this
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []
        for project in projects:
            pass
        return result
