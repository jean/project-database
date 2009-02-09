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
            'Dbase ID.',
            'GEF ID',
            'IMIS No.',
            'Focal Area',
            'Project Title',
            'Lead Executing Agency',
            'Total GEF Amount',
            'UNEP Amount',
            'UNEP Fee',
            'Signature',
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
            if not project.milestones.getProjectImplementationDate('ClosureActual'):
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    'Unknown IMIS No',
                    project.project_general_info.getFocalAreaNames(),
                    project.Title(),
                    project.getTotalGEFAmount(),
                    project.getTotalUNEPGEFAmount(),
                    project.getTotalUNEPFee(),
                    ))
        return result
