from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole
from Products.CMFPlone import PloneMessageFactory as _

class FMORole(object):
    implements(ISharingPageRole)
    title = _(u'title_fmo_role', u'FMO')
    required_permission = 'Manage portal content'
