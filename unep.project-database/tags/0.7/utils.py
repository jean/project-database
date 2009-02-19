from Products.CMFCore.utils import getToolByName

def inner_strip(object):
    """
    Removes spaces from inside a string
    """
    return ''.join(str(object).split(' '))

def unep_report_format_date(context, dateObject):
    if dateObject is not None:
        return context.restrictedTraverse('@@plone').toLocalizedTime(\
                    dateObject, long_format=0)
    else:
        return ''


def getVocabularyValue(context, vocabName, selection):
    """
    get the actual value of a vocabulary item
    """
    if selection:
        atvm = getToolByName(context, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName(vocabName)
        dict = vocab.getVocabularyDict(context)
        return dict[selection][0]
    return 'No Selection'
