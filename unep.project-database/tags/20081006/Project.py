""" 
Project definition
Projects are contained within a 'ProjectDatabase'
A Project is a combination of many schema defined in the schemata file.
Projects are folderish types and they can contain other objects within them.
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"
    
    
# import schema definitions
from Products.ProjectDatabase.schemata import *
# from Products.ProjectDatabase.permissions import *

# functions used to display lists 
from Products.ATExtensions.extensions_utils import getDisplayList, makeDisplayList

# Project class definition - it is a folderish type

class Project(BaseFolder):
	
    global_allow =0
    portal_type = 'Project'

    # restrict the content types that can be added to a Project

    filter_content_types = 1
    allowed_content_types = ['ProjectImplementation', 'FinancialManagementInformation', 'MilestoneDates', 'SubProject']

    # define the Project schema = schema from the schemata file + some computed fields (calculated on the fly)
    # the functions for the computed fields can be found after the class definition    
    
    schema = ProjectBaseInfoSchema + DescriptionSchema + FocalAreaSchema + CountrySchema + ProjectSchema + AgencySchema + ImplementationModeSchema + UrlSchema + ContactsSchema + CoordinatorSchema + MidTermReviewSchema + TerminalEvaluationSchema + LeveragedFinancingSchema + ResultsSchema + Schema(
    	      (
    		
    		ComputedField('total_gef_allocation',
			      expression="context.Total_Finance_vals('Total_gef_allocation')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
                
    		ComputedField('total_unep_allocation',
			      expression="context.Total_Finance_vals('Total_unep_allocation')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
    		
    		ComputedField('total_cofinancing_actual',
			      expression="context.Total_Finance_vals('Cofinancing_actual')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
                
    		ComputedField('total_cofinancing_planned',
			      expression="context.Total_Finance_vals('Cofinancing_planned')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ), 
                
                ComputedField('total_cash_disbursements',
			      expression="context.Total_Finance_vals('Total_Disbursements')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
                
                ComputedField('total_imis_expenditures',
			      expression="context.Total_Finance_vals('Total_Expenditures')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
                
                ComputedField('pdfa_status',
			      expression="context.Status_Values('Pdfa_Status')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
                                
                
                ComputedField('pdfb_status',
			      expression="context.Status_Values('Pdfb_Status')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
                
                ComputedField('msp_status',
			      expression="context.Status_Values('Msp_Status')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),
                
                ComputedField('fsp_status',
			      expression="context.Status_Values('Fsp_Status')",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),

                ComputedField('project_title',
			      expression="context.Project_Title()",
			      widget=ComputedWidget(
			      visible={'view': 'visible',
                                       'edit': 'invisible'}
                              )
                ),   
                
              ))                

	
    # override the default views and actions from Archetypes
    
    actions = (
                {
            	'id': 'overview',
            	'name': 'Overview',
            	'action': 'string:${object_url}/Project_overview',
            	'permissions': (ViewProjects,),
            	'visible':1,
                },    
                {
            	'id': 'view',
            	'name': 'Project Core',
            	'action': 'string:${object_url}/Project_Core_view',
            	'permissions': (ViewProjects,),
            	'visible':1,
                },
                {
            	'id': 'financialmgmtinfo',
            	'name': 'Financial Management Information',
            	'action': 'string:${object_url}/fmi_view',
            	'permissions': (ViewProjects,),
            	'visible':1,
                },
                {
                'id': 'milestonedates',
                'name': 'Milestone Dates',
                'action': 'string:${object_url}/Milestone_view',
                'permissions': (ViewProjects,),
                'visible':1,
                },
                {
            	'id': 'pjdocs',
            	'name': 'Project Documents',
            	'action': 'string:${object_url}/Project_Doc_view',
            	'permissions': (ViewProjects,),
            	'visible':1,
                },                 
                {
    	    	'id': 'local_roles',
    	    	'name': 'Sharing',
    	    	'action': 'string:${object_url}/folder_localrole_form',
    	    	'permissions': (CMFCorePermissions.ManageProperties)
                },
        )
 
    # functions for the computed fields - Each function is called from the relevant computed field definition    
        
    def Total_Finance_vals(self,n):
     	"""sum of finance components"""
     	supplementary_cash_vals = self.contentValues('FinancialManagementInformation')
     	subproject_cash_vals = self.contentValues('SubProject')
     	
     	sum_of_cash_val = 0.0
     	
     	for cash_val in supplementary_cash_vals:
     	    if n == 'Cofinancing_actual':
     	    	sum_of_cash_val +=float(cash_val.getSum_cofin_cash_actual())
     	    	sum_of_cash_val += float(cash_val.getSum_cofin_inkind_actual())
     	    elif n == 'Cofinancing_planned':
     	    	sum_of_cash_val += float(cash_val.getSum_cofin_cash_planned())
     	    	sum_of_cash_val += float(cash_val.getSum_cofin_inkind_planned())
     	    elif n == 'Total_Disbursements':
     	    	sum_of_cash_val += float(cash_val.getSum_cash_disbursements())
     	    elif n == 'Total_Expenditures':
     	    	sum_of_cash_val += float(cash_val.getSum_imis_expenditures())
     	    elif n == 'Total_gef_allocation':
                try:
     	    	  sum_of_cash_val += float(cash_val.getGef_project_allocation())
                except:
		  pass
     	    elif n == 'Total_unep_allocation':
     	    	sum_of_cash_val += float(cash_val.getCash_unep_allocation())
     	    	
     	for cash_val in subproject_cash_vals:
     	    if n == 'Total_cost_actual':
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_cash_actual())
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_inkind_actual())
     	    	sum_of_cash_val += float(cash_val.getSub_project_allocation())
     	    elif n == 'Total_cost_planned':
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_cash_planned())
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_cash_actual())
     	    	sum_of_cash_val += float(cash_val.getSub_project_allocation())
     	    elif n == 'Cofinancing_actual':
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_cash_actual())
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_inkind_actual())
     	    elif n == 'Cofinancing_planned':
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_cash_planned())
     	    	sum_of_cash_val += float(cash_val.getSub_project_cofin_inkind_planned())     	   
     	    elif n == 'Total_Disbursements':
     	    	sum_of_cash_val += float(cash_val.getSub_project_cash_disbursements())
     	    elif n == 'Total_Expenditures':
     	    	sum_of_cash_val += float(cash_val.getSub_project_imis_expenditures())
     	    elif n == 'Total_gef_allocation':
                try:
     	    	  sum_of_cash_val += float(cash_val.getGef_project_allocation())
                except:
                  pass
     	    
     	    
     	
	return sum_of_cash_val   
	
    def Status_Values(self,n):
     	"""sum of finance components"""
        status_vals = self.contentValues('FinancialManagementInformation')
    
        str_status = ''
        
        for status_val in status_vals:
     	    if n == 'Pdfa_Status':
     	    	if status_val.getFinance_category() =='PDF A':
     	    		str_status = status_val.getStatus()
     	    elif n == 'Pdfb_Status':
     	    	if status_val.getFinance_category() =='PDF B':
     	    		str_status = status_val.getStatus()
     	    elif n == 'Msp_Status':
     	    	if status_val.getFinance_category() =='MSP':
     	    		str_status = status_val.getStatus()
     	    elif n == 'Fsp_Status':
     	    	if status_val.getFinance_category() =='FSP':
     	    		str_status = status_val.getStatus()
     	return str_status 
     	

    def Project_Title(self):
        """sum of finance components"""
        project_vals = self.contentValues('FinancialManagementInformation')
    
        start_date_val = ''
        start_date_val_comp = ''
        r_str = ''
    
        for project_val in project_vals:
            start_date_val = project_val.getStart_date()
            if start_date_val_comp == '':
	    	start_date_val_comp = project_val.getStart_date()
	    	r_str = project_val.Title()
            else:
            	if start_date_val > start_date_val_comp:
            		start_date_val_comp = start_date_val
            		r_str = project_val.Title()
  	return r_str     	

           	
    def getCountryVocabulary(self):
	return getDisplayList(self, 'country_names')
	
# register the class 'Project' with our product

registerType(Project, PROJECTNAME)
