from zope.interface import Interface

class IImportForm(Interface):
    """ 
    Interface for Import form
    """

    def action(self):
        """
        Validate form, do import
        """

