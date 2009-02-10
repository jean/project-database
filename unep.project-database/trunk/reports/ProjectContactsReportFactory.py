from Report import Report

class ProjectContactsReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Project Contacts Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Project Title',
            'FMO',
            'email',
            'Phone No',
            'TM',
            'email',
            'Phone No',
            'GEF Sec',
            'email',
            'Other IA',
            'email',
            'Phone No.',
            'Project Manager',
            'email',
            'Phone No.',
            ),))
        # XXX Implement this
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []
        # for project in projects:
        #     result.append((
        #         project.project_general_info.Title(),
        #         project.getId(),
        #         project.project_general_info.getGEFid(),
        #         'Unknown IMIS No',
        #         project.project_general_info.getFocalAreaNames(),
        #         project.project_general_info.getProjectTypeName(),
        #         project.project_general_info.getGeographicScopeValues(),
        #         project.project_general_info.getCountryNames(),
        #         project.getTotalGEFAmount(),
        #         project.getTotalUNEPGEFAmount(),
        #         project.getTotalUNEPFee(),
        #         project.milestones.getProjectImplementationDate('SignatureOfLegalInstrumentActual'),
        #         project.milestones.getProjectImplementationDate('Suspension'),
        #         'Unknown reason',
        #         'Unknown resume date',
        #         ))
        return result
