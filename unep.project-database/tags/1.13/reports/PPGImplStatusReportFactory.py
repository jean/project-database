from Report import Report
from FMIImplStatusReportFactory import FMIImplementationStatusReportFactory

class PPGImplementationStatusReportFactory(FMIImplementationStatusReportFactory):

    def getReport(self):
        return FMIImplementationStatusReportFactory.getReport(self, 'PPG Implementation Status Report', 'ppg')
