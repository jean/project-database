from Report import Report

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
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            if project.isTheProjectPublished() and \
                    not project.milestones.isPIFClearedByCEO():
                    # project.milestones.isConceptClearedBySPO() and \
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    project.project_general_info.getExecutingAgencyNames(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getProjectTypeName(),
                    project.project_general_info.getUNEPPriorityNames(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.project_general_info.Title(),
                    project.project_general_info.getPIFTotalGEFAmount(),
                    project.project_general_info.getPIFUNEPGEFAmount(),
                    project.project_general_info.getPIFUNEPFee(),
                    project.project_general_info.getPIFCofinancingAmount(),
                    project.milestones.getConceptDevelopmentDate('PAGClearance'),
                    project.milestones.getPIFApprovalDate('SubmissionToGEFSec'),
                    project.milestones.getPIFApprovalDate('ReviewSheet'),
                    project.milestones.getPIFApprovalDate('CEOPIFApprovalExpected'),
                    project.project_general_info.getPIFPPGAmount()
                    ))
        return result



