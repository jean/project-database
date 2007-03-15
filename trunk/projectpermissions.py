from Products.CMFCore.CMFCorePermissions import setDefaultRoles
import Products.Archetypes.public as atapi
import config

projectpermissions = {}
types = atapi.listTypes(config.PROJECTNAME)
for atype in  types:
    permission = "%s: Add %s" % (config.PROJECTNAME, atype['portal_type'])
    projectpermissions[atype['portal_type']] = permission

    # Assign default roles
    setDefaultRoles(permission, ('Member',
                                 'Contributor',
                                 'Manager',
                                 'Anonymous'
                                 )
                    )

    permission = "%s: Edit %s" % (config.PROJECTNAME, atype['portal_type'])
    projectpermissions[atype['portal_type']] = permission

    # Assign default roles
    # setDefaultRoles(permission, ('Member',
                                 # 'Contributor',
                                 # 'Manager',
                                 # 'Anonymous'
                                 #  )
                    #  )
  




