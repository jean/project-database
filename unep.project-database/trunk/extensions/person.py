from Products.Archetypes import PloneMessageFactory as _
from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from Products.Archetypes.atapi import *
from Products.UpfrontContacts.Person import Person
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.widgets.UNEPSelectionWidget \
        import UNEPSelectionWidget
from Products.ProjectDatabase.utils import *
from utils import *
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

class RatingComputedField(ExtensionField, ComputedField):
    """ """
    def getRating(self, context):
        """ """
        print "Inside Last Rating"
        refcat = getToolByName(context, 'reference_catalog')
        relationships = refcat.getBackReferences(
            context.UID(), 
            relationship='mne_evaluator')
        mod_date = DateTime('1900/01/01')
        last_mne = None
        for rel in relationships:
            mne = refcat.lookupObject(rel.sourceUID)
            #Maybe also check for lead evaluator
            if mne['modification_date'] > mod_date:
                mod_date = mne['modification_date']
                last_mne = mne
        if last_mne:
            rating = last_mne.getEOUTerminalEvaluationReportQuality()
            if rating != 'No Selection':
                rating = getVocabularyValue(context, 'Rating', rating)
            return rating
        



fields = [
        efStringField("Salutation", 
            widget = UNEPSelectionWidget(
                label=_(u'label_salutation', default=u'Salutation')),
            vocabulary=NamedVocabulary("""Salutation"""),
        ),
        efStringField("JobTitle", 
            widget = UNEPSelectionWidget(
                label=_(u'label_jobtitle', default=u'Job Title')),
            vocabulary=NamedVocabulary("""JobTitle"""),
        ),
        efStringField("FocalArea", 
            widget = UNEPSelectionWidget(
                label=_(u'label_focalarea', default=u'Focal Area')),
            vocabulary=NamedVocabulary("""FocalArea"""),
        ),
        efStringField("AreaOfExpertise", 
            widget = StringWidget(
                label=_(u'label_areaofexpertise', \
                        default=u'Area Of Expertise')),
        ),
        RatingComputedField("LastRating", 
            expression="context.Schema().getField('LastRating').getRating(context)",
            widget = ComputedField._properties['widget'](
                visible=True,
                label=_(u'label_lastrating', \
                        default=u'Last Rating')),
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
    
