## Script (Python) "generateUniqueId"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=type_name=None
##title=
##
from DateTime import DateTime
from random import random
import logging

logger = logging.getLogger('generateUniqueId')
logger.info('Type Name %s', type_name)

if type_name == 'Project':
    return context.getNextProjectId()

now=DateTime()
time='%s.%s' % (now.strftime('%Y-%m-%d'), str(now.millis())[7:])
rand=str(random())[2:6]
prefix=''
suffix=''

if type_name is not None:
    prefix = type_name.replace(' ', '_')+'.'
prefix=prefix.lower()

return prefix+time+rand+suffix
