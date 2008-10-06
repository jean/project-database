## easy way to import most relevant symbols
from Products.CMFCore import CMFCorePermissions
from Products.Archetypes.public import *
from config import *

## BaseSchema provides title and all metadata stuff (i.e. expiration date)
schema = BaseSchema + Schema(
	(
	        StringField('imis_expenditure_year',
		required=1,
		searchable=1,
		accessor='Title',
		widget=StringWidget(
		label="Year",
		),
	        ),
	
    		FixedPointField('imis_expenditure_amount',
			searchable=1,
			required=0,
			widget=DecimalWidget(
			label="Amount")
		),

))	      	


## the final class definition. Deriving from BaseContent does most of the
## tricky work. Just let our schema be the schema for this content type.

class IMISExpenditure(BaseFolder):
    """ Information about the milestone dates for the project
        """
    global_allow = 0
    portal_type = 'IMISExpenditure'
    
    filter_content_types = 1
    schema = schema
           
      	
    
## important step: register the class as an archetype, so all of the 
## archetypes machinery will know it exists.

registerType(IMISExpenditure, PROJECTNAME)    

