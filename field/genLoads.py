"""
genLoads.py

Generate ARF excitation field for the QIBA curvilinear array for different focal
depths and attenuations.

Mark Palmeri
mlp6@duke.edu
2015-03-17
"""

import os
import shutil

# define some stuff
Freq = [3.0]
Fnum = [2.0, 3.5]
FD = [0.030, 0.050, 0.070]
alpha = [0.45]

root = '/home/mlp6/fem/field/'

SGE_TEMPLATE = 'genLoadsSGE.py'

for i in range(len(Freq)):
    for j in range(len(Fnum)):
        for k in range(len(FD)):
            for l in range(len(alpha)):
                datafile = '%s/dyna-I-f%.2f-F%.1f-FD%.3f-a%.2f.mat' % \
                           (root, Freq[i], Fnum[j], FD[k], alpha[l])
                if not os.path.exists(datafile):
                    SGE_FILENAME = datafile.replace('dyna-I-', 'field_')
                    SGE_FILENAME = SGE_FILENAME.replace('.mat', '_SGE.py')
                    shutil.copy(SGE_TEMPLATE, SGE_FILENAME)
                    os.system('qsub %s' % (SGE_FILENAME))
                else:
                    print('%s ALREADY EXISTS!!' % datafile)
