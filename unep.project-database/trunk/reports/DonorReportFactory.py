from Report import Report

class DonorReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Donor Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Donor name',
            'Donor type',
            'Project title',
            'Focal Area',
            'Geographic scope',
            'Region',
            'Country(ies)',
            'Pledged (planned) amount',
            'Total project grant',
            'Project status',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
