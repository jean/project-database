# -*- coding: utf-8 -*-
#
# File: CoreMixin.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
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

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn, CalendarColumn
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
import Project
import Financials
from Products.CMFCore.utils import getToolByName
from Products.FinanceFields.Money import Money

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    LinesField(
        name='FocalArea',
        widget=MultiSelectionWidget(
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""FocalArea"""),
        default_method="getDefaultFocalArea",
    ),
    StringField(
        name='OperationalProgramme',
        widget=SelectionWidget(
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""OperationalProgramme"""),
        default_method="getDefaultOperationalProgramme",
    ),
    StringField(
        name='StrategicObjectives',
        widget=SelectionWidget(
            label="Strategic Objective",
            label_msgid='ProjectDatabase_label_StrategicObjectives',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicObjectives"""),
    ),
    StringField(
        name='PipelineNumber',
        widget=SelectionWidget(
            label="Pipeline Number",
            label_msgid='ProjectDatabase_label_PipelineNumber',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""PipelineNumber"""),
        default_method="getDefaultPipelineNumber",
    ),
    LinesField(
        name='Country',
        widget=MultiSelectionWidget(
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Country"""),
        default_method="getDefaultCountry",
    ),
    LinesField(
        name='Region',
        widget=MultiSelectionWidget(
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Region"""),
        default_method="getDefaultRegion",
    ),
    LinesField(
        name='Scope',
        widget=MultiSelectionWidget(
            label="Geographic Scope",
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        multiValued=1,
        vocabulary=NamedVocabulary("""Scope"""),
        default_method="getDefaultScope",
    ),
    StringField(
        name='GEFPhase',
        widget=SelectionWidget(
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""GEFPhase"""),
        default_method="getDefaultGEFPhase",
    ),
    StringField(
        name='Website',
        widget=StringField._properties['widget'](
            label='Website',
            label_msgid='ProjectDatabase_label_Website',
            i18n_domain='ProjectDatabase',
        ),
        default_method="getDefaultWebsite",
        validators=('isUrl',),
    ),
    ReferenceField(
        name='CurrentTaskManager',
        widget=ReferenceBrowserWidget(
            label="Current Task Manager",
            label_msgid='ProjectDatabase_label_CurrentTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        relationship="Project_CurrentTaskManager",
        default_method="getDefaultCurrentTaskManager",
    ),
    ReferenceField(
        name='PreviousTaskManager',
        widget=ReferenceBrowserWidget(
            label="Previous Task Manager",
            label_msgid='ProjectDatabase_label_PreviousTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        relationship="Project_PreviousTaskManager",
        default_method="getDefaultPreviousTaskManager",
    ),
    ReferenceField(
        name='ProjectCoordinator',
        widget=ReferenceBrowserWidget(
            label="Project Coordinator",
            label_msgid='ProjectDatabase_label_ProjectCoordinator',
            i18n_domain='ProjectDatabase',
        ),
        relationship="Project_ProjectCoordinator",
        default_method="getDefaultProjectCoordinator",
    ),
    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label="Project Title",
            label_msgid='ProjectDatabase_label_ProjectTitle',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='PMSNumber',
        widget=StringField._properties['widget'](
            label="PMS Number",
            label_msgid='ProjectDatabase_label_PMSNumber',
            i18n_domain='ProjectDatabase',
        ),
    ),
    StringField(
        name='IMISNumber',
        widget=StringField._properties['widget'](
            label="IMIS Number",
            label_msgid='ProjectDatabase_label_IMISNumber',
            i18n_domain='ProjectDatabase',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CoreMixin_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
CoreMixin_schema['CurrentTaskManager'].widget.startup_directory = '/contacts'
CoreMixin_schema['PreviousTaskManager'].widget.startup_directory = '/contacts'
CoreMixin_schema['ProjectCoordinator'].widget.startup_directory = '/contacts'
##/code-section after-schema

class CoreMixin(BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.ICoreMixin)

    meta_type = 'CoreMixin'
    _at_rename_after_creation = True

    schema = CoreMixin_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getDefaultFocalArea')
    def getDefaultFocalArea(self):
        """
        """
        return self.getProjectGeneralInformation().getFocalArea()

    security.declarePublic('getDefaultOperationalProgramme')
    def getDefaultOperationalProgramme(self):
        """
        """
        return self.getProjectGeneralInformation().getOperationalProgramme()

    security.declarePublic('getDefaultStrategicObjectives')
    def getDefaultStrategicObjectives(self):
        """
        """
        return self.getProjectGeneralInformation().getStrategicObjectives()

    security.declarePublic('getDefaultPipelineNumber')
    def getDefaultPipelineNumber(self):
        """
        """
        return self.getProjectGeneralInformation().getPipelineNumber()

    security.declarePublic('getDefaultCountry')
    def getDefaultCountry(self):
        """
        """
        return self.getProjectGeneralInformation().getCountry()

    security.declarePublic('getDefaultRegion')
    def getDefaultRegion(self):
        """
        """
        return self.getProjectGeneralInformation().getRegion()

    security.declarePublic('getDefaultScope')
    def getDefaultScope(self):
        """
        """
        return self.getProjectGeneralInformation().getScope()

    security.declarePublic('getDefaultGEFPhase')
    def getDefaultGEFPhase(self):
        """
        """
        return self.getProjectGeneralInformation().getGEFPhase()

    security.declarePublic('getDefaultWebsite')
    def getDefaultWebsite(self):
        """
        """
        return self.getProjectGeneralInformation().getWebsite()

    security.declarePublic('getDefaultCurrentTaskManager')
    def getDefaultCurrentTaskManager(self):
        """
        """
        return self.getProjectGeneralInformation().getCurrentTaskManager()

    security.declarePublic('getDefaultPreviousTaskManager')
    def getDefaultPreviousTaskManager(self):
        """
        """
        return self.getProjectGeneralInformation().getPreviousTaskManager()

    security.declarePublic('getDefaultProjectCoordinator')
    def getDefaultProjectCoordinator(self):
        """
        """
        return self.getProjectGeneralInformation().getProjectCoordinator()

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """
        """
        return self.getProjectGeneralInformation().getProjectTitle()


# end of class CoreMixin

##code-section module-footer #fill in your manual code here
##/code-section module-footer



