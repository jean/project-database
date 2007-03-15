# -*- coding: utf-8 -*-
#
# File: ProjectDatabase.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.5.1-svn
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
import zope
from Products.ProjectDatabase.interfaces.IProjectDatabase import IProjectDatabase
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.ProjectDatabase.widgets.SelectedLinesField import SelectedLinesField
from Products.CMFCore.utils import getToolByName
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

    SelectedLinesField(
        name='ProjectType',
        widget=SelectedLinesField._properties['widget'](
            label="Project Type",
            label_msgid='ProjectDatabase_label_ProjectType',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectType""")
    ),

    SelectedLinesField(
        name='FocalArea',
        widget=SelectedLinesField._properties['widget'](
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""FocalArea""")
    ),

    SelectedLinesField(
        name='Country',
        widget=SelectedLinesField._properties['widget'](
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Country""")
    ),

    SelectedLinesField(
        name='OperationalProgramme',
        widget=SelectedLinesField._properties['widget'](
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""OperationalProgramme""")
    ),

    SelectedLinesField(
        name='Region',
        widget=SelectedLinesField._properties['widget'](
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Region""")
    ),

    SelectedLinesField(
        name='ProjectStatus',
        widget=SelectedLinesField._properties['widget'](
            label="Project Status",
            label_msgid='ProjectDatabase_label_ProjectStatus',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectStatus""")
    ),

    SelectedLinesField(
        name='StrategicPriority',
        widget=SelectedLinesField._properties['widget'](
            label="Strategic Priority",
            label_msgid='ProjectDatabase_label_StrategicPriority',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicPriority""")
    ),

    SelectedLinesField(
        name='Scope',
        widget=SelectedLinesField._properties['widget'](
            label='Scope',
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Scope""")
    ),

    SelectedLinesField(
        name='GEFPhase',
        widget=SelectedLinesField._properties['widget'](
            label="GEF Phase",
            label_msgid='ProjectDatabase_label_GEFPhase',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""GEFPhase""")
    ),

    ComputedField(
        name='LeadAgencies',
        widget=ComputedField._properties['widget'](
            label="Lead Agencies",
            label_msgid='ProjectDatabase_label_LeadAgencies',
            i18n_domain='ProjectDatabase',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProjectDatabase_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ProjectDatabase(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IProjectDatabase)

    # This name appears in the 'add' box
    archetype_name = 'ProjectDatabase'

    meta_type = 'ProjectDatabase'
    portal_type = 'ProjectDatabase'
    allowed_content_types = ['ATFolder', 'Project']
    filter_content_types = 1
    global_allow = 1
    #content_icon = 'ProjectDatabase.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "ProjectDatabase"
    typeDescMsgId = 'description_edit_projectdatabase'

    _at_rename_after_creation = True

    schema = ProjectDatabase_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getLeadAgencies')
    def getLeadAgencies(self):
        """
        """
        catalog = getToolByName(self, 'portal_catalog')
        proxies = catalog(portal_type='Agency')
        return [p.getObject() for p in proxies]


registerType(ProjectDatabase, PROJECTNAME)
# end of class ProjectDatabase

##code-section module-footer #fill in your manual code here
##/code-section module-footer



