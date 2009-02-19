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

import logging 
logger = logging.getLogger("Add M&E")
logger.info("Inside add mandeo: %s" %"/".join(context.getPhysicalPath()))

result='failure'
message='Could not add M&E.'

if etype == 'PIRRating':
    newid = context.generateUniqueId(type_name = 'PIRRating')
    logger.info("New ID: %s", newid)
    context.invokeFactory(id=newid, type_name='PIRRating')
    new_context = context[newid]
else:
    #create id
    pc = context.portal_catalog
    brains = pc( \
        portal_type='MonitoringAndEvaluation', \
        path="/".join(context.getPhysicalPath()), \
        sort_on='created', \
        sort_order='reverse')
    if len(brains) == 0:
        childrenCount = 0
    else:
        childrenCount = int(brains[0].getId.split('-')[1])
    id = '%s-%s' % (etype, childrenCount + 1)

    #create object
    context.invokeFactory(id=id, type_name='MonitoringAndEvaluation')
    new_context = context[id]
    new_context.edit(title=id, EvaluationType=etype)

message = 'Create M&E Object %s successfully' % etype
result = 'success'

return state.set(context=new_context, status=result, portal_status_message=message)
