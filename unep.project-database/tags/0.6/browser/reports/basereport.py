import StringIO
import csv
from zope.publisher.interfaces.browser import IBrowserView
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

have_rl = True
try:
    from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
except ImportError:
    have_rl = False

class BaseReport(BrowserView):
    implements(IBrowserView)

    _pt = ViewPageTemplateFile("simplehtmlreport.pt")

    def getReportFileName(self):
        return self.__class__.__name__

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
        self.request.response.setHeader("Content-Disposition", "attachment; filename=%s.csv" % self.getReportFileName())
        return x

    def pdf(self):
        if not have_rl:
            self.request.response.setHeader("Content-Type", "text/plain")
            return "PDF generation not enabled in this installation (reportlab not installed)"

        Elements = []
        data = []
        style = []
        width = 0
        stylesheet = getSampleStyleSheet()
        normal = stylesheet['Normal']


        report = self.getReport()
        for header in report.getReportHeaders():
            rownum = len(data)
            style.append(('FONT', (0, rownum), (1, rownum), "Helvetica-Bold", 12))
            data.append([header])
            width = max(width, 1)

        for header in report.getTableHeaders():
            rownum = len(data)
            style.append(('FONT', (0, rownum), (len(header)-1, rownum), "Helvetica-Bold", 9))
            data.append([Paragraph(h, normal) for h in header])
            width = max(width, len(header))

        for row in report.getTableRows():
            rownum = len(data)
            style.append(('FONT', (0, rownum), (len(row)-1, rownum), "Helvetica", 9))
            data.append(row)
            width = max(width, len(row))

        for total in report.getTableTotals():
            rownum = len(data)
            style.append(('FONT', (0, rownum), (len(total)-1, rownum), "Helvetica-Bold", 9))
            data.append(total)
            width = max(width, len(total))

        for footer in report.getReportFooters():
            rownum = len(data)
            style.append(('FONT', (0, rownum), (1, rownum), "Helvetica", 9))
            data.append([footer])
            width = max(width, 1)

        # Pad each row to the correct length
        for row in data:
            for i in range(len(row), width):
                row.append('')

        # Additional styles
        style.extend([('ALIGN',(0,0),(-1,-1),'LEFT'),
                      ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                     ])

        # Get reasonable table cell widths.
        colsizes = [0] * width
        for section in (report.getTableHeaders(),
                        report.getReportFooters()):
            for row in section:
                for col in range(len(colsizes)):
                    for word in row[col].split():
                        colsizes[col] = max(len(word), colsizes[col])
        for row in report.getTableRows():
            for col in range(len(colsizes)):
                colsizes[col] = max(len(row[col]), colsizes[col])
        colsizes = [min(size, 36) for size in colsizes]
        totalsize = 0
        for size in colsizes:
            totalsize = totalsize + size
        colsizes = [size*inch*7/totalsize for size in colsizes]

        # Construct the table
        t=Table(data, colsizes, None)
        t.setStyle(TableStyle(style))
        Elements.append(t)

        IO = StringIO.StringIO()
        doc = SimpleDocTemplate(IO)
        doc.build(Elements)
        buf = IO.getvalue()
        IO.close()
        self.request.response.setHeader("Content-Disposition", "attachment; filename=%s.pdf" % self.getReportFileName())
        self.request.response.setHeader("Content-Type", "application/pdf")
        return buf

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
