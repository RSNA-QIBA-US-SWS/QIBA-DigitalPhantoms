#!/bin/bash
#SBATCH --mem=12000
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=6
#SBATCH --exclude=moab,wasatch

FEMGIT='/home/mlp6/git/fem'
DYNADECK='qiba_elastic_pml.dyn'

date
hostname
ls-dyna-d ncpu=$SLURM_NTASKS i=$DYNADECK
rm d3*
python $FEMGIT/post/create_disp_dat.py --dat
python $FEMGIT/post/create_res_sim_mat.py --dynadeck $DYNADECK
if [ -e res_sim.mat ]; 
    then 
        rm nodout; 
        xz -v disp.dat;
fi
