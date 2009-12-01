from Acquisition import aq_inner
from zope.interface import implements
from Products.Five import BrowserView
from interface import IUnepUtilities
from Products.CMFCore.utils import getToolByName

class UnepUtilities(BrowserView):
    """ Utilities class for UNEP project database
    """

    implements(IUnepUtilities)

    def getUnepVocabulary(self, vocabulary_name):
        """ return a vocabulary from ATVocabulary manager
        """
        context = aq_inner(self.context)
        atvm = getToolByName(context, 'portal_vocabularies')
        vocabulary = atvm.getVocabularyByName(vocabulary_name)
        return vocabulary.getDisplayList(context)

