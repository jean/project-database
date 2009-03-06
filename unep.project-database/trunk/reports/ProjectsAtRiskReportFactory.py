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
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        if projects is None:
            projects = self.context.objectValues(spec='Project')
        result = []
        for project in projects:
            pgi = project.project_general_info
            ms = project.milestones
            mofu = project.fmi_folder.getMainFinanceObject()
            projectRisk = project.projectRisk()

            if mofu and project.isTheProjectPublished() and \
                    projectRisk > 0:
                result.append((
                    project.getId(),
                    pgi.getGEFid(),
                    mofu.getIMISNumber(),
                    pgi.getFocalAreaNames(),
                    pgi.getProjectTypeName(),
                    mofu.getId().upper(),
                    pgi.Title(),
                    pgi.getLeadExecutingAgencyNames(),
                    pgi.getCurrentTM(),
                    mofu.getCurrentFMODetails()[0],
                    projectRisk
                    ))

        return result
