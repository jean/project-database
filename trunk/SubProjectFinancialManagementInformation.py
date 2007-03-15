## easy way to import most relevant symbols
from Products.CMFCore import CMFCorePermissions
from Products.Archetypes.public import *
from config import *
from Products.ProjectDatabase.schemata import *
from Products.ATExtensions.Extensions.utils import getDisplayList, makeDisplayList


## BaseSchema provides title and all metadata stuff (i.e. expiration date)
#schema = SupplementalCoreSchema + SupplementalBudgetSchema + SupplementalAgencySchema 

	      	


## the final class definition. Deriving from BaseContent does most of the
## tricky work. Just let our schema be the schema for this content type.
    
class SubProjectFinancialManagementInformation(BaseFolder):
    """ Information about the milestone dates for the project
        """
    global_allow = 0
    portal_type = 'SubProjectFinancialManagementInformation'
    
    filter_content_types = 1
    allowed_content_types = ['CofinancingCash','CofinancingInKind','CashDisbursement','IMISExpenditure','Reports']
    schema = SupplementalCoreSchema + SupplementalBudgetSchema + SupplementalAgencySchema + SubProjectCodeSchema + Schema(
    	      (
                ComputedField('suppl_cash_cofinance_planned',
			      expression="context.Finance_vals('Cash_cofinance_planned')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )			      
                ),
                
                ComputedField('suppl_cash_cofinance_actual',
			      expression="context.Finance_vals('Cash_cofinance_actual')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )			      
                ),
                
                ComputedField('suppl_inkind_cofinance_planned',
			      expression="context.Finance_vals('Inkind_cofinance_planned')",
			      widget=ComputedWidget(
			      visible={'view': 'invisible',
                                       'edit': 'invisible'}
                              )			      
                ),
                
                ComputedField('suppl_inkind_cofinance_actual',
			      expression="context.Finance_vals('Inkind_cofinance_actual')",
			      widget=ComputedWidget(
			      visible={'view': 'invisible',
                                       'edit': 'invisible'}
                              )			      
                ),
                
                ComputedField('suppl_cash_disbursements',
			      expression="context.Finance_vals('Cash_disbursements')",
			      widget=ComputedWidget(
			      visible={'view': 'invisible',
                                       'edit': 'invisible'}
                              )			      
                ),
                
                ComputedField('suppl_imis_expenditures',
			      expression="context.Finance_vals('Imis_expenditures')",
			      widget=ComputedWidget(
			      visible={'view': 'invisible',
                                       'edit': 'invisible'}
                              )			      
                ), 

                ComputedField('sub_project_reports',
			      expression="context.Reports_Summary()",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),                


              ))
	    
    
    #get the controlled vocabulary
        
    # for the computed 'Finance values' field

    def Finance_vals(self,n):
     	"""sum of finance components"""
     	if n == 'Cash_cofinance_planned':
	    cash_vals = self.contentValues('CofinancingCash')
	elif n == 'Cash_cofinance_actual':
	    cash_vals = self.contentValues('CofinancingCash')
	elif n == 'Inkind_cofinance_planned':
	    cash_vals = self.contentValues('CofinancingInKind')
	elif n == 'Inkind_cofinance_actual':
	    cash_vals = self.contentValues('CofinancingInKind')
	elif n == 'Cash_disbursements':
	    cash_vals = self.contentValues('CashDisbursement')
	elif n == 'Imis_expenditures':
	    cash_vals = self.contentValues('IMISExpenditure')
	else:
	    cash_vals = self.contentValues('CofinancingCash')
	   
     	sum_of_cash_val = 0.0
     	
     	for cash_val in cash_vals:
     	    if n == 'Cash_cofinance_planned':
     	    	sum_of_cash_val += float(cash_val.getPlanned_amount())
     	    elif n == 'Cash_cofinance_actual':
     	    	sum_of_cash_val += float(cash_val.getActual_amount())
     	    elif n == 'Inkind_cofinance_planned':
     	    	sum_of_cash_val += float(cash_val.getPlanned_amount())
     	    elif n == 'Inkind_cofinance_actual':
     	    	sum_of_cash_val += float(cash_val.getActual_amount())
     	    elif n == 'Cash_disbursements':
     	    	sum_of_cash_val += float(cash_val.getCash_disbursement_amount())
	    elif n == 'Imis_expenditures':
     	    	sum_of_cash_val += float(cash_val.getImis_expenditure_amount())     	    	
     	
	return sum_of_cash_val

 
    def Reports_Summary(self):
        """sum of finance components"""
        report_vals = self.contentValues('Reports')
    
        str_val = ''
    
        for report_val in report_vals:
            str_val += report_val.Title() +": "
            str_val += report_val.getReport_period() +": "
    	    str_val += report_val.getReport_received() + "<br /><br />"
    
    	return str_val     	
    
## important step: register the class as an archetype, so all of the 
## archetypes machinery will know it exists.

registerType(SubProjectFinancialManagementInformation, PROJECTNAME)    	
