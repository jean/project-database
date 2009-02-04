## Controller Python Script "add_financial"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=category
##title=
##

import logging 
logger = logging.getLogger("Add Financial")
logger.info("Inside add financial with %s" % category)


result='failure'
message='Could not add financial.'

context.invokeFactory(id=category, type_name='Financials')
new_context = context[category]
new_context.edit(Title=category, FinancialCategory=category)

message = 'Create Finance Object %s successfully' % category
result = 'success'

return state.set(context=new_context, status=result, portal_status_message=message)
