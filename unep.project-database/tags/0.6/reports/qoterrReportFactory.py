from Report import Report

class qoterrReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Quality of Terminal Evaluation report ratings"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Project title',
            'EOU rating',
            'GEF EO Rating',
            ),))
        # XXX Implement this
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        # for project in projects:

        #     for me in project.bbb:
        return result
