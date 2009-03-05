from Report import Report
from Products.ProjectDatabase.utils import \
        inner_strip, amount2millions, unep_report_format_date, getVocabularyValue
from DateTime import DateTime

class ProjectImplementationReviewReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Project Implementation Review Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Fiscal Year',
            'GEF ID',
            'IMIS No',
            'Implementing Agencies',
            'Focal Area',
            'Geographic Scope',
            'Region',
            'Countries',
            'Project Title',
            'First Disbursement',
            'Completion Expected',
            'Actual/Revised Completion',
            'Project Type',
            'PDF Funding US$m',
            'GEF Grant US$m',
            'Total GEF Grant US$m',
            'Expected Co-financing US$m',
            'Total Project Cost US$m',
            'Overall DO Rating',
            'Overall IP Rating',
            'Overall Risk Rating',
            'Total GEF Disbursement as of June 30 US$m',
            'Evaluation Type',
            'Evaluation Date',
            'Overall Evaluation Rating',
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
            ms = project.milestones
            mofu = project.fmi_folder.getMainFinanceObject()
            mande = project.mne_folder

            if mofu and project.isTheProjectPublished():
                for pir in mande.objectValues(spec='PIRRating'):
                    pdf_funding = project.fmi_folder.getTotalPDFFunding()
                    mofu_funding = mofu.getSumFinanceObjectAmount()
                    total_funding = pdf_funding + mofu_funding
                    cofin = mofu.getTotalCostOfFinanceObjectPlanned()
                    total_cost = cofin + total_funding
                    fiscal_year_end = DateTime('%s/06/30' % pir.getFiscalYear())
                    eval_type, report_date, rating = \
                            mande.getFinalReportInfoInYear(fiscal_year_end)
                    result.append((
                        pir.getFiscalYear(),
                        pgi.getGEFid(),
                        mofu.getIMISNumber(),
                        pgi.getGEFAgencyNames(),
                        pgi.getFocalAreaNames(),
                        pgi.getGeographicScopeValues(),
                        pgi.getRegionNames(),
                        pgi.getCountryNames(),
                        pgi.Title(),
                        unep_report_format_date(self.context, \
                                ms.getProjectImplementationDate('FirstDisbursementActual')),
                        unep_report_format_date(self.context, \
                                ms.getProjectImplementationDate('CompletionExpected')),
                        unep_report_format_date(self.context, \
                                ms.getProjectImplementationDate('CompletionActual')),
                        pgi.getProjectTypeName(),
                        amount2millions(pdf_funding),
                        amount2millions(mofu_funding),
                        amount2millions(total_funding),
                        amount2millions(cofin),
                        amount2millions(total_cost),
                        getVocabularyValue(self.context, 'Rating', \
                                pir.getDevelopmentObjective()),
                        getVocabularyValue(self.context, 'Rating', \
                                pir.getImplementationProgress()),
                        getVocabularyValue(self.context, 'RiskLevel', \
                                pir.getProjectRisk()),
                        amount2millions(mofu.getSumCashDisbursementsToDate(fiscal_year_end)),
                        eval_type,
                        unep_report_format_date(self.context, report_date),
                        rating,
                        ))
        return result
