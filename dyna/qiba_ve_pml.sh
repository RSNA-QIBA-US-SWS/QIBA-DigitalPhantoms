#!/bin/bash
#SBATCH --mem=24000
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24

FEMGIT='/home/mlp6/projects/fem'
DYNADECK='qiba_ve_pml.dyn'

date
hostname
ls-dyna-d ncpu=$SLURM_NTASKS i=$DYNADECK
rm d3*
python $FEMGIT/post/create_disp_dat.py
python $FEMGIT/post/create_res_sim_mat.py --dynadeck $DYNADECK
if [ -e res_sim.mat ]; 
    then 
        rm nodout; 
        xz -v disp.dat;
fi
