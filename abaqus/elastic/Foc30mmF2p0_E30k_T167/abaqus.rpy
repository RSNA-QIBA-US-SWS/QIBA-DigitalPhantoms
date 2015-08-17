# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.12-1 replay file
# Internal Version: 2012_03_13-20.23.18 119612
# Run by m066760 on Mon Apr 13 16:01:02 2015
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=261.907501220703, 
    height=162.854995727539)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='Foc30mmF2p0_E30k_T167.odb')
#: Model: C:/Users/m066760/Desktop/Foc30mmF2p0_E30k_T167/Foc30mmF2p0_E30k_T167.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370871, 
    farPlane=0.56395, width=0.153762, height=0.125419, cameraPosition=(
    -0.164593, -0.301247, 0.387272), cameraUpVector=(-0.681851, 0.306788, 
    -0.664048), cameraTarget=(0.0227272, 0.00850154, 0.108771))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.415388, 
    farPlane=0.51639, width=0.172219, height=0.140474, cameraPosition=(
    -0.215966, -0.381032, 0.146419), cameraUpVector=(-0.252019, 0.451803, 
    -0.855781), cameraTarget=(0.0215525, 0.00667721, 0.103264))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.422594, 
    farPlane=0.509281, width=0.175207, height=0.142911, cameraPosition=(
    -0.0974921, -0.434048, 0.0786219), cameraUpVector=(0.148801, 0.354118, 
    -0.923287), cameraTarget=(0.0238834, 0.00563415, 0.10193))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.430282, 
    farPlane=0.502949, width=0.178395, height=0.145511, cameraPosition=(
    0.0843007, -0.447794, 0.10653), cameraUpVector=(-0.18771, 0.304075, 
    -0.933972), cameraTarget=(0.0274787, 0.0053623, 0.102482))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.410803, 
    farPlane=0.521318, width=0.170319, height=0.138924, cameraPosition=(
    0.0681013, -0.43948, 0.00613929), cameraUpVector=(-0.0506872, 0.518183, 
    -0.853767), cameraTarget=(0.0271353, 0.00553857, 0.100354))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.411574, 
    farPlane=0.520547, width=0.170639, height=0.139185, 
    viewOffsetX=0.000943622, viewOffsetY=0.0438786)
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.415212, 
    farPlane=0.51691, width=0.12634, height=0.103051, viewOffsetX=0.00670568, 
    viewOffsetY=0.0461966)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=1)
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
#: Warning: Results for the current deformed variable are not available for one or more nodes contained in the model. Deformations at such nodes are assumed to be zero.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=100)
