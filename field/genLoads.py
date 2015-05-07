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
FD = [0.070, 0.050, 0.030]  # done in reverse order for normalization case to
                            # be generated first
alpha = [0.45]

root = '/getlab/mlp6/scratch/QIBA-DigitalPhantoms/field'

SLURM_TEMPLATE = 'genLoads.sh'

for i in range(len(Freq)):
    for j in range(len(Fnum)):
        for k in range(len(FD)):
            for l in range(len(alpha)):
                datafile = '%s/dyna-I-f%.2f-F%.1f-FD%.3f-a%.2f.mat' % \
                           (root, Freq[i], Fnum[j], FD[k], alpha[l])
                if not os.path.exists(datafile):
                    SLURM_FILENAME = datafile.replace('dyna-I-', 'field_')
                    SLURM_FILENAME = SLURM_FILENAME.replace('.mat', '.sh')
                    print SLURM_FILENAME
                    shutil.copy(SLURM_TEMPLATE, SLURM_FILENAME)
                    PARAM_STRING = '%.1f, %.3f, %.2f, %.2f' % \
                                   (Fnum[j], FD[k], Freq[i], alpha[l])
                    os.system('sed -i -e "s/PARAM_STRING/%s/" %s' %
                              (PARAM_STRING, SLURM_FILENAME))
                    os.system('sbatch %s' % (SLURM_FILENAME))
                else:
                    print('%s ALREADY EXISTS!!' % datafile)
