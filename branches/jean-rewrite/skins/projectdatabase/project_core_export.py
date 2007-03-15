# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
import string
request = container.REQUEST
RESPONSE =  request.RESPONSE
RESPONSE.setHeader('Content-Type','text/csv')
RESPONSE.setHeader('Content-Disposition','filename=projectdata.csv')

# Return a string identifying this script.
results = context.portal_catalog(
                                 portal_type='Project',
                                 review_state='visible',
                                 path= '/'.join(context.getPhysicalPath())
                              )

print "Internal Id, GEF Id, Title, Focal Area, Operational Programme, Strategic Priority, Project Type, Pipeline Number, Scope, Region, Lead Implementing Agency, Other Implementing Agencies, Description of UNEP Components, GEF Phase, Implementing Agency Fee, UNEP IA Fee"
for result in results:
    pj = result.getObject()
    internal_id_val = pj.id
    gef_id_val = pj.title
    descr_val = pj.summary_project_description
    focal_area_val = pj.focal_area
    operational_programme_val = ', '.join(pj.operational_programme)
    operational_programme_val = operational_programme_val.replace ( ',', ';' )
    strategic_priority_val = ', '.join(pj.strategic_priority)
    strategic_priority_val = strategic_priority_val.replace ( ',', ';' )
    project_type_val = pj.project_type
    pipeline_no_val = pj.pipeline_number
    scope_val = pj.scope
    region_val = pj.region
    country_val = pj.country
    leadimplagency_val = pj.leadagency
    descr_comp_val = pj.unep_component_description
    phase_val = pj.gef_phase
    implementing_agency_fee_val = pj.implementing_agency_fee
    unep_ia_fee_val = pj.unep_ia_fee
    project_title_val = pj.getProject_title().replace ( ',', ';' )
    

    
    
    print internal_id_val,",", gef_id_val, ",", project_title_val,",", focal_area_val, ",", operational_programme_val,",", strategic_priority_val,",", project_type_val,",", pipeline_no_val,",", scope_val,",", region_val,",", leadimplagency_val,",\n", 



   
return printed
