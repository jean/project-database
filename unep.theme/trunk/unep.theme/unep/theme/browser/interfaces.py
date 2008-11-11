from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IUnepViewUtils(Interface):
    """ Marker interface for the UNEP main browser utility view class
    """

    def projectDatabasesURL(self):
        """ return the URL of the project databases folder
        """

    def contactsURL(self):
        """ return the URL of the contacts manager
        """
