## Script (Python) "add_financial.cpy"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=category
##title=
##
''' import a journal csv file
'''
import logging 
logger = logging.getLogger("Add Financial")
logger.info("Inside add financial with %s" % category)


#defaults
status='failure'
message='Could not add financial.'

context.invokeFactory(
    id=category, 
    type_name='Financials')
fin_obj = getattr(context, category)
find_obj.edit('Title'=category, 'FinancialCategory'=category)
find_obj.reindexObject()


message= 'Create Finance Object %s successfully' % category
status='success'

return state.set(status=status, portal_status_message=message)

