## easy way to import most relevant symbols
from Products.CMFCore import CMFCorePermissions
from Products.Archetypes.public import *
from config import *
from Products.ATExtensions.Extensions.utils import getDisplayList, makeDisplayList

## BaseSchema provides title and all metadata stuff (i.e. expiration date)
schema = BaseSchema + Schema(
	(
	        StringField('report_type',
		required=1,
		searchable=1,
		index='FieldIndex:brains',
		vocabulary = REPORT_TYPE,
		accessor='Title',
		widget=SelectionWidget(
		label="Mode",
		),
	        ),
	        
	StringField('report_period',
		searchable=1,
		required=0,
		widget=StringWidget(
		label="Report Period")
	      	),
	      	
	DateTimeField('report_received',
		searchable=1,
		required=0,
		widget=CalendarWidget(
		label="Date Report Received")
	      	),
	
))	      	


## the final class definition. Deriving from BaseContent does most of the
## tricky work. Just let our schema be the schema for this content type.

class Reports(BaseFolder):
    """ Information about the milestone dates for the project
        """
    global_allow = 0
    portal_type = 'Reports'
    
    filter_content_types = 1
    schema = schema
        
      	
    
## important step: register the class as an archetype, so all of the 
## archetypes machinery will know it exists.

registerType(Reports, PROJECTNAME)    
