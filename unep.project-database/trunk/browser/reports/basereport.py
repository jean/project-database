import StringIO
import csv
from zope.publisher.interfaces.browser import IBrowserView
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

class BaseReport(BrowserView):
    implements(IBrowserView)

    _pt = ViewPageTemplateFile("simplehtmlreport.pt")

    def html(self):
        return self._pt()

    def csv(self):
        report = self.getReport()
        output = StringIO.StringIO()
        csvwriter = csv.writer(output)

        for header in report.getReportHeaders():
            csvwriter.writerow([header])

        for header in report.getTableHeaders():
            csvwriter.writerow(header)

        for row in report.getTableRows():
            csvwriter.writerow(row)

        for total in report.getTableTotals():
            csvwriter.writerow(total)

        for footer in report.getReportFooters():
            csvwriter.writerow([footer])
        
        x = output.getvalue()
        output.close()
        self.request.response.setHeader("Content-Type", "text/csv")
        self.request.response.setHeader("Content-Disposition", "attachment; filename=bob.csv")
        return x

    def pdf(self):
        return "I am not a pdf, but I can fake it"

    def __call__(self, format=None):
        if format is None:
            format = self.request.get('format', None)

        if format == 'csv':
            return self.csv()

        if format == 'pdf':
            return self.pdf()

        return self.html()
        
    def getCSVReport(self):
        return self.__call__(format="csv")

    def getPDFReport(self):
        return self.__call__(format="pdf")

    def getReport(self):
        raise TypeError('Abstract method ' + self._class.__name__ + 
                                    '.' + self._function + ' called')
