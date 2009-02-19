from Report import Report

class ExecutingAgencyRiskReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Executing Agency Risk Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Executing Agency',
            'Year',
            'Risk Ratings',
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
            pgi = project.project_general_info
            mofu = project.fmi_folder.getMainFinanceObject()
        return result
