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
        
        newValue = []
        
        #print "form value:" + str(form)
        
        for row in value:
            
            # we must clone row since
            # row is readonly ZPublished.HTTPRequest.record object
            newRow = {}
            for key in row.keys():
                newRow[key] = row[key]
                        
            try:
                orderIndex = int(row["orderindex_"])
                cellId = "%s.%s" % (field.getName(), columnId)
                if form.has_key(cellId):
                    start = orderIndex * 6 - 6
                    end = orderIndex * 6 
                    valList = form[cellId][start:end]
                    if valList[1] != '00' and valList[2] != '00':
                        new_date_str = "%s/%s/%s" % (valList[0], valList[1], valList[2])
                        #new_date = DateTime(new_date_str)
                        newRow[columnId] = DateTime(new_date_str)
            except IndexError:
                pass
            except ValueError:
                pass

            newValue.append(newRow)
            
        return newValue
        

        
# Initializes class security
InitializeClass(CalendarColumn)
