"""
qiba_ve_pml.py - setup SGE scripts to launch sims on the cluster

Viscoelastic digital phantoms for the QIBA industry comparison.

Mark Palmeri
mark.palmeri@duke.edu
2015-06-28
"""

import os
from math import sqrt as sqrt
import re

"""
Measured values:
    E2297-AX c(200) = 2.06 dc/df = 3.08
    E2297-BX c(200) = 2.44 dc/df = 3.72
    E2297-CX c(200) = 2.87 dc/df = 5.11

Closest match VE 3-param and associated phase velocities and phase velocity slopes:
    G_0 = 10 kPa, G_infinity = 2 kPa, beta = 6666.7 1/s, c(200) = 1.91, dc/df = 3.05
    G_0 = 15 kPa, G_infinity = 4 kPa, beta = 5500.0 1/s, c(200) = 2.49, dc/df = 3.49
    G_0 = 20 kPa, G_infinity = 4 kPa, beta = 4000.0 1/s, c(200) = 2.91, dc/df = 5.55
"""

# convert all of these to cgs units
VE = [{'G0': 10*1e4, 'GI': 2*1e4, 'BETA': 6666.7},
      {'G0': 15*1e4, 'GI': 4*1e4, 'BETA': 5500.0},
      {'G0': 20*1e4, 'GI': 4*1e4, 'BETA': 4000.0}
      ]

YoungsModuli = [x['G0'] * 3.0 for x in VE]  # kPa
ExcitationDurations = [167, 334]  # us, 500 and 1000 cycles @ 3 MHz
FocalDepths = [30, 50, 70]  # mm
Fnums = [2.0, 3.5]

root = '/radforce/fem/QIBA-DigitalPhantoms'
femgit = '/home/mlp6/projects/fem'
indynFile = 'qiba_ve_pml.dyn'
slurmFile = 'qiba_ve_pml.sh'

# force running all sims, regardless of res_sim.mat file existence
run_all = True

for n, YM in enumerate(YoungsModuli):
    for FD in FocalDepths:
        for ED in ExcitationDurations:
            for FN in Fnums:

                strToReplace = {
                    'YM': '%.1f' % (YM),
                    'G0': '%.1f' % (VE[n]['G0']),
                    'GI': '%.1f' % (VE[n]['GI']),
                    'BETA': '%.1f' % (VE[n]['BETA']),
                    'BULK': '%.1f' % (YM / (3 * (1 - 2 * 0.495))),
                    'TOFF1': '%.1f' % ED,
                    'TOFF2': '%.1f' % (ED + 1),
                    'TRUN': '%.1f' % (25 / sqrt(YM / (3 * 1e4)))
                }

                re_strToReplace = re.compile('|'.join(strToReplace.keys()))

                sim_path = '%s/data/G0%.1fkPa/GI%.1fkPa/BETA%.1f/foc%imm/F%.1f/EXCDUR_%ius/' % \
                           (root, VE[n]['G0']/1e4, VE[n]['GI']/1e4, VE[n]['BETA'], FD, FN, ED)

                if not os.path.exists(sim_path):
                    os.makedirs(sim_path)

                os.chdir(sim_path)
                print(os.getcwd())

                if not os.path.exists('res_sim.mat') or run_all:
                    print('\tres_sim.mat missing . . . running ls-dyna')

                    indyn = open(root + '/dyna/' + indynFile, 'r')
                    outdyn = open(indynFile, 'w')

                    for i in indyn:
                        outdyn.write(re_strToReplace.sub(lambda j: strToReplace[j.group(0)], i))

                    indyn.close()
                    outdyn.close()

                    os.system("ln -fs %s/field/PointLoads-f3.00-"
                              "F%.1f-FD0.0%i-a0.45.dyn loads.dyn" %
                              (root, FN, FD)
                              )
                    os.system("ln -fs %s/mesh/nodesFoc%imm.dyn nodes.dyn" %
                              (root, FD)
                              )
                    os.system("ln -fs %s/mesh/elemsFoc%imm_pml.dyn "
                              "elems_pml.dyn" % (root, FD)
                              )
                    os.system("ln -fs %s/mesh/bcPMLfoc%imm.dyn bc_pml.dyn" %
                              (root, FD)
                              )
                    os.system('cp %s/dyna/%s .' % (root, slurmFile))

                    os.system('sbatch %s' % slurmFile)
                else:
                    print('res_sim.mat already exists')
