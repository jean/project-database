from Acquisition import aq_inner
from zope.interface import implements

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from interfaces import IUtilView

class UtilView(BrowserView):
    """
    View for utility methods
    """
    implements(IUtilView)

    def assemble_categories(self, skip_empty_rows=False, skip_empty_columns=False, 
            skip_empty_vocab_columns=False, parent_filtered=False):

        context = aq_inner(self.context)

        # xxx: sorry for the strange names. fields are columns and lines are rows.


        # In some cases the available options must be a subset of what the parent has set, eg. an FSP
        # constrains the options available to Key Individuals.
        if parent_filtered:

            # Recurse
            view = context.aq_parent.restrictedTraverse(str('@@%s' % self.__name__))
            parent_matrix = view(skip_empty_rows=True, 
                skip_empty_columns=True, skip_empty_vocab_columns=True)

            parent_fields = {}
            for field in parent_matrix[0][1:]:
                parent_fields[field] = getattr(context.aq_parent, field.accessor)() 

            parent_license_category_ids = []
            for row in parent_matrix[1:]:
                parent_license_category_ids.append(row[0]['key'])

        rows = []

        # Get all *Vocab field values on portal_moonstone as a flat list. Kill dupes.
        pms = getToolByName(context, 'portal_moonstone')
        flat_vocab = []
        pms_vocabs = {}
        pms_vocab_fields = []
        empty_columns = {}
        row = ['']
        sparse_license_category_ids = []

        def field_sort(a, b):
            return cmp(a.getName(), b.getName())

        sorted_fields = pms.Schema().fields()
        sorted_fields.sort(field_sort)

        for field in sorted_fields:
            if parent_filtered and not parent_fields.has_key(field):
                continue
            # xxx: I should be shot for the following line
            if not field.widget.visible: continue

            # Only KI, rep and admin may see date and string columns. This is a very artificial limit but will suffice.
            #if not context.portal_type in ('KeyIndividual','Representative','Administrative') and \
            #        not field.getName().startswith('cat'):
            #    continue

            if field.getName().startswith('cat') \
                or field.getName().startswith('string') \
                or field.getName().startswith('date') \
                or field.getName().startswith('fspstring') \
                or field.getName().startswith('fspdate'):

                license_category_ids = getattr(pms, field.accessor)() 
                if skip_empty_vocab_columns:
                    if not license_category_ids:
                        continue
                row.append(field)
                pms_vocabs[field] = license_category_ids
                pms_vocab_fields.append(field)
                empty_columns[field] = True
                for id in license_category_ids:
                    if not id in sparse_license_category_ids:
                        sparse_license_category_ids.append(id)

        # This row is the 'heading'
        rows.append(row)

        for license_category_id in sparse_license_category_ids:
            if parent_filtered and (license_category_id not in parent_license_category_ids):
                continue
            row = [{'key':license_category_id, 'value':pms.getLicenseCategoriesVocab().getValue(license_category_id)}]
            has_true_value = False
            for field in pms_vocab_fields:
                if license_category_id in pms_vocabs[field]:
                    # If there is skipping to be done then we have to fetch values
                    if skip_empty_rows or skip_empty_columns:
                        value = getattr(context, field.accessor)()
                        if skip_empty_rows and (license_category_id in value):
                            has_true_value = True
                        if skip_empty_columns and (license_category_id in value):
                            if empty_columns[field]:
                                empty_columns[field] = False        

                    # If an element is False in parent then it must not be editable
                    # in UI for context.
                    if parent_filtered and (license_category_id not in parent_fields[field]):
                        row.append(None)
                    else:
                        row.append(field)
                else:
                    row.append(None)

            if skip_empty_rows:
                if has_true_value:
                    rows.append(row)
            else:
                rows.append(row)

        # The result (rows) is row-major, so we can only remove empty columns here
        if skip_empty_columns:
            transposed_rows = zip(*rows)
            rows = [transposed_rows[0]]
            for row in transposed_rows[1:]:
                if not empty_columns[row[0]]:
                    rows.append(row)
            # Transpose back
            rows = zip(*rows)

        return rows

    def my_compliance(self):
        """
        Find the compliance instance for the FSP and redirect to it
        """
        context = aq_inner(self.context)
        serviceType = context.getServiceType()
        # The mapping is hardcoded
        id = ''
        if serviceType == '1':
            id = 'comprehensive'
        elif serviceType == '2':
            id = 'one-person'
        elif serviceType == '3':
            id = 'internal-co'
        else:
            raise "This FSP has no service type set"

        if id: 
            context.REQUEST.RESPONSE.redirect(context[id].absolute_url() + '/fsp_compliance_tree')

