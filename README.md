[![DOI](https://zenodo.org/badge/31222567.svg)](https://zenodo.org/badge/latestdoi/31222567) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# QIBA-DigitalPhantoms
RSNA QIBA wiki overview of [US SWS Digital Phantom Studies](http://qibawiki.rsna.org/index.php?title=Ultrasound_SWS_tech_ctte)

Related publication to cite: Palmeri ML, Qiang B, Chen S, Urban M. "[Guidelines for Finite-Element Modeling of Acoustic Radiation Force-Induced Shear Wave Propagation in Tissue-Mimicking Media](https://doi.org/10.1109/TUFFC.2016.2641299)," IEEE TUFFC, 64(1):78-92, 2016.

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
* Focal Depths: 30, 50, 70 mm

## Acoustic Material Properties
* Attenuation: 0.45 dB/cm/MHz
* Linear

## Elastic Material Properties
* Poisson’s ratio: 0.495
* Shear modulus: [1.0, 2.0, 5.0, 10.0] kPa
* LS-DYNA Input Deck: ```dyna/qiba_elastic_pml.dyn```
* LS-DYNA Run Script: ```dyna/qiba_elastic_pml.py```
* ABAQUS Input Files: ```abaqus/```

## Viscoelastic Material Properties
* G_0 = 10 kPa, G_infinity = 2 kPa, beta = 6666.7 Pa-s
* G_0 = 15 kPa, G_infinity = 4 kPa, beta = 5500.0 Pa-s
* G_0 = 20 kPa, G_infinity = 4 kPa, beta = 4000.0 Pa-s 
* LS-DYNA Input Deck: ```dyna/qiba_ve_pml.dyn```
* LS-DYNA Run Script: ```dyna/qiba_ve_pml.py```
* FEBio Input File: ```febio/phantom1_200Hz_case1.feb```

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

## Download Digital Phantom Data
The raw simulation data for processing is available through the Duke University
Library Digital Research Data Repository: [QIBA Ultrasound Shear Wave Speed
Digital Phantoms](https://doi.org/10.7924/r4sj1f98c)

## Contributors
* Dr. Shigao Chen, Ph.D.
* Dr. Mark Palmeri, M.D., Ph.D.
* Bo Qiang, MSEE
* Dr. Matthew Urban, Ph.D.
* Dr. Jingfeng Jiang, Ph.D.

## Funding
This work has been supported in part by RSNA QIBA, FDA contracts
HHSF223201400703P and HHSN268201300071C, and NIH grants R01DK092255 and R01
EB002132.
