# -*- coding: utf-8 -*-
#
# File: CoreMixin.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Jean Jordaan <jean.jordaan@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget
from Products.DataGridField import DataGridField, DataGridWidget, Column, SelectColumn
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
        default_method="getDefaultFocalArea"
    ),

    StringField(
        name='OperationalProgramme',
        widget=SelectionWidget(
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""OperationalProgramme"""),
        default_method="getDefaultOperationalProgramme"
    ),

    StringField(
        name='StrategicObjectives',
        widget=SelectionWidget(
            label="Strategic Objective",
            label_msgid='ProjectDatabase_label_StrategicObjectives',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicObjectives""")
    ),

    StringField(
        name='PipelineNumber',
        widget=SelectionWidget(
            label="Pipeline Number",
            label_msgid='ProjectDatabase_label_PipelineNumber',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""PipelineNumber"""),
        default_method="getDefaultPipelineNumber"
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
        default_method="getDefaultCountry"
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
        default_method="getDefaultRegion"
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
        default_method="getDefaultScope"
    ),

    StringField(
        name='GEFPhase',
        widget=SelectionWidget(
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        default_method="getDefaultGEFPhase"
    ),

    StringField(
        name='Website',
        widget=StringWidget(
            label='Website',
            label_msgid='ProjectDatabase_label_Website',
            i18n_domain='ProjectDatabase',
        ),
        default_method="getDefaultWebsite",
        validators=('isUrl',)
    ),

    ReferenceField(
        name='CurrentTaskManager',
        widget=ReferenceField._properties['widget'](
            label="Current Task Manager",
            label_msgid='ProjectDatabase_label_CurrentTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        relationship="Project_CurrentTaskManager",
        default_method="getDefaultCurrentTaskManager"
    ),

    ReferenceField(
        name='PreviousTaskManager',
        widget=ReferenceField._properties['widget'](
            label="Previous Task Manager",
            label_msgid='ProjectDatabase_label_PreviousTaskManager',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        relationship="Project_PreviousTaskManager",
        default_method="getDefaultPreviousTaskManager"
    ),

    ReferenceField(
        name='ProjectCoordinator',
        widget=ReferenceField._properties['widget'](
            label="Project Coordinator",
            label_msgid='ProjectDatabase_label_ProjectCoordinator',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('mxmContactsPerson',),
        relationship="Project_ProjectCoordinator",
        default_method="getDefaultProjectCoordinator"
    ),

    ComputedField(
        name='ProjectTitle',
        widget=ComputedField._properties['widget'](
            label="Project Title",
            label_msgid='ProjectDatabase_label_ProjectTitle',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='PMSNumber',
        dummy="PMS Number",
        widget=StringWidget(
            label="PMS Number",
            label_msgid='ProjectDatabase_label_PMSNumber',
            i18n_domain='ProjectDatabase',
        )
    ),

    StringField(
        name='IMISNumber',
        dummy="IMIS Number",
        widget=StringWidget(
            label="IMIS Number",
            label_msgid='ProjectDatabase_label_IMISNumber',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CoreMixin_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CoreMixin:
    """
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'CoreMixin'

    meta_type = 'CoreMixin'
    portal_type = 'CoreMixin'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'CoreMixin.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "CoreMixin"
    typeDescMsgId = 'description_edit_coremixin'

    _at_rename_after_creation = True

    schema = CoreMixin_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getDefaultFocalArea')
    def getDefaultFocalArea(self):
        """
        """
        return self.getProject().getFocalArea()

    security.declarePublic('getDefaultOperationalProgramme')
    def getDefaultOperationalProgramme(self):
        """
        """
        return self.getProject().getOperationalProgramme()

    security.declarePublic('getDefaultStrategicObjectives')
    def getDefaultStrategicObjectives(self):
        """
        """
        return self.getProject().getStrategicObjectives()

    security.declarePublic('getDefaultPipelineNumber')
    def getDefaultPipelineNumber(self):
        """
        """
        return self.getProject().getPipelineNumber()

    security.declarePublic('getDefaultCountry')
    def getDefaultCountry(self):
        """
        """
        return self.getProject().getCountry()

    security.declarePublic('getDefaultRegion')
    def getDefaultRegion(self):
        """
        """
        return self.getProject().getRegion()

    security.declarePublic('getDefaultScope')
    def getDefaultScope(self):
        """
        """
        return self.getProject().getScope()

    security.declarePublic('getDefaultGEFPhase')
    def getDefaultGEFPhase(self):
        """
        """
        return self.getProject().getGEFPhase()

    security.declarePublic('getDefaultWebsite')
    def getDefaultWebsite(self):
        """
        """
        return self.getProject().getWebsite()

    security.declarePublic('getDefaultCurrentTaskManager')
    def getDefaultCurrentTaskManager(self):
        """
        """
        return self.getProject().getCurrentTaskManager()

    security.declarePublic('getDefaultPreviousTaskManager')
    def getDefaultPreviousTaskManager(self):
        """
        """
        return self.getProject().getPreviousTaskManager()

    security.declarePublic('getDefaultProjectCoordinator')
    def getDefaultProjectCoordinator(self):
        """
        """
        return self.getProject().getProjectCoordinator()

    security.declarePublic('getProjectTitle')
    def getProjectTitle(self):
        """
        """
        return self.getProject().getProjectTitle()


# end of class CoreMixin

##code-section module-footer #fill in your manual code here
##/code-section module-footer



