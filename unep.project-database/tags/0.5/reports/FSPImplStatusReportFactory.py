from Report import Report
from FMIImplStatusReportFactory import FMIImplementationStatusReportFactory

class FSPImplementationStatusReportFactory(FMIImplementationStatusReportFactory):

    def getReport(self):
        # create and fill the report
        return FMIImplementationStatusReportFactory.getReport(self, 
            'FSP Implementation Status Report', 'fsp')
