import transaction
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.migrations.migration_util import safeEditProperty
from Products.ProjectDatabase.content.ProjectDatabase import ProjectDatabase
from Products.ProjectDatabase.content.CountryClassificationSystem import CountryClassificationSystem

PRODUCT_DEPENDENCIES = (
        'ATExtensions', 
        'ATSchemaEditorNG', 
        'FinanceFields', 
        'DataGridField', 
        'ATVocabularyManager',
        'UpfrontContacts', 
        'ProjectDatabase', 
        'unep.theme',
        )
DEPENDENT_EXTENSION_PROFILES = (
        'membrane:default', 
        'remember:default',
        )
EXTENSION_PROFILES = (
        'unep.policy:default', 
        )

def Install(self, reinstall=False):
    pqi = getToolByName(self, 'portal_quickinstaller')
    psu = getToolByName(self, 'portal_setup')

    # we need to do membrane and remember first
    for extension_id in DEPENDENT_EXTENSION_PROFILES:
        psu.runAllImportStepsFromProfile('profile-%s' % extension_id, purge_old=False)
        product_name = extension_id.split(':')[0]
        pqi.notifyInstalled(product_name)
        transaction.savepoint()

    # now we do all the old-style 2.5 products
    for product in PRODUCT_DEPENDENCIES:
        if reinstall and pqi.isProductInstalled(product):
            pqi.reinstallProducts([product])
            transaction.savepoint()
        elif not pqi.isProductInstalled(product):
            pqi.installProduct(product)
            transaction.savepoint()

    # now we do the policy product
    for extension_id in EXTENSION_PROFILES:
        psu.runAllImportStepsFromProfile('profile-%s' % extension_id, purge_old=False)
        product_name = extension_id.split(':')[0]
        pqi.notifyInstalled(product_name)
        transaction.savepoint()

    portal = getToolByName(self,'portal_url').getPortalObject()

    # # add default contact groups
    # if 'Evaluators' not in portal.contentIds():
    #     portal.invokeFactory('UpfrontContacts', 'Evaluators', title='Evaluators')

    # add default project databases folder
    if 'projectdatabases' not in portal.contentIds():
        projdb = ProjectDatabase('projectdatabases')
        portal._setObject('projectdatabases', projdb)
        projdb = portal['projectdatabases']
        projdb.title='PROJECTS'
        projdb.reindexObject()

    # add global contact manager
    if 'contacts' not in portal.contentIds():
        portal.invokeFactory('ContactManager', 'contacts', title='STAFF & CONTACTS')

    # add country classification system
    if 'countryclassification' not in portal.contentIds():
        ccs = CountryClassificationSystem('countryclassification')
        portal._setObject('countryclassification', ccs)
        ccs = portal['countryclassification']
        ccs.title='Country Classification System'
        ccs.reindexObject()

    # remove unneeded folders
    ids=['Members', 'news', 'events', 'front-page']
    for id in ids:
        if id in portal.objectIds():
            portal.manage_delObjects(ids=[id])

    portal.portal_vocabularies.reindexObject()
 
    # remove portlets
    safeEditProperty(portal, 'left_slots', (), 'lines')
    safeEditProperty(portal, 'right_slots', (), 'lines')
