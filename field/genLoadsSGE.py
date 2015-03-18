import os

os.system('date')
os.system('hostname')

os.system("matlab -nodesktop -nosplash -r 'genLoads(PARAM_STRING)'")

os.system('qstat -j %s' % os.environ['JOB_ID'])
