from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter

class ViewOptions(ViewletBase):
    render = ViewPageTemplateFile('viewoptions.pt')

    def _isType(self, type):
        return self.context.portal_type == type

    def _endsWith(self, path):
        return self.context.request.URL.endswith(path)

    def getTabs(self):

        project = self.context.restrictedTraverse('@@unep_utils').projectParentURL()
        if project:
            tabs = [
                (project, "Overview",
                    self._isType('Project') and self._endsWith('/base_view')),
                ("%s/project_general_info" % project,"General",
                    self._isType('ProjectGeneralInformation')),
                ("%s/fmi_folder" % project, "Financial",
                    self._isType('FMIFolder')),
                ("%s/milestones" % project, "Milestones",
                    self._isType('Milestone')),
                ("%s/mne_folder" % project, "Monitoring & Evaluation",
                    self._isType('MandEfolder')),
                ("%s/@@reports" % project, "Reports",
                    self._isType('Project') and self._endsWith('/@@reports')),
                ("%s/documents" % project, "Documents",
                    self._isType('Folder')),
            ]
        elif self._isType('ProjectDatabase'):
            tabs = [
                (self.context.absolute_url(), "Projects A-Z",
                    self._endsWith('/base_view')),
                ("%s/@@reports" % self.context.absolute_url(), "Reports",
                    self._endsWith('/@@reports')),
            ]
        else:
            return []

        return [dict(url=i, title=j, selected=k) for i,j,k in tabs]
