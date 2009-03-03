## Controller Python Script "add_financial"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=etype
##title=
##

from Products.CMFCore.utils import getToolByName

import logging 
logger = logging.getLogger("Add M&E")
logger.info("Inside add mandeo: %s" %"/".join(context.getPhysicalPath()))

portal_type = etype
mande_type = None
if etype in ['MTR', 'MTE', 'TE', 'EOF']:
    portal_type = 'MonitoringAndEvaluation'
    mande_type = etype

logger.info("Type: %s", portal_type)

pf = getToolByName(context, 'portal_factory')
if pf.getFactoryTypes().has_key(portal_type):
    if portal_type == 'PIRRating':
        # get PIRRating id
        newid = context.generateUniqueId(type_name = portal_type)
        new_url = 'portal_factory/' + portal_type + '/' + newid + '/edit'

    else:
        #create M&E instance id
        pc = getToolByName(context, 'portal_catalog')
        brains = pc( \
            portal_type='MonitoringAndEvaluation', \
            path="/".join(context.getPhysicalPath()), \
            sort_on='created', \
            sort_order='reverse')
        if len(brains) == 0:
            childrenCount = 0
        else:
            childrenCount = int(brains[0].getId.split('-')[1])
        newid = '%s-%s' % (mande_type , childrenCount + 1)
        new_url = 'portal_factory/%s/%s/edit?EvaluationType=%s&amp;title=%s' \
                %(portal_type, newid, mande_type, newid)

    logger.info("New ID: %s", newid)
    logger.info("New URL: %s", new_url)
    state.set(status='factory', next_action='redirect_to:string:%s'%new_url)

    return state

else:
    raise '''Only objects created through portal factory can be inserted into
    the Monitoring and Evaluation section of a project.'''
