"""
Contains field definitions that can be used for different schema.
Add new field definitions here.
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"


# Import field types, widgets and base schema from Archetypes
from Products.Archetypes.public import *

# Import list definitions from the config file
from config import *
from permissions import *

# Another widget import
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import *

# Import the DataGrid Field and DataGridWidget
from Products.DataGridField import *

#Define the basic view
BaseInfoSchema = BaseSchema.copy()

#Field definitions - Each field is placed within the logical schema definition

ProjectBaseInfoSchema = BaseInfoSchema + Schema(
	(
    	StringField('title',
		required=0,
		searchable=1,
		accessor='Title',
		index='FieldIndex:brains',
		widget=StringWidget(
		label="GEF Project Id",
                description="GEF Secretariat Id",
		),
		),

	))

SubProjectBaseInfoSchema = BaseInfoSchema + Schema(
	(
    	StringField('title',
		required=1,
		searchable=0,
		accessor='Title',
		index='FieldIndex:brains',
		widget=StringWidget(
		label="Title",
                description="Enter Project Title",
		#visible={'edit':'hidden'},
		#visible = -1,
		),
		),
	))
	
	
	
DescriptionSchema = Schema(
	(
	TextField('summary_project_description',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		allowable_content_types=('text/x-web-intelligent',),
                default_content_type="text/x-web-intelligent",
                default_output_type="text/html",
		widget=TextAreaWidget(
        	label="Project Description",
                description="Enter Project Description",
		rows=8)
	      	),
	))

FocalAreaSchema	 = Schema(
	(
	StringField('focal_area',
		searchable=1,
		required=1,
		vocabulary = FOCAL_AREAS,
		index='FieldIndex:brains',
		widget=SelectionWidget(
		label="Focal Areas",
                description="Select Focal Area")
		),
	))


CountrySchema	 = Schema(
	(
 	StringField('scope',
		searchable=1,
		default='',
		required=0,
		vocabulary = SCOPE,
		index='FieldIndex:brains',
		widget = SelectionWidget(
		label = "Geographic Scope",
                description= "Select Geographic Scope",
		format="radio")
              	),
              	
        StringField('region',
		searchable=1,
		default='',
		required=0,
		vocabulary = REGION,
		index='FieldIndex:brains',
		widget = SelectionWidget(
		label = "Geographic Region",
                description ="Select Geographic Region",
		format="radio")
              	),

	LinesField('country',
		searchable=1,
		required=0,
		vocabulary = 'getCountryVocabulary',
		index='KeywordIndex:brains',
		widget=PicklistWidget(
		label="Countries",
                description="Select participating countries")
		),	
	))

ProjectSchema = Schema(
	(
	StringField('operational_programme',
		searchable=1,
		required=0,
		vocabulary = OPERATIONAL_PROGRAMMES,
		index='KeywordIndex:brains',
		widget = MultiSelectionWidget(
		label = "GEF Operational Programme",
                description ="Select Operational Programmes",
		format="checkbox")
		),
		
	StringField('strategic_priority',
		searchable=1,
		required=0,
		vocabulary = STRATEGIC_PRIORITIES,
		index='KeywordIndex:brains',
		widget = MultiSelectionWidget(
		label = "GEF Strategic Priority",
                description ="Select Strategic Priorities",
		format="checkbox")
		),
		
	StringField('project_type',
	        searchable=1,
		required=0,
		vocabulary=PROJECT_TYPES,
		index='FieldIndex:brains',
		widget=SelectionWidget(
		label = "Project Type",
                description ="Select Project Type")
                ),
              
                 
           
	StringField('pipeline_number',
	        searchable=1,
		required=0,
		vocabulary=PIPELINE_NUMBERS,
		index='FieldIndex:brains',
		widget=SelectionWidget(
		label = "Pipeline Number",
                description ="Select a pipeline number between 1 and 50")
                ),
	
	))
	
	

AgencySchema	 = Schema(
	(
        StringField('leadagency',
		searchable=1,
		required=0,
		vocabulary = LEAD_AGENCY,
		index='FieldIndex:brains',
		widget = SelectionWidget(
		label = "Lead Implementing Agency",
                description = "Select a Lead Implementing Agency")
		),
						    
	ReferenceField('other_implementing_agency', 
			allowed_types=('mxmContactsOrganization'),
			multiValued=1,
			relationship='oia',
			required=0,
			widget=ReferenceBrowserWidget(allow_search=1, 
						 allow_browse=0,
						 show_indexes=1, 
						 label="Other Implementing Agencies",
						 available_indexes={'SearchableText':'Free text search'},
				    description='Select Other Implementing Agencies.')) ,
	
			    
	TextField('unep_component_description',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
                        allowable_content_types=('text/x-web-intelligent',),
                        default_content_type="text/x-web-intelligent",
                        default_output_type="text/html",
			widget=TextAreaWidget(
			label="Description of UNEP components",
                        description = "Enter a description of the UNEP components",
			rows=8)
		),

        StringField('gef_phase',
		searchable=1,
		required=0,
		vocabulary = GEF_PHASE,
		index='FieldIndex:brains',
		widget = SelectionWidget(
		label = "Gef Phase",
                description = "Select GEF Phase")
		),

		
	StringField('implementing_agency_fee',
		searchable=1,
		required=0,
		widget=StringWidget(
		label="Implementing Agency Fee",
                description ="Enter Implementing Agency Fee")
		),
		
	StringField('unep_ia_fee',
		searchable=1,
		required=0,
		widget=StringWidget(
		label="UNEP Implementing Agency Fee",
                description ="Enter UNEP Implementing Agency Fee")
		),	
	))


ImplementationModeSchema = Schema(
	(
	StringField('implementation_mode',
		required=0,
		searchable=1,
		index='FieldIndex:brains',
		vocabulary = IMPLEMENTATION_TYPE,
		widget=SelectionWidget(
		label="Mode",
                description="Select Mode")
		),

	StringField('office',
		searchable=0,
		required=0,
		index='FieldIndex:brains',
		widget=StringWidget(
		label="Office",
                description="Select Office")
		),	
	      	
	))


UrlSchema = Schema(
	(
	StringField('project_website_address',
		searchable=1,
		required=0,
		validators=("isUrl"),
		index='FieldIndex:brains',
		widget=StringWidget(
		label="Project Website Address",
                description = "Enter project website address"
		)), 
		
	      	
	))

	
ContactsSchema = Schema(
	(
	ReferenceField('current_task_manager', 
			allowed_types=('mxmContactsPerson'),
			multiValued=1,
			required=0,
		        relationship='ctm',
			widget=ReferenceBrowserWidget(allow_search=1, 
						 allow_browse=0,
						 show_indexes=1, 
						 label="Current Task Manager",
						 available_indexes={'SearchableText':'Free text search'},
						    description='Select Current Task Manager. <br><b>CAUTION: UNSELECTING A VALUE IN THE LIST BELOW WILL REMOVE THE LINK!!')) ,
	ReferenceField('previous_task_manager', 
			allowed_types=('mxmContactsPerson'),
			multiValued=1,
			required=0,
		        relationship='ptm',
			widget=ReferenceBrowserWidget(allow_search=1, 
						 allow_browse=0,
						 show_indexes=1, 
						 label="Previous Task Manager",
						 available_indexes={'SearchableText':'Free text search'},
						    description='Select Previous Task Manager.<br><b>CAUTION: UNSELECTING A VALUE IN THE LIST BELOW WILL REMOVE THE LINK')) ,
	
	      	
	))

CoordinatorSchema = Schema(
	(
	        
	ReferenceField('project_coordinator', 
		allowed_types=('mxmContactsPerson'),
		multiValued=1,
		required=0,
		relationship='pc',
		widget=ReferenceBrowserWidget(allow_search=1, 
					 allow_browse=0,
					 show_indexes=1, 
					 label="Project Coordinator",
					 available_indexes={'SearchableText':'Free text search'},
						    description='Select Project Coordinator.<br><b>CAUTION: UNSELECTING A VALUE IN THE LIST BELOW WILL REMOVE THE LINK')) ,
	
	      	
	))
	
	
MidTermReviewSchema = Schema(
	(
	DateTimeField('mid_term_review_report_date',
		required=0,
		searchable=1,
		index='DateIndex:brains',
		widget=CalendarWidget(
		label="Mid Term Review Report Date",
                description="Enter Mid Term Review Report Date",
                show_hm = False,
                format="%d-%m-%Y")
		),

	StringField('mid_term_review_evaluator_name',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=StringWidget(
		label="Name of consultant",
                description="Enter Mid Term Review Evaluator's name",)
		),

	DateTimeField('mid_term_review_planned_review_date',
		searchable=1,
		required=0,
		index='DateIndex:brains',
		widget=CalendarWidget(
		label="Planned Mid Term Review Date",
                description="Enter Planned Mid Term Review Date",
                show_hm = False)
		),

	DateTimeField('mid_term_review_actual_review_date',
		searchable=1,
		required=0,
		index='DateIndex:brains',
		widget=CalendarWidget(
		label="Actual Mid Term Review Date",
                description="Enter Actual Mid Term Review Date",
                show_hm = False)
		),	
	      	
	))
	

TerminalEvaluationSchema = Schema(
	(
	DateTimeField('terminal_evaluation_report_date',
		required=0,
		searchable=1,
		index='DateIndex:brains',
		widget=CalendarWidget(
		label="Terminal Evaluation Report Date",
                description="Enter Terminal Evaluation Report Date",
                show_hm = False)
		),

	StringField('terminal_report_evaluator_name',
		searchable=1,
		required=0,
		widget=StringWidget(
		label="Name of evaluator",
                description="Enter Terminal Report Evaluator name",)
		),

	DateTimeField('terminal_report_planned_evaluation_date',
		searchable=1,
		required=0,
		index='DateIndex:brains',
		widget=CalendarWidget(
		label="Planned Terminal Evaluation Date",
                description="Enter Planned Terminal Evaluation Date",
                show_hm = False)
		),

	DateTimeField('terminal_report_actual_evaluation_date',
		searchable=1,
		required=0,
		index='DateIndex:brains',
		widget=CalendarWidget(
		label="Actual Terminal Evaluation Date",
                description="Enter Actual Terminal Evaluation Date",
                show_hm = False)
		),	
	      	
	))
	

LeveragedFinancingSchema = Schema(
	(
	
    	FloatField('leveraged_financing_amount',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="Leveraged Financing Amount",
                description="Enter Leveraged Financing Amount",
		size=30)
		), 
			
	StringField('leveraged_financing_remark',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
                allowable_content_types=('text/x-web-intelligent',),
                default_content_type="text/x-web-intelligent",
                default_output_type="text/html",
		widget=TextAreaWidget(
		label="Leveraged Financing Remark",
                description="Enter Leveraged Financing Remark")
		),
	      	
	))
	

ResultsSchema = Schema(
	(
	TextField('project_results',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
                        allowable_content_tyeps=('text/x-web-intelligent',),
                        default_content_type="text/x-web-intelligent",
                        default_output_type="text/html",
			widget=TextAreaWidget(
			label="Overall Project Results",
                        description="Enter Overall Project Results",
			rows=8)
		),

		
	      	
	))	
	
	

SupplementalCoreSchema = BaseInfoSchema + Schema(
	(
    	StringField('title',
		required=1,
		searchable=1,
		accessor='Title',
		index='FieldIndex:brains',
		widget=StringWidget(
		label="Project Title",
		# visible={'edit':'hidden'},
		# visible = -1,
		),
		),

	StringField('finance_category',
		searchable=1,
		required=0,
		vocabulary = FINANCE_CATEGORY,
		index='FieldIndex:brains',
		widget=SelectionWidget(
		label="Finance Category",
                description="Select Finance Category")
		),
		
	StringField('pms_number',
	        searchable=1,
	        index='FieldIndex:brains',
		required=0,
		widget=StringWidget(
		label="PMS Number",
                description="Enter PMS Number")
	),
	
	StringField('imis_number',
	        searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=StringWidget(
		label="IMIS Number",
                description="Enter IMIS Number")
	),
	
    	FloatField('gef_project_allocation',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="Total GEF Allocation",
                description="Enter Total GEF Allocation",
		size=30)
	),
		
      	
	))


SupplementalFinanceSchema = Schema(
	(
    	FloatField('gef_trust_fund',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="GEF Trust Fund",
                description="Enter GEF Trust Fund Amount",
		size=30)
		),

    	FloatField('ldc_fund_allocation',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="LDC Fund Allocation",
                description="Enter LDC Fund Allocation",
		size=30)
		), 
			
    	FloatField('sccf_allocation',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="SCCF Allocation",
                description="Enter SCCF Allocation",
		size=30)
		), 

    	FloatField('strategic_partnership',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="Strategic Partnership",
                description="Strategic Partnership amount",
		size=30)
		),
			
    	FloatField('adaptation_trust_fund',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="Adaptation Trust Fund",
                description="Enter Adaptation Trust Fund",
		size=30)
		),			
			
    	FloatField('supplementary_unep_allocation',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=DecimalWidget(
		default=0.00,
		label="Supplementary Allocation to UNEP",
                description="Enter Supplementary Allocation to UNEP",
		size=30)
		), 
			
	StringField('supplementary_unep_allocation_remark',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=TextAreaWidget(
		label="Remark",
                description="Enter Supplementary UNEP Allocation Remark")
		),			
		
      	
	))
	

SupplementalBudgetSchema = Schema(
	(
	
        DataGridField('cofinancing_cash',
                searchable = True,
                columns=("cofinancing_cash_source", "cofinancing_cash_donor_name", "cofinancing_cash_planned_amount", "cofinancing_cash_actual_amount"),
                widget = DataGridWidget(
                    columns={
                        'cofinancing_cash_source' : SelectColumn("Source", vocabulary="getDONOR_TYPES"),
                        'cofinancing_cash_donor_name' : Column("Name of donor"),
                        'cofinancing_cash_planned_amount' : Column("Planned Amount"),
                        'cofinancing_cash_actual_amount' : Column("Actual Amount")
                    },
                ),
         ),
         

        DataGridField('cofinancing_inkind',
                searchable = True,
                columns=("cofinancing_inkind_source", "cofinancing_inkind_donor_name", "cofinancing_inkind_planned_amount", "cofinancing_inkind_actual_amount"),
                widget = DataGridWidget(
                    columns={
                        'cofinancing_inkind_source' : SelectColumn("Source", vocabulary="getDONOR_TYPES"),
                        'cofinancing_inkind_donor_name' : Column("Name of donor"),
                        'cofinancing_inkind_planned_amount' : Column("Planned Amount"),
                        'cofinancing_inkind_actual_amount' : Column("Actual Amount")
                    },
                ),
         ),	
  
   	FloatField('approved_unep_budget',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
			widget=DecimalWidget(
			label="Approved UNEP Budget")
			),
			
        DataGridField('cash_disbursements',
                searchable = True,
                columns=("cash_disbursements_date", "cash_disbursements_amount", "cash_disbursements_bank_ref_number"),
                widget = DataGridWidget(
                    columns={
                        'cash_disbursements_date' : Column("Date"),
                        'cash_disbursements_amount' : Column("Amount"),
                        'cash_disbursements_bank_ref_number' : Column("Bank Reference Number")
                    },
                ),
         ), 
         
        DataGridField('imis_expenditures',
                searchable = True,
                columns=("imis_expenditure_year", "imis_expenditure_amount"),
                widget = DataGridWidget(
                    columns={
                        'imis_expenditure_year' : Column("Date"),
                        'imis_expenditure_amount' : Column("Amount")
                    },
                ),
         ),         
		         

	StringField('status',
	        searchable=1,
		required=0,
		vocabulary=STATUS,
		index='FieldIndex:brains',
		widget=SelectionWidget(
		label = "Status",
                description = "Select Project Status")
         ),
                
	StringField('start_date',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=CalendarWidget(
		label="Start Date",
                description ="Select Project Start Date")
	 ),                
 
	StringField('initial_completion_date',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=CalendarWidget(
		label="Initial Completion Date",
                description = "Select Initial Completion Date")
	 ),
	 
	      	
	StringField('revised_completion_date',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=CalendarWidget(
		label="Revised Completion Date",
                description ="Select Revised Completion Date")
	 ),


	TextField('delay_reason',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=TextAreaWidget(
		label="Reason for delay",
                description = "Enter Reson for delay",
		rows=8)
	),
	

        DataGridField('reports',
                searchable = True,
                columns=("report_type", "report_period", "report_received_date"),
                widget = DataGridWidget(
                    columns={
                        'report_type' : SelectColumn("Source", vocabulary="getREPORT_TYPES"),                    
                        'report_period' : Column("Report Period"),
                        'report_received_date' : Column("Report Received Date")
                    },
                ),
         ),	

))

SupplementalAgencySchema = Schema(
        (
	ReferenceField('lead_executing_agency', 
			allowed_types=('mxmContactsOrganization'),
			multiValued=0,
			required=0,
			relationship='lea',
			widget=ReferenceBrowserWidget(allow_search=1, 
						 allow_browse=0,
						 show_indexes=1, 
						 label="Lead Executing Agency",
						 available_indexes={'SearchableText':'Free text search'},
				    description='Select Lead Executing Agency Contact.')) ,
				    
	ReferenceField('other_lead_executing_agency', 
	
			allowed_types=('mxmContactsOrganization'),
			multiValued=1,
			required=0,
			relationship='olea',
			widget=ReferenceBrowserWidget(allow_search=1, 
						 allow_browse=0,
						 show_indexes=1, 
						 label="Other Lead Executing Agencies",
						 available_indexes={'SearchableText':'Free text search'},
			    description='Select Other Lead Executing Agency Contact.')) ,	
	
	))
	



SupplementalFinalSchema = Schema(
	(
	ReferenceField('fund_management_officer', 
			allowed_types=('mxmContactsPerson'),
			multiValued=1,
			relationship='Rel2',
			widget=ReferenceBrowserWidget(allow_search=1, 
						 allow_browse=0,
						 show_indexes=1, 
						 label="Fund Management Officer",
						 available_indexes={'SearchableText':'Free text search'},
						    description='Select Fund Management Officer.')) ,
					    
	TextField('pdf_results',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
			widget=TextAreaWidget(
			label="Project Results",
			rows=8)
		),
	))


SubProjectCodeSchema = Schema(
	(
	StringField('account_code',
		searchable=1,
		required=0,
		index='FieldIndex:brains',
		widget=StringWidget(
		label="Account Code")
		),
	))
	
FactSheetSchema = Schema(
	(
					    
	TextField('environmental_problem',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
			allowable_content_types=('text/x-web-intelligent',),
			default_content_type="text/x-web-intelligent",
			default_output_type="text/html",
			widget=TextAreaWidget(
			label="Environmental Problem",
			rows=8)
		),

	TextField('project_goals',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
			allowable_content_types=('text/x-web-intelligent',),
			default_content_type="text/x-web-intelligent",
			default_output_type="text/html",
			widget=TextAreaWidget(
			label="Project Goal",
			rows=8)
		),
		
	TextField('activities',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
                        allowable_content_types=('text/x-web-intelligent',),
			default_content_type="text/x-web-intelligent",
			default_output_type="text/html",
			widget=TextAreaWidget(
			label="Activities",
			rows=8)
		),
		
	TextField('benefits',
			searchable=1,
			required=0,
			index='FieldIndex:brains',
                        allowable_content_types=('text/x-web-intelligent',),
			default_content_type="text/x-web-intelligent",
			default_output_type="text/html",
			widget=TextAreaWidget(
			label="Benefits",
			rows=8)
		),		
	))	
