from MnEStatusReportFactory import MnEStatusReportFactory

class MidTermReviewStatusReportFactory(MnEStatusReportFactory):

    def __init__(self, context):
        self.context = context
        self.evaluationType = 'MTR'
        self.name = "Mid-term Review Status Report"

