from Report import Report
from DateTime import DateTime
from Products.ProjectDatabase.utils import \
        unep_report_format_date, getVocabularyValue

class ProjectImplementationReviewTableReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Project Implementation Review Report (Section 1)"
        report = Report(name)
        report.setReportHeaders(( 
            name,
            "Report Date: %s" % unep_report_format_date(self.context, DateTime())),)
        report.setTableHeaders(((
            'Item', 'Value',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        project = self.context
        result = []
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
                result.append(( 'Project Title:', pgi.Title(),))
                result.append(( 'Executing Agency:', pgi.getLeadExecutingAgencyNames(),))
                result.append(( 'Other Project partners:', pgi.getOtherExecutingAgencyNames(),))
                result.append(( 'Geographical Scope:', pgi.getGeographicScopeValues(),))
                result.append(( 'Participating Countries:', pgi.getCountryNames(),))
                result.append(( 'GEF ID:', pgi.getGEFid(),))
                result.append(( 'IMIS number:', mofu.getIMISNumber(),))
                result.append(( 'Focal Area(s):', pgi.getFocalAreaNames(),))
                result.append(( 'Strategic Priority:', pgi.getStrategicPriorityName(),))
                result.append(( 'Strategic Objective:', pgi.getStrategicObjectiveName(),))
                result.append(( 'GEF approval/endorsement date:', 'Unknown'))
                result.append(( 'UNEP approval date:', 'Unknown'))
                result.append(( 'First Disbursement:',
                    unep_report_format_date(self.context, \
                            ms.getProjectImplementationDate('FirstDisbursementActual')),))
                result.append(( 'Planned duration:', mofu.getPlannedDuration(),))
                result.append(( 'Expected completion date:',
                    unep_report_format_date(self.context, \
                            ms.getProjectImplementationDate('CompletionExpected')),))
                result.append(( 'Revised completion date:',
                    unep_report_format_date(self.context, \
                            ms.getProjectImplementationDate('CompletionRevised')),))
                result.append(( 'Actual completion date:',
                    unep_report_format_date(self.context, \
                            ms.getProjectImplementationDate('CompletionActual')),))
                result.append(( 'Project Type:', pgi.getProjectTypeName(),))
                result.append(( 'PDF/PPG GEF amount:', pdf_funding,))
                result.append(( 'PDF/PPG co-financing:', project.fmi_folder.getTotalPDFPPGcofinActual()))
                result.append(( 'Project GEF amount:', mofu_funding,))
                result.append(( 'Expected Project Co-financing:', cofin,))
                result.append(( 'Total Project Cost:', total_cost,))
                result.append(( 'Mid-term review/evaluation (planned date):',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('MTERexpected'))
                    ))
                result.append(( 'Terminal Evaluation (planned date):',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('TerminalEvaluationExpected'))
                    ))
                result.append(( 'Mid-term review/evaluation (actual date):',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('MTERactual'))
                    ))
                result.append(( 'Terminal Evaluation (actual date):',
                    unep_report_format_date(self.context, ms.getEvaluationDatesDate('TerminalEvaluationActual'))
                    ))
                result.append(( 'No. of revisions:',
                    ))
                result.append(( 'Date of last Steering Committee meeting:', 'Unknown'))
                result.append(( 'Date of last Revision:', mofu.getLastestRevisionDate()))
                result.append(( 'Disbursement as of 30 June:',
                    mofu.getSumCashDisbursementsToDate(fiscal_year_end),
                    ))
                result.append(( 'Date of completion:',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('CompletionActual'))
                    ))
                result.append(( 'Date of financial closure:',
                    unep_report_format_date(self.context, ms.getProjectImplementationDate('ClosureActual'))
                    ))
                result.append(( 'Actual expenditures reported as of 30 June:', 'Unknown'))
                result.append(( 'Total co-financing realized as of 30 June:', 'Unknown'))
                result.append(( 'Actual expenditures entered in IMIS as of 30 June:', 'Unknown'))
                result.append(( 'Leveraged financing:', pgi.getLeveragedFinancingAmount()))
                result.append(( 'Project summary:', pgi.getSummaryDescription()))
                result.append(( 'Project Implementation Status:', 
                    getVocabularyValue(self.context, 'Rating', pir.getImplementationProgress())))
        return result


