from Report import Report
from Products.ProjectDatabase.utils import \
        inner_strip, unep_report_format_date, getVocabularyValue

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
                        unep_report_format_date(self.context, \
                                ms.getProjectImplementationDate('FirstDisbursementActual')),
                        unep_report_format_date(self.context, \
                                ms.getProjectImplementationDate('ClosureExpected')),
                        unep_report_format_date(self.context, \
                                ms.getProjectImplementationDate('ClosureActual')),
                        pgi.getProjectTypeName(),
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        getVocabularyValue(self.context, 'Rating', \
                                pir.getDevelopmentObjective()),
                        getVocabularyValue(self.context, 'Rating', \
                                pir.getImplementationProgress()),
                        getVocabularyValue(self.context, 'RiskLevel', \
                                pir.getProjectRisk()),
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        'Unknown',
                        ))
        return result
