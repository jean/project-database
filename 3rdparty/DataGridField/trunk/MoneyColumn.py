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
from Products.FinanceFields.Money import Money, InvalidMoneyString
from Products.DataGridField.Column import Column

class MoneyColumn(Column):
    """
    Defines MoneyField column    
    """
    security = ClassSecurityInfo()

    def __init__(self, title, field, default=None, col_width="100"):
        """ 
        Create a MoneyColumn

        @param field Field and widget specification.
        """
        Column.__init__(self, title, default=default, col_width=col_width)
        self._field = field

    security.declarePublic('getDefault')
    def getDefault(self, context):
        if self._field.use_global_currency:
          currency = self._field.getGlobalCurrency()
        else:
          currency = self._field.getDefaultCurrency(context)
        return Money(self._field.default, currency)

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
                if self._field.use_global_currency:
                    currency = self._field.getGlobalCurrency()
                else:
                    currency = di.get(columnId + '_currency', None)
                try:
                    money = Money(di[columnId], currency)
                except InvalidMoneyString:
                    money = Money('0.00', currency)
                row[columnId] = money

            result.append(row)

        return result

    security.declarePublic('getField')
    def getField(self):
        return self._field

# Initializes class security
InitializeClass(MoneyColumn)
