includePD = [ 'ProjectDatabase' ]
includeContacts = [ 'Agency', 'mxmContacts' ]
types = context.sortObjects( context.allowedContentTypes() )
if context.getId() == 'projectdatabases':
    return [ ctype for ctype in types if ctype.getId() in includePD ] 
elif context.getId() == 'contacts':
    return [ ctype for ctype in types if ctype.getId() in includeContacts ]
else:
    return [ ctype for ctype in types if ctype.getId() ]
