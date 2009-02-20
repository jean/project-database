from Report import Report
from Products.ProjectDatabase.utils import \
        inner_strip, unep_report_format_date, getVocabularyValue

class QualityOfProjectMandEReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Quality of Project Monitoring and Evaluation Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'GEF ID',
            'IMIS No.',
            'Focal Area',
            'Lead Executing Agency',
            'Project Title',
            'M&E rating',
            'FY',
            'TM',
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
                pir = mande.getLatestPIRRating()
                if pir:
                    result.append((
                        pgi.getGEFid(),
                        mofu.getIMISNumber(),
                        pgi.getFocalAreaNames(),
                        pgi.getLeadExecutingAgencyName(),
                        pgi.Title(),
                        getVocabularyValue(self.context, \
                            'Rating', pir.getMonitoringAndEvaluation()),
                        pir.getFiscalYear(),
                        pgi.getCurrentTM(),
                        ))

        return result
