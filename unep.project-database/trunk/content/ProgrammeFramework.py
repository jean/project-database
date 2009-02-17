# -*- coding: utf-8 -*-
#
# File: ProgrammeFramework.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Jean Jordaan <jean.jordaan@gmail.com>, Jurgen Blignaut
<jurgen.blignaut@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ProjectDatabase.content.CurrencyMixin import CurrencyMixin
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.DataGridField import DataGridField, Column, SelectColumn, CalendarColumn
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='PFDShortTitle',
        widget=TextAreaWidget(
            label="PFD Short Title",
            label_msgid='ProjectDatabase_label_PFDShortTitle',
            i18n_domain='ProjectDatabase',
        ),
        required= True,
    ),
    MoneyField(
        name='PFDAllocatedAmount',
        default='0.0',
        widget=MoneyField._properties['widget'](
            label="PFD Allocated Amount",
            label_msgid='ProjectDatabase_label_PFDAllocatedAmount',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='LeadAgency',
        widget=SelectionWidget(
            label="Lead Agency",
            label_msgid='ProjectDatabase_label_LeadAgency',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""LeadAgency"""),
    ),
    LinesField(
        name='FocalArea',
        widget=MultiSelectionWidget(
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""FocalArea"""),
    ),
    DateTimeField(
        name='ProjectSubmissionDeadline',
        widget=DateTimeField._properties['widget'](
            label="Project Submission Deadline",
            label_msgid='ProjectDatabase_label_ProjectSubmissionDeadline',
            i18n_domain='ProjectDatabase',
        ),
    ),
    DataGridField(
        name='ProgrammeFrameworkMilestones',
        widget=DataGridField._properties['widget'](
            label="Programme Framework Milestones",
            columns={'milestone_action':SelectColumn('Milestone Action', vocabulary='getMilestoneActionVocabulary'), 'milestone_date':Column('Milestone Date'),  'milestone_result':SelectColumn('Milestone Result', vocabulary='getMilestoneResultVocabulary')},
            label_msgid='ProjectDatabase_label_ProgrammeFrameworkMilestones',
            i18n_domain='ProjectDatabase',
        ),
        columns= ('milestone_action', 'milestone_date',  'milestone_result'),
    ),
    ReferenceField(
        name='SeniorProgrammeOfficer',
        widget=ReferenceBrowserWidget(
            label="Senior Programme Officer",
            label_msgid='ProjectDatabase_label_SeniorProgrammeOfficer',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        multiValued=0,
        relationship="PFD_Person",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProgrammeFramework_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ProgrammeFramework_schema['SeniorProgrammeOfficer'].widget.startup_directory_method = 'getContactsPath'
##/code-section after-schema

class ProgrammeFramework(BaseContent, CurrencyMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProgrammeFramework)

    meta_type = 'ProgrammeFramework'
    _at_rename_after_creation = True

    schema = ProgrammeFramework_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def getMilestoneActionVocabulary(self):
        return self.getVocabulary('MilestoneAction')

    def getMilestoneResultVocabulary(self):
        return self.getVocabulary('MilestoneResult')

    def getVocabulary(self, vocabName):
        pvt = getToolByName(self, 'portal_vocabularies')
        vocab = pvt.getVocabularyByName(vocabName)
        return vocab.getDisplayList(self)

    security.declarePublic('getContactsPath')
    def getContactsPath(self):
        purl = getToolByName(self, 'portal_url').getPortalObject().absolute_url()
        pc = getToolByName(self, 'portal_catalog')
        brains = pc({'portal_type':'ContactManager'})
        if len(brains) > 0:
            contacts = brains[0].getObject()
            curl = contacts.absolute_url()
            return curl[len(purl)+1:]



registerType(ProgrammeFramework, PROJECTNAME)
# end of class ProgrammeFramework

##code-section module-footer #fill in your manual code here
##/code-section module-footer



