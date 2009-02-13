def inner_strip(object):
    """
    Removes spaces from inside a string
    """
    return ''.join(str(object).split(' '))

def unep_report_format_date(context, dateObject):
    return context.restrictedTraverse('@@plone').toLocalizedTime(\
                dateObject, long_format=0)
