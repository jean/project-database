## Script (Python) "validate_add_financial"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=category
##title=Validates adding a financial object
##

from Products.CMFPlone import PloneMessageFactory as _
import logging
logger = logging.getLogger("Validate Add Financial")
logger.info("Inside validate with %s" % category)

if category in context.object_ids():
    context.plone_utils.addPortalMessage(_(u'Finacial object already exists.'), 'error')
    return state.set(status='failure')
else:
    logger.info("leaving validate with %s" % category)
    return state

