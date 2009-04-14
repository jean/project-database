from FMIReceivablesReportFactory import FMIReceivablesReportFactory
from Report import Report

class EEAReceivablesReportFactory(FMIReceivablesReportFactory):
    def getReport(self):
        return FMIReceivablesReportFactory.getReport(self, 'EEA Receivables Report', 'eea')
