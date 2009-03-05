from Report import Report
from Products.CMFCore.utils import getToolByName
from Products.ProjectDatabase.utils import *

class ProjectRatingsReportFactory(object):

    def __init__(self, context, **kw):
        self.params = kw
        self.project = context
        self.pgi = context.project_general_info
        self.mande = context.mne_folder
        self.pirs = self.mande.objectValues(spec='PIRRating')
        pc = getToolByName(context, 'portal_catalog')
        mtre = pc(portal_type = 'MonitoringAndEvaluation',
                    getEvaluationType = ('MTR', 'MTE',),
                    path = '/'.join(self.mande.getPhysicalPath()))
        if len(mtre) > 0:
            self.mtre = mtre[0].getObject()
        else:
            self.mtre = None
        te = pc(portal_type = 'MonitoringAndEvaluation',
                    getEvaluationType = 'TE',
                    path = '/'.join(self.mande.getPhysicalPath()))
        if len(te) > 0:
            self.te = te[0].getObject()
        else:
            self.te = None

    def getReport(self):
        # create and fill the report
        name = "Project Ratings Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        report.setTableHeaders((self.getTableHeaders(),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        result = []
        
        # --------- Project Objectives --------------------------------------
        row = ['Project Objectives']
        for pir in self.pirs:
            row.append(
                    getVocabularyValue(self.project, \
                        'Rating', pir.getDevelopmentObjective()),)
        if self.mtre:
            row.append(self.mtre.getEvaluationCriterionRatings('Project Objectives')[0])
        else:
            row.append('')
        if self.te:
            row.extend(list(self.te.getEvaluationCriterionRatings('Project Objectives')))
        else:
            row.extend(['', '', ''])
        result.append(row)

        # --------- Implementation Progress ----------------------------------
        row = ['Implementation Progress']
        for pir in self.pirs:
            row.append(
                    getVocabularyValue(self.project, \
                        'Rating', pir.getImplementationProgress()),)
        if self.mtre:
            row.append(self.mtre.getEvaluationCriterionRatings('Implementation Progress')[0])
        else:
            row.append('')
        row.extend(['N/A', 'N/A', 'N/A'])
        result.append(row)
        
        # --------- Monitoring and Evaluation --------------------------------------
        row = ['Monitoring and Evaluation']
        for pir in self.pirs:
            row.append(
                    getVocabularyValue(self.project, \
                        'Rating', pir.getMonitoringAndEvaluation()),)
        if self.mtre:
            row.append(self.mtre.getEvaluationCriterionRatings('Monitoring and Evaluation')[0])
        else:
            row.append('')
        if self.te:
            row.extend(list(self.te.getEvaluationCriterionRatings('Monitoring and Evaluation')))
        else:
            row.extend(['', '', ''])
        result.append(row)

        # --------- Risk ----------------------------------
        row = ['Risk']
        for pir in self.pirs:
            row.append(
                    getVocabularyValue(self.project, \
                        'RiskLevel', pir.getProjectRisk()),)
        if self.mtre:
            row.append(self.mtre.getEvaluationCriterionRatings('Risk')[0])
        else:
            row.append('')
        row.extend(['N/A', 'N/A', 'N/A'])
        result.append(row)

        # --------- Project Outputs and Activities ----------------------------------
        rowheads = [
                'Project Outputs and Activities',
                'Sustainability of Outcomes',
                'Catalytic Role',
                'Preparation and Readiness',
                'Stakeholder Involvement',
                'Country Ownership',
                'Financial Planning',
                'UNEP Supervision and Backstopping',
                'Overall Rating',
                ]
        for head in rowheads:
            row = [head]
            for pir in self.pirs:
                row.append('N/A')
            if self.mtre:
                row.append(self.mtre.getEvaluationCriterionRatings(head)[0])
            else:
                row.append('')
            if self.te:
                row.extend(list(self.te.getEvaluationCriterionRatings(head)))
            else:
                row.extend(['', '', ''])
            result.append(row)

        return result


    def getTableHeaders(self):
        """
        See how many PIR reports, and add column headings
        """
        headers = ['']
        for pir in self.pirs:
            headers.append('PIR %s' % pir.getFiscalYear())
        headers.append('MTR/MTE Rating')
        headers.append('TE Rating')
        headers.append('UNEP EOU Rating')
        headers.append('GEF EO Rating')
        return tuple(headers)

