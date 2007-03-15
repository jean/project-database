# -*- coding: utf-8 -*-
#
# File: CountrySchema.py
#
# Copyright (c) 2006 by []
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

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ProjectDatabase.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField
from Products.FinanceFields.MoneyWidget import MoneyWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Country',
        widget=SelectionWidget(
            label='Country',
            label_msgid='ProjectDatabase_label_Country',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Countries""")
    ),

    StringField(
        name='Scope',
        widget=SelectionWidget(
            label='Scope',
            label_msgid='ProjectDatabase_label_Scope',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Scopes""")
    ),

    StringField(
        name='Region',
        widget=SelectionWidget(
            label='Region',
            label_msgid='ProjectDatabase_label_Region',
            i18n_domain='ProjectDatabase',
        ),
        vocabulary=NamedVocabulary("""Regions""")
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CountrySchema_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CountrySchema(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = CountrySchema_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

# end of class CountrySchema

##code-section module-footer #fill in your manual code here
##/code-section module-footer



