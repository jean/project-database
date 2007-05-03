# -*- coding: utf-8 -*-
#
# File: SelectedLinesField.py
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

#SelectedLinesField

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Field import ObjectField,encode,decode
from Products.Archetypes.Registry import registerField
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.Archetypes.Field  import *
from Products.Archetypes.Schema import Schema
try:
    from Products.generator import i18n
except ImportError:
    from Products.Archetypes.generator import i18n

from Products.ProjectDatabase import config

##code-section module-header #fill in your manual code here
# XXX Bug in AGX: this should be generated as for content classes
import zope
##/code-section module-header

from Products.Archetypes.Field import LinesField
from Products.ProjectDatabase.interfaces.ISelectedLinesField import ISelectedLinesField
from Products.Archetypes.Widget import MultiSelectionWidget




class SelectedLinesField(LinesField):
    """A lines field that starts off with all vocabulary items selected
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(LinesField,'__implements__',()),) + (getattr(LinesField,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(ISelectedLinesField)


    _properties = LinesField._properties.copy()
    _properties.update({
        'type': 'selectedlinesfield',
        'widget':MultiSelectionWidget,
        ##code-section field-properties #fill in your manual code here
        # XXX enable setting this on a <<field>> class in Poseidon
        'multiValued': True,
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()


    security.declarePrivate('set')
    security.declarePrivate('get')


    def getDefault(self, instance):
        """Return the default value to be used for initializing this
        field, defaulting to the field's vocabulary."""
        default = LinesField.getDefault(self, instance)
        if not default:
            return self.vocabulary.getDisplayList(instance)


registerField(SelectedLinesField,
              title='SelectedLinesField',
              description='')

##code-section module-footer #fill in your manual code here
# Description for SelectedLinesField
#   Used for a sequence. Starts out with the whole vocabulary selected.
##/code-section module-footer



