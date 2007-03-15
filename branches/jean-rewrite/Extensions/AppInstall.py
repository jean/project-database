from StringIO import StringIO
from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
from Products.CMFCore.utils import getToolByName

def install(self):
    """ Do stuff that GS will do for us soon ..
    """
    out = StringIO()

    setup_tool = getToolByName(self, 'portal_setup')
    setup_tool.setImportContext('profile-ProjectDatabase:default')
    result = setup_tool.runAllImportSteps()
    out.write( 'Steps run: %s \n' % ', '.join(result['steps']) )

    portal = getToolByName(self,'portal_url').getPortalObject()

    # Create 'Agency' objects for us, until we have an Agency type that
    # supports import/export.
    if 'contacts' not in portal.contentIds():
        portal.invokeFactory('Folder', 'contacts', title='Contacts')
        for id, title in (
                ('AFDB', 'African Development Bank'),
                ('ADB', 'Asian Development Bank'),
                ('EBRD', 'European Bank for Reconstruction and Development'),
                ('FAO', 'Food and Agriculture Organization'),
                ('IADB', 'Inter-American Development Bank'),
                ('IFAD', 'International Fund for Agriculture and Development'),
                ('UNDP', 'United Nations Development Programme'),
                ('UNEP', 'United Nations Environment Programme'),
                ('IBRD', 'World Bank'),
                ):
            portal.contacts.invokeFactory('Agency', id.lower(), title=title)
        out.write('Added agencies.')

    return out


def uninstall(self):
    """ 
    """

    # # Remove the content we added
    # portal = getToolByName(self,'portal_url').getPortalObject()
    # if 'contacts' in portal.contentIds():
    #     portal.manage_delObjects('contacts')

