# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
import string
request = container.REQUEST
RESPONSE =  request.RESPONSE
RESPONSE.setHeader('Content-Type','text/csv')
RESPONSE.setHeader('Content-Disposition','filename=fmidata.csv')

# Return a string identifying this script.
results = context.portal_catalog.searchResults(
                                 portal_type='Project',
                                 review_state='visible',
                                 path= '/'.join(context.getPhysicalPath())
                              )
print "Internal Id, GEF Id, FMI Id, Title, Finance Category, PMS Number, IMIS Number, Total GEF Allocation, GEF Trust Fund, LDC Fund, SCCF Allocation, Strategic Partnership, Adaptation Trust Fund, Supplementary Allocation Amount, Start Date, Initial Completion Date, Revised Completion Date"
for result in results:
    pj = result.getObject()
    internal_id_val = pj.id
    gef_id_val = pj.title
       

    pjimplresults = context.portal_catalog.searchResults( 
                                 portal_type='ProjectImplementation', 
                                 path= '/'.join(pj.getPhysicalPath()))

    for pjimpl_vals in pjimplresults :
      pjimpl_obj = pjimpl_vals.getObject()
      pjimpl_title_val = pjimpl_obj.title
      pjimpl_remark_val = pjimpl_obj.project_implementation_remark


    fmiresults = context.portal_catalog.searchResults( 
                                 portal_type='FinancialManagementInformation', 
                                 path= '/'.join(pj.getPhysicalPath()))
    for fmi_vals in fmiresults :
      fmi_obj = fmi_vals.getObject()
      fmi_internal_id_val = fmi_obj.id
      fmi_title_val =  string.replace(fmi_obj.title, ',', ';')
      fcategory_val = fmi_obj.finance_category
      pms_number_val = fmi_obj.pms_number
      imis_number_val = fmi_obj.imis_number
      total_gef_alloc_val = fmi_obj.gef_project_allocation
      gef_trust_fund_val = fmi_obj.gef_trust_fund
      ldc_fund_allocation_val = fmi_obj.ldc_fund_allocation
      sccf_allocation_val = fmi_obj.sccf_allocation
      strategic_partnership_val = fmi_obj.strategic_partnership
      adaptation_trust_fund_val =fmi_obj.adaptation_trust_fund
      supplementary_unep_allocation_val = fmi_obj.supplementary_unep_allocation
      start_date_val = fmi_obj.start_date
      initial_completion_date_val = fmi_obj.initial_completion_date
      revised_completion_date_val = fmi_obj.revised_completion_date
      delay_reason_val = fmi_obj.delay_reason
      

      print internal_id_val,",", gef_id_val,",", fmi_internal_id_val,",", fmi_title_val,",", fcategory_val,",", pms_number_val,",", imis_number_val,",", total_gef_alloc_val,",", gef_trust_fund_val,",", ldc_fund_allocation_val,",", sccf_allocation_val,",", strategic_partnership_val,",", adaptation_trust_fund_val,",", supplementary_unep_allocation_val,",", start_date_val,",", initial_completion_date_val,",", revised_completion_date_val,",", delay_reason_val,",\n",  
                                                                                                                                                                                                                                                                                                                                    
   
return printed
