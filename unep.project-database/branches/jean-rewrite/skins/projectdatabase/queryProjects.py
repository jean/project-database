from ZODB.POSException import ConflictError
from Products.ZCTextIndex.ParseTree import ParseError
from Products.CMFCore.utils import getToolByName
quote_logic_indexes=['SearchableText','Description','Title']
quote_logic=0

REQUEST=None

if REQUEST is None:
    REQUEST = context.REQUEST

results=[]
catalog=context.portal_catalog
indexes=catalog.indexes()
query={}
#show_query=show_all
second_pass = {}


def quotestring(s):
    return '"%s"' % s

def quotequery(s):
    if not s:
        return s
    try:
        terms = s.split()
    except ConflictError:
        raise
    except:
        return s
    tokens = ('OR', 'AND', 'NOT')
    s_tokens = ('OR', 'AND')
    check = (0, -1)
    for idx in check:
        if terms[idx].upper() in tokens:
            terms[idx] = quotestring(terms[idx])
    for idx in range(1, len(terms)):
        if (terms[idx].upper() in s_tokens and
            terms[idx-1].upper() in tokens):
            terms[idx] = quotestring(terms[idx])
    return ' '.join(terms)

# We need to quote parentheses when searching text indices (we use
# quote_logic_indexes as the list of text indices)
def quote_bad_chars(s):
    bad_chars = ["(", ")"]
    for char in bad_chars:
        s = s.replace(char, quotestring(char))
    return s


# Avoid creating a session implicitly.
REQUEST_keys=['SearchableText','Title','getRawCurrent_task_manager','getFocal_area','getStrategic_priority','getProject_type','getPipeline_number','getScope','getRegion','getCountry','getLeadagency','getOperational_programme','getGef_phase','path','portal_type','review_state']
for k in REQUEST_keys:
    #if k in ('SESSION',):
    #    continue
    v = REQUEST.get(k)
    if v and k in indexes:
        if k in quote_logic_indexes:
            v = quote_bad_chars(v)
            if quote_logic:
                v = quotequery(v)
        query[k] = v
        show_query = 1
    elif k.endswith('_usage'):
        key = k[:-6]
        param, value = v.split(':')
        second_pass[key] = {param:value}
    elif k in ('sort_on', 'sort_order', 'sort_limit'):
        if k == 'sort_limit' and not same_type(v, 0):
            query[k] = int(v)
        else:
            query[k] = v

for k, v in second_pass.items():
    qs = query.get(k)
    if qs is None:
        continue
    query[k] = q = {'query':qs}
    q.update(v)

# doesn't normal call catalog unless some field has been queried
# against. if you want to call the catalog _regardless_ of whether
# any items were found, then you can pass show_all=1.
if show_query:
    try:
        results = catalog(query, show_inactive=False)
    except ParseError:
        pass
#print query


# If this query has no results, then why should we go on ?
if not results:
 	return None

pathlist =[]
for r in results:
    pathlist.append(r.getPath())

#print pathlist
#print '\n\n<br/><hr/>'

qfmi = {}
Title=REQUEST.get('FMITitle',None)
if Title:
	qfmi['Title']=Title

getFinance_category=REQUEST.get('getFinance_category')
if getFinance_category:
   qfmi['getFinance_category'] = getFinance_category

Pms_number=REQUEST.get('getPms_number',None)
if Pms_number:
	qfmi['getPms_number'] = Pms_number

Imis_number=REQUEST.get('getImis_number',None)
if Imis_number:
	qfmi['getImis_number'] = Imis_number

if pathlist:
	qfmi['path'] = pathlist 

qfmi['portal_type']='FinancialManagementInformation'

if Title or Imis_number or Pms_number or getFinance_category:
    try:
        results = catalog(qfmi, show_inactive=False)
    except ParseError:
        pass
    #print qfmi

    if not results:
       return None
    alist=[]
    for r in results:
        parentpath = '/'.join(r.getObject().aq_parent.getPhysicalPath())
        if not parentpath in alist:
            alist.append(parentpath)        

    #print '\n\n<br/><hr/>'
    print alist
else:
	#if we do not query any fmi we still have the same paths
	alist = pathlist   


#query the Milestone dates:
qmd ={}

#if alist:
qmd['path'] = alist

qmd['portal_type']='MilestoneDates'

Gef_phase=REQUEST.get('getMileStoneGef_phase',None)
if Gef_phase:
   qmd['getImplementation_status'] = Gef_phase

getMilestoneName=REQUEST.get('getMilestoneName', None)
if getMilestoneName:
   qmd['getMilestone_name'] = getMilestoneName

if Gef_phase or getMilestoneName:
    try:
        results = catalog(qmd, show_inactive=False)
    except ParseError:
        pass
    print qmd
    if not results:
       return None
    alist=[]
    for r in results:
        parentpath = '/'.join(r.getObject().aq_parent.getPhysicalPath())
        if not parentpath in alist:
            alist.append(parentpath)        

    #print '\n\n<br/><hr/>'
    print alist
else:
	#if we do not query any fmi we still have the same paths
        pass
	#alist = pathlist   

#finally we want to get the projects
#this is a bit brute force ...

q={}
q['path']=alist
q['portal_type']='Project'
if alist:
    try:
        results = catalog(q, show_inactive=False)
    except ParseError:
        pass

#print alist
#return printed
return results
