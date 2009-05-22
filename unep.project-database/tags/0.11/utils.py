from Products.CMFCore.utils import getToolByName
from Products.Archetypes.utils import DisplayList
from DateTime import DateTime

def inner_strip(object):
    """
    Removes spaces from inside a string
    """
    return ''.join(str(object).split(' '))

def amount2millions(object):
    """
    Render an amount in millions
    """
    moneylst = str(object).split(' ')
    currency = moneylst[0]
    amount = ''.join(moneylst[1].split(','))
    amount = float(amount)
    amount = amount / 1000000.00
    return '%s%4.2f' % (currency, amount)


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
    
def getYearVocabulary(fiscal=True):
    dl = DisplayList()
    year = DateTime().year()
    startYear = year - 20
    endYear = year + 20
    while startYear < endYear:
        if fiscal:
            dl.add(str(startYear), 'FY' + str(startYear)[2:])
        else:
            dl.add(str(startYear), str(startYear))
        startYear += 1
    return dl
