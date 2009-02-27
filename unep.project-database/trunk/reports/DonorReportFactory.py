from Report import Report
from Products.ProjectDatabase.utils import inner_strip

class DonorReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Donor Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Donor name',
            'Donor type',
            'Project title',
            'Focal Area',
            'Geographic scope',
            'Region',
            'Country(ies)',
            'Pledged (planned) amount',
            'Total project grant',
            'Project status',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        projects = self.context.objectValues(spec='Project')
        result = []
        for project in projects:
            mofu = project.fmi_folder.getMainFinanceObject()
            pgi = project.project_general_info
            if mofu and project.isTheProjectPublished():
                pledges = mofu.getDonorPledges()
                for pledge in pledges:
                    result.append((
                        pledge['name'],
                        pledge['type'],
                        pgi.Title(),
                        pgi.getFocalAreaNames(),
                        pgi.getGeographicScopeValues(),
                        pgi.getRegionNames(),
                        pgi.getCountryNames(),
                        inner_strip(pledge['amount']),
                        inner_strip(mofu.getSumFinanceObjectAmount()),
                        mofu.getStatus(),
                        ))
        return result

