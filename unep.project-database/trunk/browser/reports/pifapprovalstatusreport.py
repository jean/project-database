import StringIO
import csv
from zope.publisher.interfaces.browser import IBrowserView
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

from Products.ProjectDatabase.reports.PIFApprovalStatusReportFactory \
        import PIFApprovalStatusReportFactory


class PIFApprovalStatusReport(BrowserView):
    implements(IBrowserView)

    pt = ViewPageTemplateFile("simplehtmlreport.pt")

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

        return self.pt()
        
    def getReport(self):
        factory = PIFApprovalStatusReportFactory(self.context)
        return factory.getReport()

    def getCSVReport(self):
        return self.__call__(format="csv")
