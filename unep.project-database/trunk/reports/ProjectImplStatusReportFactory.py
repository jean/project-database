from Report import Report

class ProjectImplementationStatusReportFactory(object):

    def __init__(self, projectdatabase, **kw):
        self.projectdatabase = projectdatabase
        self.params = kw

    def getReport(self):
        # create and fill the report
        report = Report('Project Implementation Status Report')
        report.setReportHeaders((
            'Project Implementation Status Report',
            ),)
        report.setTableHeaders(((
            'Dbase ID.',
            'GEF ID',
            'IMIS No.',
            'Focal Area',
            'Project Type',
            'Geographic Scope',
            'Country(ies)',
            'Project Title',
            'Total GEF Amount',
            'UNEP GEF Amount',
            'UNEP Fee',
            'Signature',
            'Inception Meeting',
            'Mid-term Review',
            'Last Revision Date',
            'Expected Completion',
            'Revised Completion',
            'Terminal Evaluation',
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
                    project.project_general_info.getProjectTypeName(),
                    project.project_general_info.getGeographicScopeValues(),
                    project.project_general_info.getCountryNames(),
                    project.Title(),
                    project.getTotalGEFAmount(),
                    project.getTotalUNEPGEFAmount(),
                    project.getTotalUNEPFee(),
                    project.milestones.getProjectImplementationDate('SignatureOfLegalInstrumentActual'),
                    'Unknown Inception Meeting Date',
                    'Unknown MTR',
                    'Unknown Last revision date',
                    'Unknown Expected Completion Date',
                    'Unknown Revised Completion Date',
                    project.getLatestReportData('te', 'report_received_date'),
                    ))
        return result
