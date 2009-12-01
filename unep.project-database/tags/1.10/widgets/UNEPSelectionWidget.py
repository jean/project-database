# -*- coding: utf-8 -*-
#
# File: UNEPSelectionWidget.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Rijk Stofberg <mikejmets@gmail.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.Archetypes.Widget import TypesWidget

from Products.ProjectDatabase import config

##code-section module-header #fill in your manual code here
##/code-section module-header

from zope.interface import implements

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class UNEPSelectionWidget(TypesWidget):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : 'UNEPSelectionWidget',
        'size' : '30',
        'maxlength' : '255',
        ##code-section widget-properties #fill in your manual code here
        'format' : "flex",
        'blurrable' : True,
        ##/code-section widget-properties

        })

    security = ClassSecurityInfo()



registerWidget(UNEPSelectionWidget,
               title='UNEPSelectionWidget',
               description=('no description given'),
               used_for=('Products.Archetypes.Field.StringField',)
               )
##code-section module-footer #fill in your manual code here
##/code-section module-footer



