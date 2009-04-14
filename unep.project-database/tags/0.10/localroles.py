from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole
from Products.CMFPlone import PloneMessageFactory as _

class FMORole(object):
    """
    Role for Financial Management Officer
    """
    implements(ISharingPageRole)
    title = _(u'title_fmo_role', u'FMO')
    required_permission = 'Manage portal content'

class MORole(object):
    """
    Role for Monitoring Officer
    """
    implements(ISharingPageRole)
    title = _(u'title_mo_role', u'MO')
    required_permission = 'Manage portal content'

class EORole(object):
    """
    Role for Evaluation Officer
    """
    implements(ISharingPageRole)
    title = _(u'title_eo_role', u'EO')
    required_permission = 'Manage portal content'

class RegistrarRole(object):
    """
    Role for Registrar
    """
    implements(ISharingPageRole)
    title = _(u'title_registrar_role', u'Registrar')
    required_permission = 'Manage portal content'

class TMRole(object):
    """
    Role for Task Manager
    """
    implements(ISharingPageRole)
    title = _(u'title_tm_role', u'TM')
    required_permission = 'Manage portal content'

class SPORole(object):
    """
    Role for Senior Programme Officer
    """
    implements(ISharingPageRole)
    title = _(u'title_spo_role', u'SPO')
    required_permission = 'Manage portal content'

class SPMORole(object):
    """
    Role for <Unknown TLA>
    """
    implements(ISharingPageRole)
    title = _(u'title_spmo_role', u'SPMO')
    required_permission = 'Manage portal content'

class SMRole(object):
    """
    Role for Senior Manager
    """
    implements(ISharingPageRole)
    title = _(u'title_sm_role', u'SM')
    required_permission = 'Manage portal content'
