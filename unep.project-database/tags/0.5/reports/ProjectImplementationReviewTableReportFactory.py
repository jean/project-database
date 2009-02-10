from Report import Report

class ProjectImplementationReviewTableReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Project Implementation Review Table Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'GEF ID',
            'IMIS No.',
            'Implementing Agency(ies)',
            'Focal Area',
            'Geographic Scope',
            'Region',
            'Country(ies)',
            'Project Title',
            'First Disbursement [date m/d/yyyy]',
            'Closure expected [date m/d/yyyy]',
            'Actual / Revised Closing [date m/d/yyyy]',
            'Project Type',
            'PDF Funding (if any) US$ m',
            'GEF grant US$ m',
            'Total GEF Grant (US$ m) =PDF + grant',
            'Expected Co-financing (US$ m)',
            'Total Project Cost ($m) =total GEF grant + co-financing',
            'Overall DO rating',
            'Overall IP rating',
            'Overall Risk rating',
            'Total GEF disbursement as of June 30, [year] ($m)',
            'Evaluation type',
            'Evaluation date',
            'Overall evaluation rating',
            ),))
        # XXX Implement this
        # report.setTableRows()
        # report.setTableTotals([])
        # report.setReportFooters()
        return report
