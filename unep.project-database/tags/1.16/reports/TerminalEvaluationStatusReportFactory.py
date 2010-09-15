from MnEStatusReportFactory import MnEStatusReportFactory

class TerminalEvaluationStatusReportFactory(MnEStatusReportFactory):

    def __init__(self, context, **kw):
        self.context = context
        self.evaluationType = 'TE'
        self.name = "Terminal Evaluation Status Report"
        self.params = kw
