"""
qiba_elastic_pml.py - setup SGE scripts to launch sims on the cluster

Elastic digital phantoms for the QIBA industry comparison.

Mark Palmeri
mlp6@duke.edu
2015-03-18
"""

import os

YoungsModuli = [3.0, 6.0, 15.0, 30.0]  # kPa
ExcitationDurations = [167, 334]  # us, 500 and 1000 cycles @ 3 MHz
FocalDepths = [30, 50, 70]  # mm
Fnums = [2.0, 3.5]

root = '/radforce/fem/QIBA-DigitalPhantoms'
femgit = '/home/mlp6/git/fem'
indyn = 'qiba_elastic_pml.dyn'
sgeFile = 'qiba_elastic_pml.sh'

for YM in YoungsModuli:
    for FD in FocalDepths:
        for ED in ExcitationDurations:
            for FN in Fnums:

                sim_path = '%s/data/E%.1fkPa/foc%imm/F%.1f/EXCDUR_%ius/' % \
                           (root, YM, FD, FN, ED)

                if not os.path.exists(sim_path):
                    os.makedirs(sim_path)

                os.chdir(sim_path)
                print(os.getcwd())

                if not os.path.exists('res_sim.mat'):
                    print('\tres_sim.mat missing . . . running ls-dyna')
                    os.system('cp %s/dyna/%s .' % (root, indyn))
                    os.system("sed -i -e 's/YM/%.1f/' %s" %
                              (YM * 10000.0, indyn)
                              )
                    os.system("sed -i -e 's/TOFF1/%.1f/' %s" %
                              (ED, indyn)
                              )
                    os.system("sed -i -e 's/TOFF2/%.1f/' %s" %
                              (ED + 1, indyn)
                              )
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
                    os.system('cp %s/dyna/%s .' % (root, sgeFile))

                    os.system('qsub --bash %s' % (sgeFile))
                else:
                    print('res_sim.mat already exists')
