## Controller Python Script "retrieve_projects"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=
##

import logging
logger = logging.getLogger('retrieve_projects')

# report = context.REQUEST.get('report', None)
# logger.info('view: %s', report)
# if not report:
#     return state.set(status='failure')

brains = context.restrictedTraverse('@@unepsearch')(context.REQUEST)
projects = '|'.join([b.UID for b in brains])
logger.info('projects: %s', projects)
context.REQUEST.set('projects', projects)
return state
