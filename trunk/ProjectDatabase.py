""" The ProjectDatabase is the overall container for the projects
    It has only a title field so we dfine its schema in here.
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"



# import permissions from both the config file and CMFCOre
from Products.CMFCore.CMFCorePermissions import ListFolderContents
from config import *
from permissions import *
# import fields, widgets from Archetypes
from Products.Archetypes.public import *
from AccessControl import ClassSecurityInfo

# schema definition for the ProjectDatabase type
schema = BaseSchema + Schema(
	(
    	StringField('title',
		required=0,
		searchable=1,
		accessor='Title',
		widget=StringWidget(
		# visible={'edit':'hidden'}
		# visible = -1
		),
                ),
))
	
# ProjectDatabase class definition - it is a folderish type
 
class ProjectDatabase(BaseFolder):
	
    global_allow = 1
    portal_type = 'ProjectDatabase'
    
    # restrict the content types that can be added to a ProjectDatabase
    # in this case we only allow 'Project' and 'Folder'    
    
    filter_content_types = 1
    allowed_content_types = ['Project','Folder']

    # icon associated with a 'ProjectDatabase' type    
    content_icon = 'project.jpg'
    schema = schema
    
    # override the default views and actions 

    actions = (
    {
	'id': 'view',
	'name': 'View',
	'action': 'string:${object_url}/Project_view',
	'permissions': (ViewProjects,),
	'visible':1,
    },
    {
	'id': 'folderContents',
	'name': 'Contents',
	'action': 'string:${object_url}/folder_contents',
	'permissions': (ListFolderContents,),
	'visible':0,
    },
    {
	'id': 'edit',
	'name': 'Edit',
	'action': 'string:${object_url}/base_edit',
	'permissions': (EDIT_CONTENTS_PERMISSION,),
	'visible':0,
    },
    {
	'id': 'metadata',
	'name': 'Properties',
	'action': 'string:${object_url}/base_metadata',
	'permissions': (EDIT_CONTENTS_PERMISSION,),
	'visible':0,
    },
    {
	'id': 'references',
	'name': 'References',
	'action': 'string:${object_url}/reference_edit',
	'permissions': (EDIT_CONTENTS_PERMISSION,),
	'visible':0,
    },
    )

    security = ClassSecurityInfo()
    security.declareObjectProtected(ViewProjects)
    
    def getProjectTypes(self):
        return PROJECT_TYPES.items()

    def getFocalAreas(self):
        return FOCAL_AREAS.items()

    def getCountrys(self):
        return getDisplayList(self, 'country_names')

    def getOperationalProgrammes(self):
        return OPERATIONAL_PROGRAMMES.items()

    def getLeadAgency(self):
        return LEAD_AGENCY.items()

    def getRegions(self):
        return REGION.items()

    def getProjectStatus(self):
        return PROJECT_STATUS.items()

    def getStrategicPriorities(self):
        return STRATEGIC_PRIORITIES.items()

    def getGeographicScope(self):
        return SCOPE.items()

    def getGEFPhase(self):
	return GEF_PHASE.items()
    
# register the object 'ProjectDatabase' with our product
registerType(ProjectDatabase, PROJECTNAME)	

