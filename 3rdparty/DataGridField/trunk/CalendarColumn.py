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
from DateTime import DateTime

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
        """
        result = []
        for di in value:
            # Skip over marker row
            if di["orderindex_"] == 'template_row_marker':
                continue

            # Clone row since ZPublished.HTTPRequest.record object
            # is readonly            
            row = {}
            for key in di.keys():
                row[key] = di[key]

            # Convert to datetime
            try:
                row[columnId] = DateTime(row[columnId])
            except:
                row[columnId] = None
           
            result.append(row)

        return result
        

        
# Initializes class security
InitializeClass(CalendarColumn)
