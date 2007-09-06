includePD = [ 'Project' ]
includeContacts = [ 'Agency', 'mxmContacts' ]
types = context.sortObjects( context.allowedContentTypes() )
if context.getId() == 'projectdatabases':
    return [ ctype for ctype in types if ctype.getId() in includePD ] 
elif context.getId() == 'contacts':
    return [ ctype for ctype in types if ctype.getId() in includeContacts ]
elif context.portal_type == 'Project':
    return []
else:
    return [ ctype for ctype in types if ctype.getId() ]
