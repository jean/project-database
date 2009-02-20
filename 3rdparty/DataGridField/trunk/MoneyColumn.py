"""

    Money column 

    Copyright 2007 Upfront Systems
    
    Licensed under GPL.

"""

from __future__ import nested_scopes
__author__ = ""
__docformat__ = 'reStructuredText'

# Zope imports
from AccessControl import ClassSecurityInfo
from AccessControl import getSecurityManager
from Globals import InitializeClass

# Plone imports
from Products.CMFCore.utils import getToolByName

# Local imports
from Products.FinanceFields.Money import Money
from Products.DataGridField.Column import Column

class MoneyColumn(Column):
    """
    Defines MoneyField column    
    """
    security = ClassSecurityInfo()

    def __init__(self, title, field, default=None):
        """ 
        Create a MoneyColumn

        @param field Field and widget specification.
        """
        Column.__init__(self, title, default=default)
        self._field = field

    security.declarePublic('getDefault')
    def getDefault(self, context):
        return Money(self._field.default, self._field.getDefaultCurrency(context))

    security.declarePublic('getMacro')
    def getMacro(self):
        """ 
        Return macro used to render this column in view/edit 
        """
        return "datagrid_money_cell"

    security.declarePublic('processCellData')
    def processCellData(self, form, value, context, field, columnId):
        """
        Marshall form data
        """
        result = []
        for di in value:            
            # We must clone row since row is readonly ZPublished.HTTPRequest.record object
            row = {}
            for key in di.keys():
                row[key] = di[key]

            if di['orderindex_'] != 'template_row_marker':
                # Attempt to convert to Money. Falied conversion can be avoided by
                # the calling application doing validation.
                try:
                    money = Money(di[columnId], di[columnId + '_currency'])
                except ValueError:
                    money = Money('0.00', self._field.getDefaultCurrency(context).int_currency_symbol)
                row[columnId] = money

            result.append(row)

        return result

    security.declarePublic('getField')
    def getField(self):
        return self._field

# Initializes class security
InitializeClass(MoneyColumn)
