from Report import Report

class ProjectsAtRiskReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self, thename):
        # create and fill the report
        report = Report(thename)
        report.setReportHeaders(( thename,),)
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
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []
        for project in projects:
            for fo in project.fmi_folder.objectValues():
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    fo.getIMISNumber(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getProjectTypeName(),
                    fo.getId().upper(),
                    project.project_general_info.Title(),
                    project.project_general_info.getExecutingAgencyNames(),
                    project.project_general_info.getCurrentTM(),
                    fo.getCurrentFMO(),
                    fo.getLatestEARiskRating()
                    ))

        return result
