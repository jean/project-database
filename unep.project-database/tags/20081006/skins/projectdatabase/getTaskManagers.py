catalog = container.portal_catalog
results = catalog(portal_type='Project', path='/'.join(context.getPhysicalPath()))

udict = {}
for item in results:
     o = item.getObject()
     try:
       tms = o.getCurrent_task_manager()
       for tm in tms:
         #print tm.Title()
         #print tm.UID()
         udict [tm.UID()] = tm.Title()
     except:
       print o.id

print udict
rlist =[]
for key in udict.keys():
    rlist.append([key, udict[key]])
return rlist
#return printed
