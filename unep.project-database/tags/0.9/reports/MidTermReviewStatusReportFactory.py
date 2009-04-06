from MnEStatusReportFactory import MnEStatusReportFactory

class MidTermReviewStatusReportFactory(MnEStatusReportFactory):

    def __init__(self, context, **kwargs):
        self.context = context
        self.evaluationType = 'MTR'
        self.name = "Mid-term Review Status Report"
        self.params = kwargs

