"""
SubProject definition
SubProjects are contained within a 'Project'
A SubProject is a combination of many schema defined in the schemata file.
SubProjects are folderish types and they can contain other objects within them.
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"


# import schema definitions
from Products.ProjectDatabase.schemata import *

# functions used to display lists
from Products.ATExtensions.extensions_utils import getDisplayList, makeDisplayList

# define the SubProject schema = schema from the schemata file + some computed fields (calculated on the fly)
# the functions for the computed fields can be found after the class definition	

schema = SubProjectBaseInfoSchema + DescriptionSchema + CountrySchema + ImplementationModeSchema + UrlSchema + CoordinatorSchema + SupplementalCoreSchema + SupplementalBudgetSchema + SupplementalAgencySchema + Schema(
              (
                ComputedField('sub_project_cofin_cash_actual',
                              expression="context.SPFinance_vals('Cash_cofinance_actual')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sub_project_cofin_cash_planned',
                              expression="context.SPFinance_vals('Cash_cofinance_planned')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sub_project_cofin_inkind_planned',
                              expression="context.SPFinance_vals('Inkind_cofinance_planned')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sub_project_cofin_inkind_actual',
                              expression="context.SPFinance_vals('Inkind_cofinance_actual')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sub_project_cash_disbursements',
                              expression="context.SPFinance_vals('Cash_disbursements')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ),

                ComputedField('sub_project_imis_expenditures',
                              expression="context.SPFinance_vals('Imis_expenditures')",
                              widget=ComputedWidget(
                              visible={'view': 'invisible',
                                       'edit': 'invisible'}
                             )
                ), 
            
              ))


# SubProject class definition - it is a folderish type

class SubProject(BaseFolder):

    global_allow =0
    portal_type = 'SubProject'

    # restrict the content types that can be added to a Project
    
    filter_content_types = 1
    allowed_content_types = ['ProjectImplementation']
    schema = schema  
    
    
    # functions for the computed fields - Each function is called from the relevant computed field definition
    
    def SPFinance_vals(self,n):
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
           
        return sum_of_cash_vals

   #  def getDONOR_TYPES(self):
        # return DONOR_TYPE

   # def getREPORT_TYPES(self):
        # return REPORT_TYPE

# register the class 'SubProject' with our product
registerType(SubProject, PROJECTNAME)
