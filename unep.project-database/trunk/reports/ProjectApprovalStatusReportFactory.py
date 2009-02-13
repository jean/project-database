from Report import Report
from Products.ProjectDatabase.utils import inner_strip

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
            'UNEP GEF Amount',
            'UNEP Fee',
            'PRC Review',
            'Expected CEO Endorsement/Approval',
            'Submission to GEF Sec',
            'Review Sheet',
            'Actual CEO Endorsement',
            'UNEP Approval Expected'
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.projectdatabase.objectValues(spec='Project')
        result = []
        for project in projects:
            pgi = project.project_general_info
            ms = project.milestones
            mofu = project.fmi_folder.getMainFinanceObject()

            if mofu and project.isTheProjectPublished() and \
                    not project.milestones.getProjectImplementationDate('SignatureOfLegalInstrumentActual'):
                result.append((
                    project.getId(),
                    pgi.getGEFid(),
                    pgi.getExecutingAgencyNames(),
                    pgi.getFocalAreaNames(),
                    pgi.getProjectTypeName(),
                    pgi.getGeographicScopeValues(),
                    pgi.getCountryNames(),
                    pgi.Title(),
                    inner_strip(project.getTotalUNEPGEFAmount()),
                    inner_strip(project.getTotalUNEPFee()),
                    ms.getProjectApprovalDate('PRCReview'),
                    ms.getProjectApprovalDate('CEOApprovalEndorsementExpected'),
                    ms.getProjectApprovalDate('SubmissionToGEFSec'),
                    ms.getProjectApprovalDate('ReviewSheet'),
                    ms.getProjectApprovalDate('CEOApprovalEndorsementActual'),
                    ms.getProjectImplementationDate('SignatureOfLegalInstrumentExpected'),
                    ))
        return result
