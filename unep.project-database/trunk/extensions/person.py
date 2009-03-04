from Products.Archetypes import PloneMessageFactory as _
from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from Products.Archetypes.atapi import *
from Products.UpfrontContacts.Person import Person

fields = [
    ]

class PersonExtender(object):
    adapts(Person)
    implements(IOrderableSchemaExtender)

    fields = fields

    def __init__(self, context):
         self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
        return original
    
