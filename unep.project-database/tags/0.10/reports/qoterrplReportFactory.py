from Report import Report
from Products.ProjectDatabase.utils import getVocabularyValue

class qoterrplReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Quality of Terminal Evaluation Report Ratings (Portfolio Level)"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Project title',
            'EOU rating',
            'GEF EO Rating',
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
            mande = project.mne_folder
            for me in mande.objectValues(spec='MonitoringAndEvaluation'):
                if me.getEvaluationType() == 'TE':
                    result.append((
                        pgi.Title(),
                        getVocabularyValue(self.context, \
                            'Rating', me.getEOUTerminalEvaluationReportQuality()),
                        getVocabularyValue(self.context, \
                            'Rating', me.getGEFTerminalEvaluationReportQuality())
                        ))
        return result
