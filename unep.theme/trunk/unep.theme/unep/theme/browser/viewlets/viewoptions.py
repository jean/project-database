from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter

class ViewOptions(ViewletBase):
    render = ViewPageTemplateFile('viewoptions.pt')

