"""
Start the import process by:
- getting the CSV payload
- encoding it in the portal encoding
- calling the relevant external method
"""
from types import ListType

from Acquisition import aq_inner
from zope.interface import implements

from Products.Five import BrowserView

from Products.ProjectDatabase.import_pgi_csv import run

from interfaces import IImportForm

class ImportForm(BrowserView):
    """
    View for importing content
    """
    implements(IImportForm)

    def action(self):
        context = aq_inner(self.context)
        request = context.REQUEST

        csvfile = request.get('csvfile')

        # Validate
        errors = {}
        if not csvfile:
            errors['csvfile'] = "Please specify a file"

        if errors:
            import_form = context.restrictedTraverse('@@unep.import-form')
            return import_form(REQUEST=request, errors=errors)

        # Delegate to external method
        msg = run(context, csvfile, debug=1)

        # Make msg a list because the global_status macro doesn't handle line breaks well
        if not isinstance(msg, ListType):
            msg = [msg]
        for m in msg:
            context.plone_utils.addPortalMessage(m)
        
        redirect_url = '%s/%s' % (context.absolute_url(), '@@unep.import-form')
        request.RESPONSE.redirect(redirect_url)
