from MnEStatusReportFactory import MnEStatusReportFactory

class MidTermEvaluationStatusReportFactory(MnEStatusReportFactory):

    def __init__(self, context):
        self.context = context
        self.evaluationType = 'MTE'
        self.name = "Mid-term Evaluation Status Report"
