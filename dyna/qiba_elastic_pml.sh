#!/bin/bash
#$ -l mem_free=1G
#$ -pe smp 4 

FEMGIT='/home/mlp6/git/fem'
DYNADECK='qiba_elastic_pml.dyn'

date
hostname

ls-dyna-d ncpu=$NSLOTS i=$DYNADECK
rm d3*
python $FEMGIT/post/create_disp_dat.py --dat
python $FEMGIT/post/create_res_sim_mat.py --dynadeck $DYNADECK
if [ -e res_sim.mat ]; 
    then rm disp.dat nodout; 
fi

qstat -j $JOB_ID
