from Report import Report
from DateTime import DateTime

class KeyMilestonesReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Key Milestones Report"
        report = Report(name)
        report.setReportHeaders(( \
            name, 
            "Project Title: %s" % self.context.pgi.Title(),
            "Report Date: %s" % DateTime()),)
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        project = self.context
        result = []
        pgi = project.project_general_info
        ms = project.milestones
        mofu = project.fmi_folder.getMainFinanceObject()
        if mofu and project.isTheProjectPublished():
            result.append((
                unep_report_format_date(self.projectdatabase, \
                    ms.getProjectApprovalDate('PRCReview')),
                unep_report_format_date(self.projectdatabase, \
                    ms.getProjectApprovalDate('CEOApprovalEndorsementExpected')),
                unep_report_format_date(self.projectdatabase, \
                    ms.getProjectApprovalDate('SubmissionToGEFSec')),
                unep_report_format_date(self.projectdatabase, \
                    ms.getProjectApprovalDate('ReviewSheet')),
                unep_report_format_date(self.projectdatabase, \
                    ms.getProjectApprovalDate('CEOApprovalEndorsementActual')),
                unep_report_format_date(self.projectdatabase, \
                    ms.getProjectApprovalDate('PAGApprovalExpected')),
                ))
        return result
