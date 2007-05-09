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
    project_title_val = pj.Title().replace ( ',', ';' )
    descr_val = pj.getSummaryDescription()
    focal_area_val = pj.getFocalArea()
    operational_programme_val = ', '.join(pj.getOperationalProgramme())
    operational_programme_val = operational_programme_val.replace ( ',', ';' )
    strategic_priority_val = ', '.join(pj.getStrategicPriority())
    strategic_priority_val = strategic_priority_val.replace ( ',', ';' )
    project_type_val = pj.getProjectType()
    pipeline_no_val = pj.getPipelineNumber()
    scope_val = pj.getScope()
    region_val = pj.getRegion()
    country_val = pj.getCountry()
    leadimplagency_val = pj.getLeadAgency()
    descr_comp_val = pj.getUnepComponentDescription()
    phase_val = pj.getGEFPhase()
    implementing_agency_fee_val = pj.getImplementingAgencyFee()
    unep_ia_fee_val = pj.getUNEPImplementingAgencyFee()
    

    
    
    print internal_id_val,",", gef_id_val, ",", project_title_val,",", focal_area_val, ",", operational_programme_val,",", strategic_priority_val,",", project_type_val,",", pipeline_no_val,",", scope_val,",", region_val,",", leadimplagency_val,",\n", 



   
return printed
