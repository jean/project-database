from Report import Report

class ProjectsAtRiskReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Projects at Risk Report"
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
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []
        # import pdb; pdb.set_trace()
        for project in projects:
            for fo in project.fmi_folder.objectValues():
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    fo.getIMISNumber(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getProjectTypeName(),
                    fo.getId(),
                    project.Title(),
                    project.project_general_info.getExecutingAgencyNames(),
                    project.project_general_info.getCurrentTM(),
                    fo.getCurrentFMO(),
                    fo.getLatestEARiskRating()
                    ))

        return result
