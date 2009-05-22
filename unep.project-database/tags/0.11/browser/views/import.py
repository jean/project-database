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

from Products.ProjectDatabase.content.Project import Project_CSVImporter
from Products.ProjectDatabase.content.Financials import Financial_CSVImporter
from Products.ProjectDatabase.content.SubProject import SubProject_CSVImporter
from Products.ProjectDatabase.content.Milestone import Milestone_CSVImporter

from interfaces import IImportForm

class ImportForm(BrowserView):
    """
    View for importing content
    """
    implements(IImportForm)

    def setup(self):
        self._request = self.context.REQUEST
        self._csvfile = self._request.get('csvfile')
        self._coding = 'latin-1'
        self._debug = self._request.get('debug', 0)
        self._import_form = \
                self.context.restrictedTraverse('@@unep.import-form')
        # Validate
        self._errors = {}
        if not self._csvfile:
            self._errors['csvfile'] = "Please specify a file"

    def import_financials(self):
        self.setup()
        if self._errors:
            return self._import_form(REQUEST=self._request, errors=self._errors)
        # Delegate to external method
        csv_importer = Financial_CSVImporter(
                               context=self.context,
                               csvfile=self._csvfile,
                               coding=self._coding,
                               debug=self._debug)
        msg = csv_importer.importCSV()
        self.returnResult(msg)

    def import_projects(self):
        self.setup()
        if self._errors:
            return self._import_form(REQUEST=self._request, errors=self._errors)
        # Delegate to external method
        csv_importer = Project_CSVImporter(
                               context=self.context,
                               csvfile=self._csvfile,
                               coding=self._coding,
                               debug=self._debug)
        msg = csv_importer.importCSV()
        self.returnResult(msg)

    def import_subprojects(self):
        self.setup()
        if self._errors:
            return self._import_form(REQUEST=self._request, errors=self._errors)
        # Delegate to external method
        csv_importer = SubProject_CSVImporter(
                                  context=self.context,
                                  csvfile=self._csvfile,
                                  coding=self._coding,
                                  debug=self._debug)
        msg = csv_importer.importCSV()
        self.returnResult(msg)

    def import_milestones(self):
        self.setup()
        if self._errors:
            return self._import_form(REQUEST=self._request, errors=self._errors)
        # Delegate to external method
        csv_importer = Milestone_CSVImporter(
                                 context=self.context,
                                 csvfile=self._csvfile,
                                 coding=self._coding,
                                 debug=self._debug)
        msg = csv_importer.importCSV()
        self.returnResult(msg)

    def returnResult(self, msg=[]):
        """
        Make msg a list because the global_status macro doesn't handle
        line breaks well
        """
        if not isinstance(msg, ListType):
            msg = [msg]
        for m in msg:
            self.context.plone_utils.addPortalMessage(m)
        
        redirect_url = '%s/%s' % (self.context.absolute_url(),
                       '@@unep.import-form')
        self._request.RESPONSE.redirect(redirect_url)
