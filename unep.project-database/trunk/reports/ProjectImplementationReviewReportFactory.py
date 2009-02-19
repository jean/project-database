from Report import Report

class ProjectImplementationReviewReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Project Implementation Review Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        # XXX Implement this
        report.setTableHeaders(((
            'GEF ID',
            'IMIS No',
            'Implementing Agencies',
            'Focal Area',
            'Geographic Scope',
            'Region',
            'Countries',
            'Project Title',
            'First Disbursement',
            'Closure Expected',
            'Actual Closing Date',
            'Project Type',
            'PDF Funding',
            'GEF Grant',
            'Total GEF Grant',
            'Expected Co-financing',
            'Total Project Cost',
            'Overall DO Rating',
            'Overall IP Rating',
            'Overall Risk Rating',
            'Total GEF Disbursement as of June 30',
            'Evaluation Type',
            'Evaluation Date',
            'Overall Evaluation Rating',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []

        for project in projects:
            pgi = project.project_general_info
            ms = project.milestones
            mofu = project.fmi_folder.getMainFinanceObject()
            mande = project.mne_folder

            if mofu and project.isTheProjectPublished():
                for pir in mande.objectValues(spec='PIRRating'):
                    result.append((
                        pgi.getGEFid(),
                        mofu.getIMISNumber(),
                        pgi.getExecutingAgencyNames(),
                        pgi.getFocalAreaNames(),
                        pgi.getGeographicScopeValues(),
                        pgi.getRegionNames(),
                        pgi.getCountryNames(),
                        pgi.Title(),
                        ms.getProjectImplementationDate('FirstDisbursementActual'),
                        ms.getProjectImplementationDate('ClosureExpected'),
                        ms.getProjectImplementationDate('ClosureActual'),
                        pgi.getProjectTypeName(),
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        pir.getDevelopmentObjective(),
                        pir.getImplementationProgress(),
                        pir.getProjectRisk(),
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        ))
        return result
