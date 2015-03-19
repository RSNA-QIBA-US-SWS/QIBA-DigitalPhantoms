# QIBA-DigitalPhantoms
RSNA QIBA Digital Phantom Studies
(http://qibawiki.rsna.org/index.php?title=Ultrasound_SWS_tech_ctte)

This repository contains the parameters and simulation configuration files used
for the digital phantom datasets that will be circulated to all of the
manufacturers.

## Curvilinear Probe Parameters
* Radius of curvature: 60 mm
* Element Height: 14 mm
* Element Pitch: 0.477 mm (0.007 mm kerf)
* Center Freq: 3.0 MHz
* Frac. Bandwidth: 100%
* Elevation Focus: 50 mm

## ARF Excitation Parameters
* Frequency: 3.0 MHz
* F/# = 2, 3.5
* 500, 1000 cycles
* Focal Depths: 30, 50, 70 mm (F/2 for all configurations)

## Acoustic Material Properties
* Attenuation: 0.45 dB/cm/MHz
* Linear

## Elastic Material Properties
* Poisson’s ratio: 0.495
* Shear modulus: [1.0, 2.0, 5.0, 10.0] kPa

## Misc. Parameters
* Displacement data in the imaging plane saved at 0.1 mm spacing every 0.1 ms.
* 15 mm of total lateral extent
* Just axial components of displacements
* Just imaging plane displacements
* MATLAB-formatted data will be shared

## Mesh Dimensions & Configurations
* ¼ symmetry
* 0.25 mm node spacing
* 10 mm elevation
* 25 mm laterally
* Focal depth + 25 mm axially
* PMLs on outer lateral/elevation faces and top/bottom

## Future Efforts
* Ultrasonic tracking configurations and realizations
* Viscoelastic material definitions

## Contributors
* Dr. Shigao Chen, Ph.D.
* Dr. Mark Palmeri, M.D., Ph.D.
* Bo Qiang, MSEE
* Dr. Matthew Urban, Ph.D.
