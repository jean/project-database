from Report import Report
from Products.Archetypes.utils import getToolByName
from Products.ProjectDatabase.utils import getVocabularyValue

class CountryRiskReportFactory(object):

    def __init__(self, context, **kw):
        portal = getToolByName(context, 'portal_url').getPortalObject()
        self.context = portal.get('countryclassification', None)
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Country Risk Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders(((
            'Country',
            'Year',
            'Risk Rating',
            ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        countries = self.context.objectValues(spec='CountryClassification')
        result = []
        for country in countries:
            result.append((
                getVocabularyValue(self.context,
                    'Country', country.getCountryName()),
                country.getYear(),
                getVocabularyValue(self.context,
                    'RiskLevel', country.getRiskRating())))
        return result
          

