from Report import Report
from Products.ProjectDatabase.utils import inner_strip, unep_report_format_date

class PIFApprovalStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('PIF Approval Status Report')
        report.setReportHeaders((
            'PIF Approval Status Report',
            ),)
        report.setTableHeaders(((
            'Dbase ID',
            'GEF ID',
            'IA(s)',
            'Focal Area',
            'Project Type',
            'UNEP Priority',
            'Geographic Scope',
            'Country(ies)',
            'Project Title',
            'Total GEF Amount',
            'UNEP GEF Amount',
            'UNEP Fee',
            'Cofinancing',
            'PAG Approval',
            'Submission to GEF Sec',
            'Review Sheet',
            'CEO Approval Expected',
            'PPG Amount'
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        result = []
        for project in projects:
            if project.isTheProjectPublished() and \
                    not project.milestones.isPIFClearedByCEO():
                    # project.milestones.isConceptClearedBySPO() and \
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    project.project_general_info.getGEFAgencyNames(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getProjectTypeName(),
                    project.project_general_info.getUNEPPriorityNames(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.project_general_info.Title(),
                    inner_strip(project.project_general_info.getPIFTotalGEFAmount()),
                    inner_strip(project.project_general_info.getPIFUNEPGEFAmount()),
                    inner_strip(project.project_general_info.getPIFUNEPFee()),
                    inner_strip(project.project_general_info.getPIFCofinancingAmount()),
                    unep_report_format_date(self.projectdatabase, \
                        project.milestones.getConceptDevelopmentDate('PAGClearance')),
                    unep_report_format_date(self.projectdatabase, \
                        project.milestones.getPIFApprovalDate('SubmissionToGEFSec')),
                    unep_report_format_date(self.projectdatabase, \
                        project.milestones.getPIFApprovalDate('ReviewSheet')),
                    unep_report_format_date(self.projectdatabase, \
                        project.milestones.getPIFApprovalDate('CEOPIFApprovalExpected')),
                    inner_strip(project.project_general_info.getPIFPPGAmount())
                    ))
        return result



