# -*- coding: utf-8 -*-
#
# File: Milestone.py
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
from Products.ProjectDatabase.interfaces.IMilestone import IMilestone
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.DataGridField import CalendarColumn
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

    StringField(
        name='ProjectCycleStage',
        index="FieldIndex:brains",
        widget=SelectionWidget(
            label="Project Cycle Stage",
            label_msgid='ProjectDatabase_label_ProjectCycleStage',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectCycleStage""")
    ),

    StringField(
        name='MilestoneName',
        index="FieldIndex:brains",
        widget=SelectionWidget(
            label="Milestone Name",
            label_msgid='ProjectDatabase_label_MilestoneName',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""MilestoneName""")
    ),

    DateTimeField(
        name='MilestoneDate',
        index="FieldIndex:brains",
        widget=CalendarWidget(
            label="Milestone Date",
            show_hm=False,
            label_msgid='ProjectDatabase_label_MilestoneDate',
            i18n_domain='ProjectDatabase',
        )
    ),

    TextField(
        name='MilestoneDescription',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Remarks on Decision",
            label_msgid='ProjectDatabase_label_MilestoneDescription',
            i18n_domain='ProjectDatabase',
        ),
        default_output_type='text/html',
        vocabulary=NamedVocabulary("""ProjectStatusses""")
    ),

    DataGridField(
        name='ProjectProcess',
        widget=DataGridField._properties['widget'](
            columns={'project_process':SelectColumn('Project Process',vocabulary='getProjectProcesses'),'project_status':SelectColumn('Status', vocabulary='getProjectStatusses')},
            label="Project Processes",
            description="Project Process and Review Dates",
            label_msgid='ProjectDatabase_label_ProjectProcess',
            description_msgid='ProjectDatabase_help_ProjectProcess',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ProjectProcesses"""),
        columns=('project_process', 'project_status')
    ),

    DataGridField(
        name='NationalFocalPointEndorsements',
        widget=DataGridField._properties['widget'](
            label="National Focal Point Endorsements",
            columns={'country':SelectColumn('Country', vocabulary='getCountryNames'),'endorsement_date':CalendarColumn('Endorsement Date')},
            label_msgid='ProjectDatabase_label_NationalFocalPointEndorsements',
            i18n_domain='ProjectDatabase',
        ),
        columns=('country', 'endorsement_date')
    ),

    DataGridField(
        name='ApprovalInitiationAndClosure',
        widget=DataGridField._properties['widget'](
            label="Project Approval, Initiation and Closure",
            columns={'approval_initiation_closure':SelectColumn('Project Approval, Initiation and Closure', vocabulary='getApprovalInitiationClosure'), 'actual_date':CalendarColumn('Date')},
            label_msgid='ProjectDatabase_label_ApprovalInitiationAndClosure',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""ApprovalInitiationClosure"""),
        columns=('approval_initiation_closure','actual_date')
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Milestone_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
title_field = Milestone_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
##/code-section after-schema

class Milestone(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IMilestone)

    # This name appears in the 'add' box
    archetype_name = 'Project Cycle Milestone'

    meta_type = 'Milestone'
    portal_type = 'Milestone'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Milestone.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Project Cycle Milestone"
    typeDescMsgId = 'description_edit_milestone'

    _at_rename_after_creation = True

    schema = Milestone_schema

    ##code-section class-header #fill in your manual code here
    security.declarePublic('Title')
    def Title(self):
        """
        """
        return self.getMilestoneName()

    ##/code-section class-header

    # Methods

    security.declarePublic('getProjectProcesses')
    def getProjectProcesses(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('ProjectProcesses')
        return vocab.getDisplayList(self)

    security.declarePublic('getProjectStatusses')
    def getProjectStatusses(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('ProjectStatusses')
        return vocab.getDisplayList(self)

    security.declarePublic('getCountryNames')
    def getCountryNames(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('Country')
        return vocab.getDisplayList(self)

    security.declarePublic('getApprovalInitiationClosure')
    def getApprovalInitiationClosure(self):
        """
        """
        atvm = self.portal_vocabularies
        vocab = atvm.getVocabularyByName('ApprovalInitiationClosure')
        return vocab.getDisplayList(self)

    # Manually created methods

    security.declarePublic('Title')
    def Title(self):
        """
        """
        return self.getMilestoneName()



registerType(Milestone, PROJECTNAME)
# end of class Milestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



