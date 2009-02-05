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
            'PAG Approval',
            'Submission to GEF Sec',
            'Review Sheet',
            'CEO Approval',
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
            if project.milestones.isConceptClearedBySPO() and \
                    not project.milestones.isPIFClearedByCEO():
                result.append((
                    project.getId(),
                    project.project_general_info.getGEFid(),
                    project.project_general_info.getExecutingAgencyNames(),
                    project.project_general_info.getFocalAreaNames(),
                    project.project_general_info.getProjectTypeName(),
                    project.project_general_info.getUNEPPriorityNames(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.Title(),
                    project.getTotalGEFAmount(),
                    project.getTotalUNEPGEFAmount(),
                    project.getTotalUNEPFee(),
                    project.milestones.getConceptDevelopmentDate('PAGClearance'),
                    project.milestones.getPIFApprovalDate('SubmissionToGEFSec'),
                    project.milestones.getPIFApprovalDate('ReviewSheet'),
                    project.milestones.getPIFApprovalDate('CEOPIFApproval'),
                    project.fmi_folder.getTotalPPGAmount()
                    ))
        return result



