class Report:

    def __init__(self, context, name, **kw):
        self.name = name
        self.params = kw

        self.report_headers = []
        self.table_headers = [[]]
        self.table_rows = [[]]
        self.table_totals = [[]]
        self.report_footers = []

    def getReportHeaders(self):
        return self.data['report_headers']

    def getTableHeaders(self):
        return self.data['table_headers']

    def getTableRows(self):
        return self.data['table_rows']

    def getTableTotals(self):
        return self.data['table_totals']

    def getReportFooters(self):
        return self.data['report_footers']

    def buildReportData(self):
        pass
