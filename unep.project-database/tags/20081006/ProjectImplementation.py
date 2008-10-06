""" 
ProjectImplementation definition
'ProjectImplementation' is contained within a 'Project'It has only a title field so we dfine its schema in here.
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"
    

from Products.Archetypes.public import *
from config import *
from permissions import *

# define the ProjectImplementation schema

schema = BaseSchema + Schema(
	(
	        DateTimeField('title',
		required=1,
		searchable=1,
                accessor='Title',
		index='FieldIndex:brains',
		widget=CalendarWidget(
		label="Year",
		),
	        ),
	
    		StringField('project_implementation_remark',
		searchable=1,
		required=1,
		index='FieldIndex:brains',
                allowable_content_types=('text/x-web-intelligent',),
                default_content_type="text/x-web-intelligent",
                default_output_type="text/html",
		widget=TextAreaWidget(
		label="Remark")
		),
))	      	



# ProjectImplementation class definition - it is a folderish type

class ProjectImplementation(BaseFolder):

    global_allow = 0
    portal_type = 'ProjectImplementation'

    # restrict the content types that can be added to a ProjectImplementation (actually there are none)
       
    filter_content_types = 1
    schema = schema

    # override the default views and actions from Archetypes
 
    actions = (
                {
              'id': 'view',
              'name': 'View',
              'action': 'string:${object_url}/Project_Core_view',
              'permissions': (ViewProjects,),
              'visible':1,
                },
             )      	
    
# register the class 'ProjectImplementation' with our product
registerType(ProjectImplementation, PROJECTNAME)    
