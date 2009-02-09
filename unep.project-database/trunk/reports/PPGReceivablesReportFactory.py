from FMIReceivablesReportFactory import FMIReceivablesReportFactory
from Report import Report

class PPGReceivablesReportFactory(FMIReceivablesReportFactory):
    def getReport(self):
        return FMIReceivablesReportFactory.getReport(self, 'PPG Receivables Report', 'ppg')
