import transaction
from Products.CMFCore.utils import getToolByName
PRODUCT_DEPENDENCIES = (
        'ATExtensions', 
        'ATSchemaEditorNG', 
        'FinanceFields', 
        'DataGridField', 
        'ATVocabularyManager',
        'UpfrontContacts', 
        'ProjectDatabase', 
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
