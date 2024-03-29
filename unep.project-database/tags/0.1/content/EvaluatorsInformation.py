# -*- coding: utf-8 -*-
#
# File: EvaluatorsInformation.py
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

    ReferenceField(
        name='TeamLeader',
        widget=ReferenceBrowserWidget(
            label="Team Lead",
            description="Name of Evaluation Team Leader",
            checkbox_bound=0,
            label_msgid='ProjectDatabase_label_TeamLeader',
            description_msgid='ProjectDatabase_help_TeamLeader',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="EI_team_leader",
        multiValued=0,
        # vocabulary='contactsVocab',
    ),
    ReferenceField(
        name='TeamMembers',
        widget=ReferenceBrowserWidget(
            label="Team Members",
            description="Names of other evaluation Team Members",
            label_msgid='ProjectDatabase_label_TeamMembers',
            description_msgid='ProjectDatabase_help_TeamMembers',
            i18n_domain='ProjectDatabase',
        ),
        allowed_types=('Person',),
        relationship="EI_team_members",
        multiValued=1,
        # vocabulary='contactsVocab',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EvaluatorsInformation_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
title_field = EvaluatorsInformation_schema['title']
title_field.required=0
title_field.widget.visible = {'edit':'hidden', 'view':'invisible'}
##/code-section after-schema

class EvaluatorsInformation(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IEvaluatorsInformation)

    meta_type = 'EvaluatorsInformation'
    _at_rename_after_creation = True

    schema = EvaluatorsInformation_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

#    def contactsVocab(self):
#        """
#        """
#        path = '/'.join(self.getAProject().getPhysicalPath()) + '/contacts-1'
#        brains = self.portal_catalog(portal_type='Person', path=path)
#        pairs=[]
#        pairs.append(("", "<no reference>"))
#        for b in brains:
#            pairs.append((b.getObject().UID(), b.getObject().Title()))
#        return DisplayList(pairs)



registerType(EvaluatorsInformation, PROJECTNAME)
# end of class EvaluatorsInformation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



