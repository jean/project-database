from FMIReceivablesReportFactory import FMIReceivablesReportFactory
from Report import Report
from Products.ProjectDatabase.content.interfaces import ISubProject
from Products.ProjectDatabase.utils import inner_strip

class FSPReceivablesReportFactory(FMIReceivablesReportFactory):
    def getReport(self):
        return FMIReceivablesReportFactory.getReport(self, 'FSP Receivables Report', 'fsp')

    def getReportData(self, type):
        projects = self.params.get('projects', None)
        result = []

        for project in projects:
            if ISubProject.providedBy(project):
                # IMIS number
                imis_number = project.getIMISNumber()
               
                # Lead exec agency names
                exec_agencies = project.getLeadExecutingAgencyNames()
                
                # Grant total
                grant = inner_strip(project.getCommittedGrant())

                # Cash disbursement total
                disbursement = inner_strip(project.getSumCashDisbursements())
                # Yearly expenditures
                expenditures = inner_strip(project.getSumYearlyExpenditures())
                # Amount Receivable
                receivable = inner_strip(project.getAmountReceivable())

                # project title
                title = project.Title()
            else:
                # We assume there can only be one 'FSP' object, since
                # the Financial object create code guarentees that.
                fsp = project.fmi_folder.get('fsp', None)
                # This check should not be necessary since the search that
                # supplies the projects should not give me useless projects.
                # TODO: Refactor the search code!
                if fsp is not None:
                    # IMIS number
                    imis_number = fsp.getIMISNumber()
                    
                    # Lead exec agency names
                    exec_agencies = project.project_general_info.getLeadExecutingAgencyNames()
                    # Grant total
                    grant = inner_strip(fsp.getCommittedGEFGrant())

                    # Cash disbursement total
                    disbursement = inner_strip(fsp.getSumCashDisbursements())
                    # Yearly expenditures
                    expenditures = inner_strip(fsp.getSumYearlyExpenditures())
                    # Amount Receivable
                    receivable = inner_strip(fsp.getAmountReceivable())
            
                    # project title
                    title = project.project_general_info.Title()

            result.append((
                imis_number,
                title,
                exec_agencies,
                grant,
                disbursement,
                expenditures,
                receivable,
                ))

        return result
