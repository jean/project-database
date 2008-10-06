"""
FinancialManagementInformation definition (FMI)
Each project has financial section which is represented by the FMI
The FMI is a combination of many schema defined in the schemata file.
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"


# import schema definitions
from Products.ProjectDatabase.schemata import *

# FMI class definition - it is a folderish type
class FinancialManagementInformation(BaseFolder):

    global_allow = 0
    portal_type = 'FinancialManagementInformation'

    # restrict the content types that can be added to FMI (none can be added)
    filter_content_types = 1

    # define the FMI schema = schema from the schemata file + some computed fields (calculated on the fly)
    # the functions for the computed fields can be found after the class definition
	
    schema = SupplementalCoreSchema + SupplementalFinanceSchema + SupplementalBudgetSchema + SupplementalAgencySchema + SupplementalFinalSchema + Schema(
              (
                ComputedField('sum_cofin_cash_planned',
                              expression="context.Finance_vals('Cash_cofinance_planned')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sum_cofin_cash_actual',
                              expression="context.Finance_vals('Cash_cofinance_actual')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sum_cofin_inkind_planned',
                              expression="context.Finance_vals('Inkind_cofinance_planned')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sum_cofin_inkind_actual',
                              expression="context.Finance_vals('Inkind_cofinance_actual')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sum_cash_disbursements',
                              expression="context.Finance_vals('Cash_disbursements')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sum_imis_expenditures',
                              expression="context.Finance_vals('Imis_expenditures')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ), 

                ComputedField('cash_unep_allocation',
			      expression="context.Finance_vals('Cash_unep_allocation')",
			      widget=ComputedWidget(
			      visible={'view': 'invisible',
                                       'edit': 'invisible'}
                              )			      
                ),                
              ))

    # override the default views and actions from Archetypes

    actions = (
                {
                'id': 'view',
                'name': 'View',
                'action': 'string:${object_url}/fmi_view',
                'permissions': (ViewProjects,),
                'visible':1,
                },
              )

    # functions for the computed fields - Each function is called from the relevant computed field definition
        
    def Finance_vals(self,n):
        sum_of_cash_vals = 0.0
        if n == 'Cash_cofinance_planned':
            cash_vals = self.getCofinancing_cash()
            for cash_val in cash_vals:
                sum_of_cash_vals += float(cash_val['cofinancing_cash_planned_amount'])
        elif n == 'Cash_cofinance_actual':
            cash_vals = self.getCofinancing_cash()
            for cash_val in cash_vals:
                sum_of_cash_vals += float(cash_val['cofinancing_cash_actual_amount']) 
        elif n == 'Inkind_cofinance_planned':
            cash_vals = self.getCofinancing_inkind()
            for cash_val in cash_vals:
                sum_of_cash_vals += float(cash_val['cofinancing_inkind_planned_amount']) 
        elif n == 'Inkind_cofinance_actual':
            cash_vals = self.getCofinancing_inkind()
            for cash_val in cash_vals:
                sum_of_cash_vals += float(cash_val['cofinancing_inkind_actual_amount'])      
        elif n == 'Cash_disbursements':
            cash_vals = self.getCash_disbursements()
            for cash_val in cash_vals:
                sum_of_cash_vals += float(cash_val['cash_disbursements_amount'])  
        elif n == 'Imis_expenditures':
            cash_vals = self.getImis_expenditures()
            for cash_val in cash_vals:
                sum_of_cash_vals += float(cash_val['imis_expenditure_amount']) 
        elif n == 'Cash_unep_allocation':
            sum_of_cash_vals = 0.0
            try: 
                sum_of_cash_vals += float(self.getGef_trust_fund())
            except: pass
            try:    
	        sum_of_cash_vals += float(self.getLdc_fund_allocation())
            except: pass
            try:
	        sum_of_cash_vals += float(self.getSccf_allocation())
            except: pass
            try:
	        sum_of_cash_vals += float(self.getStrategic_partnership())
            except: pass
            try:
                sum_of_cash_vals += float(self.getAdaptation_trust_fund())
            except: pass            
           
        return sum_of_cash_vals
 
       
    def getDONOR_TYPES(self):
        return DONOR_TYPE
 
    def getREPORT_TYPES(self):
        return REPORT_TYPE
	
  
# register the class 'Financial Management Information' with our product

registerType(FinancialManagementInformation, PROJECTNAME)    	
