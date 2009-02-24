from Report import Report
from DateTime import DateTime
from Products.ProjectDatabase.utils import unep_report_format_date

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
            "Project Title: %s" % self.context.project_general_info.Title(),
            "Report Date: %s" % unep_report_format_date(self.context, DateTime())),)
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        project = self.context
        result = []
        pgi = project.project_general_info
        ms = project.milestones
        # mofu = project.fmi_folder.getMainFinanceObject()
        # if mofu and project.isTheProjectPublished():
        result.append(( 'PDF approval:', 'Unknown'))
        result.append(( 'PIF approval:',
                    unep_report_format_date(self.context, ms.getPIFApprovalDate('CEOPIFApprovalActual'))
            ))
        result.append(( 'PIF withdrawal:',
                    unep_report_format_date(self.context, ms.getPIFApprovalDate('PIFwithdrawal'))
            ))
        result.append(( 'PPG approval:',
                    unep_report_format_date(self.context, ms.getPPGApprovalDate('CEOPPGapproval'))
            ))
        result.append(( 'CEO approval/endorsement (expected):',
                    unep_report_format_date(self.context, ms.getProjectApprovalDate('CEOApprovalEndorsementExpected'))
            ))
        result.append(( 'CEO approval/endorsement (actual):',
                    unep_report_format_date(self.context, ms.getProjectApprovalDate('CEOApprovalEndorsementActual'))
            ))
        result.append(( 'Work Programme (expected)(PIF Approval?):', 'Unknown'))
        result.append(( 'Work Programme (actual)(PIF Approval?):',
                    unep_report_format_date(self.context, ms.getPIFApprovalDate('WPinclusion'))
            ))
        result.append(( 'MTE/MTR (expected):',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('MTERexpected'))
            ))
        result.append(( 'MTE/MTR (actual):',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('MTERactual'))
            ))
        result.append(( 'Completion (expected):',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('CompletionExpected'))
            ))
        result.append(( 'Completion (actual):',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('CompletionActual'))
            ))
        result.append(( 'TE (expected:',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('TerminalEvaluationExpected'))
            ))
        result.append(( 'TE (actual):',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('TerminalEvaluationActual'))
            ))
        result.append(( 'Closure:',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('ClosureActual'))
            ))
        result.append(( 'Suspension:',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('Suspension'))
            ))
        result.append(( 'Re-activation:',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('ActualReinitiation'))
            ))
        result.append(( 'Cancellation:',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('Cancellation'))
            ))
        return result


