"""

    Calendar column 

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

# Plone imports
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import *

# Local imports
from Products.DataGridField.Column import Column

class CalendarColumn(Column):
    """ Allow user select one from the build it Calendar
    
    """
    security = ClassSecurityInfo()

    security.declarePublic('getMacro')
    def getMacro(self):
        """ Return macro used to render this column in view/edit """
        return "datagrid_calendar_cell"

    security.declarePublic('processCellData')
    def processCellData(self, form, value, context, field, columnId):
        """ Read cell values from raw form data
        
        Read special table for radio button columns from form data.
        The selected radio button cell id is placed as a cell value.
        """
        
        newValue = []
        
        return value

        
# Initializes class security
InitializeClass(CalendarColumn)
