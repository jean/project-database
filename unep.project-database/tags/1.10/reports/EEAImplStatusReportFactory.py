from Report import Report
from FMIImplStatusReportFactory import FMIImplementationStatusReportFactory

class EEAImplementationStatusReportFactory(FMIImplementationStatusReportFactory):

    def getReport(self):
        # create and fill the report
        return FMIImplementationStatusReportFactory.getReport(self,
            'EEA Implementation Status Report', 'eea')
