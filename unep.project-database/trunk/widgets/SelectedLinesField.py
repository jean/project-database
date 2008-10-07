# -*- coding: utf-8 -*-
#
# File: SelectedLinesField.py
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
##/code-section module-header

from zope.interface import implements
from Products.Archetypes.Field import LinesField
from Products.ProjectDatabase.interfaces.ISelectedLinesField import ISelectedLinesField
from Products.Archetypes.Widget import MultiSelectionWidget
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class SelectedLinesField(LinesField):
    """A lines field that starts off with all vocabulary items selected
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    implements(ISelectedLinesField)


    _properties = LinesField._properties.copy()
    _properties.update({
        'type': 'selectedlinesfield',
        'widget':MultiSelectionWidget,
        ##code-section field-properties #fill in your manual code here
        'multiValued': True,
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()


    security.declarePrivate('set')
    security.declarePrivate('get')


    def getDefault(self,instance):
        """Return the default value to be used for initializing this
        field, defaulting to the field's vocabulary."""
        default = LinesField.getDefault(self, instance)
        if not default:
            return self.vocabulary.getDisplayList(instance)

    def getRaw(self, instance, **kwargs):
        return LinesField.getRaw(self, instance, **kwargs)

    def set(self, instance, value, **kwargs):
        return LinesField.set(self, instance, value, **kwargs)

    def get(self, instance, **kwargs):
        return LinesField.get(self, instance, **kwargs)


registerField(SelectedLinesField,
              title='SelectedLinesField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



