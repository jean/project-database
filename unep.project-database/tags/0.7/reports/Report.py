class Report(object):

    def __init__(self, name):
        self.name = name

        self.report_headers = []
        self.table_headers = [[]]
        self.table_rows = [[]]
        self.table_totals = [[]]
        self.report_footers = []

    def getReportHeaders(self):
        return self.report_headers

    def getTableHeaders(self):
        return self.table_headers

    def getTableRows(self):
        return self.table_rows

    def getTableTotals(self):
        return self.table_totals

    def getReportFooters(self):
        return self.report_footers

    def setReportHeaders(self, headers):
        self.report_headers = headers

    def setTableHeaders(self, headers):
        self.table_headers = headers

    def setTableRows(self, rows):
        self.table_rows = rows

    def setTableTotals(self, totals):
        self.table_totals = totals

    def setReportFooters(self, footers):
        self.report_footers = footers
