from Report import Report
from Products.ProjectDatabase.utils import \
        inner_strip, getVocabularyValue

class ProjectsByGeographicScopeReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Projects by Geographic Scope Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Focal Area',
            'Geographic scope',
            'Region',
            'Sub-region',
            'Participating countries',
            'Project title',
            'Status',
            'GEF amount',
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
            mofu = project.fmi_folder.getMainFinanceObject()
            if project.isTheProjectPublished():
                mofu_Status = 'Unspecified'
                if mofu is not None:
                    mofu_Status =  getVocabularyValue(self.context,
                        'Status', mofu.getStatus())
                result.append((
                    pgi.getFocalAreaNames(),
                    pgi.getGeographicScopeValues(),
                    pgi.getRegionNames(),
                    pgi.getSubRegion(),
                    pgi.getCountryNames(),
                    pgi.Title(),
                    mofu_Status,
                    inner_strip(project.getTotalGEFAmount()),
                ))
        return result 
