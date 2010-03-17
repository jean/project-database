from FMIReceivablesReportFactory import FMIReceivablesReportFactory
from Report import Report

class FSPReceivablesReportFactory(FMIReceivablesReportFactory):
    def getReport(self):
        return FMIReceivablesReportFactory.getReport(self, 'FSP Receivables Report', 'fsp')
