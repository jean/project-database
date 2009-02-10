from Report import Report
from FMIImplStatusReportFactory import FMIImplementationStatusReportFactory

class MSPImplementationStatusReportFactory(FMIImplementationStatusReportFactory):

    def getReport(self):
        # create and fill the report
        return FMIImplementationStatusReportFactory.getReport(self, 'MSP Implementation Status Report', 'msp')
