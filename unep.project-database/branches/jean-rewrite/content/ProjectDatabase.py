# -*- coding: utf-8 -*-
#
# File: ProjectDatabase.py
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
import zope
from Products.ProjectDatabase.interfaces.IProjectDatabase import IProjectDatabase
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.ProjectDatabase.widgets.SelectedLinesField import SelectedLinesField
from Products.CMFCore.utils import getToolByName
from Products.ProjectDatabase.content import permissions
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
        name='ProjectType',
        widget=InAndOutWidget
        (
            label="Project Type",
            label_msgid='ProjectDatabase_label_ProjectType',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectType""")
    ),

    LinesField(
        name='FocalArea',
        widget=InAndOutWidget
        (
            label="Focal Area",
            label_msgid='ProjectDatabase_label_FocalArea',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""FocalArea""")
    ),

    LinesField(
        name='Country',
        widget=InAndOutWidget
        (
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Country""")
    ),

    LinesField(
        name='OperationalProgramme',
        widget=InAndOutWidget
        (
            label="Operational Programme",
            label_msgid='ProjectDatabase_label_OperationalProgramme',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""OperationalProgramme""")
    ),

    LinesField(
        name='Region',
        widget=InAndOutWidget
        (
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Region""")
    ),

    LinesField(
        name='ProjectStatus',
        widget=InAndOutWidget
        (
            label="Project Status",
            label_msgid='ProjectDatabase_label_ProjectStatus',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectStatus""")
    ),

    LinesField(
        name='StrategicPriority',
        widget=InAndOutWidget
        (
            label="Strategic Priority",
            label_msgid='ProjectDatabase_label_StrategicPriority',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""StrategicPriority""")
    ),

    LinesField(
        name='Scope',
        widget=InAndOutWidget
        (
            label='Scope',
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Scope""")
    ),

    LinesField(
        name='GEFPhase',
        widget=InAndOutWidget
        (
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


    actions =  (


       {'action': "string:${object_url}/project_search",
        'category': "object_tabs",
        'id': 'search',
        'name': 'Project Search',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/export_project_data",
        'category': "object_tabs",
        'id': 'export_project_data',
        'name': 'Export Project Data (csv)',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:0'
       },


       {'action': "string:${object_url}/reports_view",
        'category': "object_tabs",
        'id': 'reports',
        'name': 'reports',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/export_view",
        'category': "object_tabs",
        'id': 'export',
        'name': 'export',
        'permissions': (permissions.ViewProjects,),
        'condition': 'python:1'
       },


    )

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
        pl = [p.getObject().Title() for p in proxies]
        return ','.join(pl)

    security.declarePublic('getVocabulary')
    def getVocabulary(self,vocabName):
        """Get the named vocabulary
        """
        pv_tool = getToolByName(self, 'portal_vocabularies')
        vocab = pv_tool.getVocabularyByName(vocabName)
        return vocab.getDisplayList(vocab)


registerType(ProjectDatabase, PROJECTNAME)
# end of class ProjectDatabase

##code-section module-footer #fill in your manual code here
def modify_fti(fti):
    for a in fti['actions']:
        print str(a)
        if a['id'] in ('metadata', 'references'):
            a['visible'] = False
        print str(a)
    return fti
##/code-section module-footer



