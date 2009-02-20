from Report import Report
from Products.ProjectDatabase.utils import unep_report_format_date

class ProjectCycleStageStatusReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Project Cycle Stage Status Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Dbase ID',
            'GEF ID',
            'IMIS No.',
            'Project title',
            'Project Cycle Stage',
            'Milestone action',
            'Date',
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
            mofu = project.fmi_folder.getMainFinanceObject()
            if mofu and project.isTheProjectPublished():
                pgi = project.project_general_info
                mande = project.mne_folder
                ms = project.milestones
                milestone, msdate = ms.getProjectStageMilestone()
                result.append((
                        project.getId(),
                        pgi.getGEFid(),
                        mofu.getIMISNumber(),
                        pgi.Title(),
                        ms.getProjectStage(),
                        milestone,
                        unep_report_format_date(self.context, msdate),
                    ),)

        return result
