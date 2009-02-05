class Report:

    def __init__(self, name, **kw):
        self.name = name
        self.params = kw

        self.data = {
                'report_headers':[],
                'table_headers':[[]],
                'table_rows':[[]],
                'table_totals':[[]],
                'report_footers':[]
                }

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
