"""
Helper classes and function to save us from tedious copy and paste 
work when extending AT schemas with schemaextender.
"""
from Products.Archetypes.atapi import *
from Products.Archetypes.Field import __all__ as ATField_all
from Products.DataGridField import DataGridField
from archetypes.schemaextender.field import ExtensionField
from copy import deepcopy

def _at_field_copy(field, name=None):
        """
        Same as Archetypes.Field except for last line of method
        """
        cdict = dict(vars(field))
        cdict.pop('__name__')
        # Widget must be copied separatedly
        widget = cdict['widget']
        del cdict['widget']
        properties = deepcopy(cdict)
        properties['widget'] = widget.copy()
        name = name is not None and name or field.getName()
        properties['name'] = name
        return properties

ATField_all = ATField_all + ('DataGridField',)
for klass in ATField_all:
    exec("class ef%s(ExtensionField, %s): pass" % (klass, klass))
