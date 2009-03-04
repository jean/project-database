from Products.Archetypes import PloneMessageFactory as _
from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from Products.Archetypes.atapi import *
from Products.UpfrontContacts.Person import Person
from utils import *

fields = [
        efStringField("JobTitle", 
            widget = StringWidget(
                label=_(u'label_jobtitle', default=u'Job Title')),
        ),
        ]

class PersonExtender(object):
    """
    Extend the schema of person in UpfrontContacts
    """

    implements(IOrderableSchemaExtender)
    adapts(Person)

    fields = fields

    def __init__(self, context):
         self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
        return original
    
