from FMIReceivablesReportFactory import FMIReceivablesReportFactory
from Report import Report

class MSPReceivablesReportFactory(FMIReceivablesReportFactory):
    def getReport(self):
        return FMIReceivablesReportFactory.getReport(self, 'MSP Receivables Report', 'msp')
