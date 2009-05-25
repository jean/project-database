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
            'GEF ID',
            'Executing Agency',
            'Year',
            'Risk Ratings',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        result = []
        for project in projects:
            pgi = project.project_general_info
            mofu = project.fmi_folder.getMainFinanceObject()
            if mofu and project.isTheProjectPublished():
                ratingPairs = mofu.getEARiskRatings()
                for ratingPair in ratingPairs:
                    result.append((
                        project.getId(),
                        mofu.getLeadExecutingAgency(),
                        ratingPair[0],
                        ratingPair[1]
                  ))
        return result
