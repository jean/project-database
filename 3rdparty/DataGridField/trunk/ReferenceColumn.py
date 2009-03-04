"""

    Reference column 

    Copyright 2007 Upfront Systems
    
    Licensed under GPL.

"""

from __future__ import nested_scopes
__author__ = ""
__docformat__ = 'reStructuredText'

# Python imports
import StringIO
from types import DictType, TupleType, ListType

# Zope imports
from AccessControl import ClassSecurityInfo
from AccessControl import getSecurityManager
from Globals import InitializeClass
from types import ListType, TupleType

# Plone imports
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import *
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from DateTime import DateTime

# Local imports
from Products.DataGridField.Column import Column

class ReferenceColumn(Column):
    """
    Defines DataGridField column with object UIDs and titles
    """
    security = ClassSecurityInfo()

    def __init__(self, title, fieldname, default=None):
        """ 
        Create a ReferenceColumn

        @param fieldname The field that must be updated on the object that
        this widget provides UI for.
        """
        Column.__init__(self, title, default=default)
        self._fieldname = fieldname

    security.declarePublic('getMacro')
    def getMacro(self):
        """ 
        Return macro used to render this column in view/edit 
        """
        return "datagrid_reference_cell"

    security.declarePublic('processCellData')
    def xxxprocessCellData(self, form, value, context, field, columnId):
        """
        Override
        """
        Column.processCellData(self, form, value, context, 
          field, columnId)
        context.getField(self._fieldname).set(context, value)
    
    security.declarePublic('getFakeReferenceField')
    def getFakeReferenceField(self, context):
        """
        Return the ReferenceField as provided by the object in context. 
        This is needed by the referencebrowser widget macros.
        """
        return context.Schema()[self._fieldname]

        field = context.Schema()[self._fieldname].copy()
        field.multiValued = 0
        return field

    security.declarePublic('sanitize')
    def sanitize(self, context, value):
        """
        Inspect value and replace invalid UIDs with empty strings. This
        is needed because the referencebrowser widgets are not fault
        tolerant.
        """ 
        pc = getToolByName(context, 'portal_catalog')

        # We need an iterable
        if isinstance(value, ListType) or isinstance(value, TupleType):
            values = value
        else:
            values = [value]

        result = []
        for v in values:
            if pc(UID=v):
                result.append(v)
            else:
                result.append('')

        # Result type must be consistent with input type
        if isinstance(value, ListType) or isinstance(value, TupleType):
            return result
        else:
            if result:
                return result[0]
            else: 
                return ''

# Initializes class security
InitializeClass(ReferenceColumn)
