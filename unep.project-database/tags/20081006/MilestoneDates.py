"""
MilestoneDates definition
Each project can have one or more milestone dates
The schema is defined here
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2006/09/29 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"


from Products.CMFCore import CMFCorePermissions
from Products.Archetypes.public import *
from config import *
from permissions import *
from DateTime import DateTime

# define the MilestoneDates schema

schema = BaseSchema + Schema(
 (

 StringField('implementation_status',
      required=1,
      vocabulary = STATUS_VALUES,
      index='FieldIndex:brains',
      widget=SelectionWidget(
                label="Implementation Stage",
                label_msgid="label_implementation_status",
                description ='Enter Implementation Stage',
                description_msgid="help_implementation_status",
                i18n_domain="GEFProjectDB")
      ),
  
 StringField('milestone_name',
      required=1,
      vocabulary = MILESTONE_VALUES,
      index='FieldIndex:brains',
      widget=SelectionWidget(
                label="Milestone Name",
                label_msgid="label_milestone_name",
                description ='Enter name of the milestone',
                description_msgid="help_milestone_name",
                i18n_domain="GEFProjectDB")
              ),
     
  
 DateTimeField('milestone_date',
          required=1,
          default_method=DateTime,
          languageIndependent=True,
          index='DateIndex',
          widget=CalendarWidget(
                show_hm = False,
                label="Date",
                label_msgid="label_milestone_date",
                description ='Enter date of this milestone',
                description_msgid="help_milestone_date",
                i18n_domain="GEFProjectDB")
             ),
    
  
 StringField('milestone_description',
          searchable=1,
          required=0,
          widget=TextAreaWidget(
                label="Remark",
                label_msgid="label_milestone_description",
                description ='Remarks about this milestone',
                description_msgid="help_milestone_description",
                i18n_domain="GEFProjectDB"),
            ), 
     
))

# Get rid of the title that comes with BaseSchema
del schema['title']

# MilestoneDates class definition - it is a folderish type
  
class MilestoneDates(BaseFolder):

    global_allow = 0
    portal_type = 'MilestoneDates'

    # restrict the content types that can be added to MilestoneDates (actually there are none)
    
    filter_content_types = 1
    schema = schema
    
    # override the default views and actions from Archetypes
      
    
    actions = (
                {
             'id': 'view',
             'name': 'View',
             'action': 'string:${object_url}/Milestone_view',
             'permissions': (ViewProjects,),
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
             'id': 'local_roles',
             'name': 'Sharing',
             'action': 'string:${object_url}/folder_localrole_form',
             'permissions': (CMFCorePermissions.ManageProperties)
                },
        )

# there's no title but this function already exists so simply do nothing    
    def setTitle(self,value):
        pass
    
# dynamically generate a title for the MilestoneDate
    def Title(self):
        "Returns the computed title of the object"
        try:
            title = str(self.milestone_date) + " - " + self.milestone_name
        except:
            title = '...'
        return title
    
# register the class 'MilestoneDates' with our product

registerType(MilestoneDates, PROJECTNAME)     
