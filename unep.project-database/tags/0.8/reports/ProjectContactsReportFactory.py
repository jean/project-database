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
            'Phone No',
            'Other IA',
            'email',
            'Phone No.',
            'Project Manager',
            'email',
            'Phone No.',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.params.get('projects', None)
        if projects is None:
            projects = self.context.objectValues(spec='Project')
        result = []
        for project in projects:
            pgi = project.project_general_info
            fmo_name = fmo_email = fmo_phone = None
            mofu = project.fmi_folder.getMainFinanceObject()
            if mofu:
                fmo_name, fmo_email, fmo_phone = mofu.getCurrentFMODetails()
            tm_name, tm_email, tm_phone = pgi.getCurrentTMDetails()
            gs_name, gs_email, gs_phone = pgi.getGEFSecStaffDetails()
            ia_name, ia_email, ia_phone = pgi.getLeadAgencyContactDetails()
            pm_name, pm_email, pm_phone = pgi.getProjectManagerDetails()
            if project.isTheProjectPublished():
                result.append((
                    pgi.Title(),
                    fmo_name,
                    fmo_email,
                    fmo_phone,
                    tm_name,
                    tm_email,
                    tm_phone,
                    gs_name,
                    gs_email,
                    gs_phone,
                    ia_name,
                    ia_email,
                    ia_phone,
                    pm_name,
                    pm_email,
                    pm_phone,
                    ))
        return result
