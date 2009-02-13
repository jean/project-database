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

class IMonitoringAndEvaluation(Interface):
    """Marker interface for .MonitoringAndEvaluation.MonitoringAndEvaluation
    """

class IMandEfolder(Interface):
    """Marker interface for .MandEfolder.MandEfolder
    """

##code-section FOOT
##/code-section FOOT