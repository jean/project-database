from Report import Report

def getDummyReport(context, **kw):
    report = Report("DummyReport", **kw)
    report.setReportHeaders(['Classy Financial Report', 'Proceedings of 555th Convention', 'Second Movement', 'Two Down'])
    report.setTableHeaders([['Date','Planned','Grant','Months'], ['Cleanup','Test', 'Size', 'Duration']])
    report.setTableRows([['2009-01-02','Tanzania','123','5'],
                         ['1652-04-12','Canada','456','4'],
                         ['1902-01-02','Egypt','789','3'],
                         ['1945-02-03','Britain','9999993453465','0']])
    report.setTableTotals([['Total','Country','Fifteen','Bob'],
                           ['','Name','Mice','Alice']])

    report.setReportFooters(['Rondo ala Turca', 'Piano concert nr. 40'])
    return report
