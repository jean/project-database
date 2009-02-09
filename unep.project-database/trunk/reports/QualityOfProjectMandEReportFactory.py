from Report import Report

class QualityOfProjectMandEReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, name):
        # create and fill the report
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'GEF ID',
            'IMIS No.',
            'Focal Area',
            'Lead Executing Agency',
            'Project Title',
            'M&E rating',
            'FY',
            'TM',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
