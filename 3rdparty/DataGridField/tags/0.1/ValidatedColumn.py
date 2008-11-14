"""

    Column with validation support definition for DataGridField


"""

from __future__ import nested_scopes
__author__ = 'Simon Pamies'
__docformat__ = 'reStructuredText'

# Python imports
import StringIO


# Zope imports
from AccessControl import ClassSecurityInfo
from AccessControl import getSecurityManager
from Globals import InitializeClass

from ZODB.POSException import ConflictError

# Plone imports
from Products.CMFCore.utils import getToolByName
from Products.CMFCore import permissions
from Products.Archetypes.public import *
from Products.Archetypes.Field import ObjectField, encode, decode, registerField

# Local imports
from Products.DataGridField import DataGridWidget
from Products.DataGridField.interfaces import IDataGridField
from Products.DataGridField.Column import Column

validator_mapping = {'printable':'isPrintable', 
                     'int':'isInt',
                     'notempty':'isNotEmpty',
                     'decimal':'isDecimal',
                     'mail':'isEmail'}

class ValidatedColumn(Column):
    """ Defines column that can be validated """

    security = ClassSecurityInfo()

    def __init__(self, title, validator, default=None):
        """ Create a ValidatedColumn

        @param vocabulary Vocabulary method name. This method is called
               from Archetypes instance to get values for dropdown list.
        """

        Column.__init__(self, title, default=default)
        self.validator = validator_mapping.get(validator, None)
        if self.validator is None:
            raise Exception, '%s is not recognized as valid validator! (Valid ones: %s)' % (validator, validator_mapping.keys())

        self._validator_raw = validator

    def getValidator(self):
        """ Returns the associated validator """

        return self.validator and self.validator or None

    def getValidatorRaw(self):
        """ Returns the readable name for the validator """

        return self._validator_raw

# Initializes class security
InitializeClass(ValidatedColumn)
