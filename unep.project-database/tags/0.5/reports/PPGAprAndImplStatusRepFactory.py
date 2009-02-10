from Report import Report

class PPGApprovalAndImplementationStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('PPG Approval and Implementation Status Report')
        report.setReportHeaders((
            'PPG Approval and Implementation Status Report',
            ),)
        report.setTableHeaders(((
            'Dbase ID',
            'GEF ID',
            'IMIS No.',
            'Focal Area',
            'Project Title',
            'Lead Executing Agency',
            'Total GEF Amount',
            'UNEP Amount',
            'UNEP Fee',
            'Total Co-financing',
            'Submission to GEF Sec',
            'Review Sheet',
            'CEO Approval',
            'UNEP Approval',
            'Expected Completion',
            'Expected Closing',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            ppg = project.fmi_folder.get('ppg', None)
            if ppg and not project.milestones.getPPGImplementationDate('ClosureActual'):
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    ppg.getIMISNumber(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.Title(),
                    project.project_general_info.getLeadExecutingAgencyName(),
                    ppg.getCommittedGEFGrant(),
                    ppg.getSumFinanceObjectAmount(),
                    ppg.getFinanceObjectFee(),
                    ppg.getTotalCoFinOfFinanceObjectActual(),
                    project.milestones.getPPGApprovalDate('SubmissionToGEFSec'),
                    project.milestones.getPPGApprovalDate('ReviewSheet'),
                    project.milestones.getPPGApprovalDate('CEOPPGapproval'),
                    'Unknown UNEP Approval Date',
                    ppg.getExpectedCompletionDate(),
                    project.milestones.getPPGImplementationDate('ClosureExpected')
                    ))
        return result
