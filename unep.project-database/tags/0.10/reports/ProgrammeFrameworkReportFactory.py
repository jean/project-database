from Report import Report
from Products.ProjectDatabase.utils import inner_strip, unep_report_format_date
from Products.CMFCore.utils import getToolByName

class ProgrammeFrameworkReportFactory(object):

    def __init__(self, context, **kw):
        self.context = context
        self.params = kw

    def getReport(self):
        # create and fill the report
        name = "Programme Framework Report"
        report = Report(name)
        report.setReportHeaders(( name,),)
        #report.setTableHeaders(((
        #    ),))
        report.setTableRows(self.getReportData())
        # report.setTableTotals([])
        # report.setReportFooters()
        return report

    def getReportData(self):
        results = []
        frameworks = self.context. \
            frameworkdatabase.objectValues(spec='ProgrammeFramework')
        refcat = getToolByName(self.context, 'reference_catalog')
        for framework in frameworks:
            row = []
            relationships = refcat.getBackReferences(
                framework.UID(), 
                relationship='project_programmeframework')
            row.extend(['Title', framework.Title()])
            row.extend(['PFD Short Title', framework.getPFDShortTitle()])
            row.extend(['SPO', framework.getSPOName()])
            row.extend(['Lead Agency', framework.getLeadAgency()])
            row.extend(['Deadline', framework.getProjectSubmissionDeadline()])
            row.append('')
            results.append(row)
            row = ('DBase ID', 'GEF ID', 'IMIS No', 'Title', 'Country(ies)', \
                    'TM', 'FMO', 'PIF Submission Date', \
                    'Expected CEO Endorsement', \
                    'Actual CEO Endorsement', 'Status')
            results.append(row)
            for rel in relationships:
                pgi = refcat.lookupObject(rel.sourceUID)
                project = pgi.getAProject()
                mofu = project.fmi_folder.getMainFinanceObject()
                ms = project.milestones
                if mofu and project.isTheProjectPublished():
                    results.append((
                        project.getId(),
                        pgi.getGEFid(),
                        mofu.getIMISNumber(),
                        pgi.Title(),
                        pgi.getCountryNames(),
                        pgi.getCurrentTM(),
                        mofu.getCurrentPrincipalFMO(),
                        unep_report_format_date(project, \
                            ms.getPIFApprovalDate('SubmissionToGEFSec')),
                        unep_report_format_date(project, \
                            ms.getProjectApprovalDate(\
                                    'CEOApprovalEndorsementExpected')),
                        unep_report_format_date(project, \
                            ms.getProjectApprovalDate( \
                                    'CEOApprovalEndorsementActual')),
                        ms.getProjectStage()
                        ))
            results.append(['--', '--','--', '--','--', '--','--', '--',\
                            '--', '--','--'])
        return results
