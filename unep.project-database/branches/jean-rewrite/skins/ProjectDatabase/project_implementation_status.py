# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
import string
request = container.REQUEST
RESPONSE =  request.RESPONSE
RESPONSE.setHeader('Content-Type','text/csv')
RESPONSE.setHeader('Content-Disposition','filename=projectdata.csv')

# Return a string identifying this script.
results = context.portal_catalog.searchResults(
                                 portal_type='Project',
                                 review_state='visible',
                                 path= '/'.join(context.getPhysicalPath())
                              )

print "Internal Id, GEF Id, Title, Year, Remark"
for result in results:
    pj = result.getObject()
    internal_id_val = pj.id
    gef_id_val = pj.title
    project_title_val = pj.getProjectTitle()
    project_title_val = project_title_val.replace ( ',', ';' )
       

    pjimplresults = context.portal_catalog.searchResults( 
                                 portal_type='ProjectImplementation', 
                                 path= '/'.join(pj.getPhysicalPath()))

    for pjimpl_vals in pjimplresults :
      pjimpl_obj = pjimpl_vals.getObject()
      pjimpl_title_val = pjimpl_obj.title
      pjimpl_remark_val = pjimpl_obj.getRemark().replace ( ',', ';' )

      print internal_id_val,",", gef_id_val,",", project_title_val,",", pjimpl_title_val,",", pjimpl_remark_val,",\n",

   
return printed
