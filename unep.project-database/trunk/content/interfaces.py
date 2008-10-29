# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IAgency(Interface):
    """Marker interface for .Agency.Agency
    """

class IProject(Interface):
    """Marker interface for .Project.Project
    """

class IProjectImplementation(Interface):
    """Marker interface for .ProjectImplementation.ProjectImplementation
    """

class IMilestone(Interface):
    """Marker interface for .Milestone.Milestone
    """

class IProjectGeneralInformation(Interface):
    """Marker interface for .ProjectGeneralInformation.ProjectGeneralInformation
    """

class ISubProject(Interface):
    """Marker interface for .SubProject.SubProject
    """

class IFinancials(Interface):
    """Marker interface for .Financials.Financials
    """

class IDocumentLinks(Interface):
    """Marker interface for .DocumentLinks.DocumentLinks
    """

class IProjectExecutingPartner(Interface):
    """Marker interface for .ProjectExecutingPartner.ProjectExecutingPartner
    """

class ITranched(Interface):
    """Marker interface for .Tranched.Tranched
    """

class ICoreMixin(Interface):
    """Marker interface for .CoreMixin.CoreMixin
    """

class IPhased(Interface):
    """Marker interface for .Phased.Phased
    """

class IAddOn(Interface):
    """Marker interface for .AddOn.AddOn
    """

class IBlankCoreMixin(Interface):
    """Marker interface for .BlankCoreMixin.BlankCoreMixin
    """

class IMonitoringAndEvaluation(Interface):
    """Marker interface for .MonitoringAndEvaluation.MonitoringAndEvaluation
    """

class IRatingTrackingSystem(Interface):
    """Marker interface for .RatingTrackingSystem.RatingTrackingSystem
    """

class IEvaluatorsInformation(Interface):
    """Marker interface for .EvaluatorsInformation.EvaluatorsInformation
    """

class IRTSFolder(Interface):
    """Marker interface for .RTSFolder.RTSFolder
    """

class IMilestoneFolder(Interface):
    """Marker interface for .MilestoneFolder.MilestoneFolder
    """

class IOtherProjectRatingsFolder(Interface):
    """Marker interface for .OtherProjectRatingsFolder.OtherProjectRatingsFolder
    """

class IOtherProjectRatings(Interface):
    """Marker interface for .OtherProjectRatings.OtherProjectRatings
    """

class IFMIFolder(Interface):
    """Marker interface for .FMIFolder.FMIFolder
    """

class IMOU(Interface):
    """Marker interface for .MOU.MOU
    """

class IFinancialsMixin(Interface):
    """Marker interface for .FinancialsMixin.FinancialsMixin
    """

##code-section FOOT
##/code-section FOOT