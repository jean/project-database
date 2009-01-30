# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IProject(Interface):
    """Marker interface for .Project.Project
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

class IProjectDatabase(Interface):
    """Marker interface for .ProjectDatabase.ProjectDatabase
    """

class IProgrammeFramework(Interface):
    """Marker interface for .ProgrammeFramework.ProgrammeFramework
    """

##code-section FOOT
##/code-section FOOT