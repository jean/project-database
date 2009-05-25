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
#logger.info('project type:%s', context.REQUEST.get('project_type'))

report = context.REQUEST.get('report', None)
logger.info('view: %s', report)
if not report:
    return state.set(status='failure')

return context.restrictedTraverse(report)()
#return state
