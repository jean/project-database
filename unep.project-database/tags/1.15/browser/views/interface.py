from zope.interface import Interface

class IUnepUtilities(Interface):
    """ Marker interface for the UNEP utilities view
    """

    def getUnepVocabulary(vocabulary_name):
        """ return a vocabulary from ATVocabulary manager
        """
