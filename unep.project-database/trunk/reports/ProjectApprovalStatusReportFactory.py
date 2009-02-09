from Report import Report

class ProjectApprovalStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('Project Approval Status Report')
        report.setReportHeaders((
            'Project Approval Status Report',
            ),)
        report.setTableHeaders(((
            'Dbase ID',
            'GEF ID',
            'IA(s)',
            'Focal Area',
            'Project Type',
            'Geographic Scope',
            'Country(ies)',
            'Project Title',
            'Total GEF Amount',
            'UNEP GEF Amount',
            'PRC Review',
            'Expected CEO Endorsement/Approval',
            'Submission to GEF Sec',
            'Review Sheet',
            'Actual CEO Endorsement',
            'UNEP Approval'
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            if not project.milestones.getProjectImplementationDate('SignatureOfLegalInstrumentActual'):
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    project.project_general_info.getExecutingAgencyNames(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getProjectTypeName(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.Title(),
                    project.getTotalGEFAllocation(),
                    project.getTotalUNEPAllocation(),
                    project.milestones.getProjectApprovalDate('PRCReview'),
                    project.milestones.getProjectApprovalDate('CEOApprovalEndorsementExpected'),
                    project.milestones.getProjectApprovalDate('SubmissionToGEFSec'),
                    project.milestones.getProjectApprovalDate('ReviewSheet'),
                    project.milestones.getProjectApprovalDate('SubmissionToGEFSec'),
                    project.milestones.getProjectApprovalDate('CEOApprovalEndorsementActual'),
                    'Unknown UNEP Approval'
                    ))
        return result
