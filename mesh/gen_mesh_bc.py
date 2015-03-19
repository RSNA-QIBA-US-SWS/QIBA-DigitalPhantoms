"""
gen_mesh_bc.py

Generate meshes and PML boundary conditions for QIBA digital phantoms.

Mark Palmeri
mlp6@duke.edu
2015-03-17
"""

import os

FEMGIT = '/home/mlp6/git/fem'

# all units are CGS
focalDepths = [3.0, 5.0, 7.0]
nodeSpacing = 0.025
axialExtent = 1.5  # ratio of focal depth to extent the mesh in depth

for fd in focalDepths:

    nodefile = 'nodesFoc%.fmm.dyn' % (fd*10)
    elemfile = 'elemsFoc%.fmm.dyn' % (fd*10)

    os.system('python %s/mesh/GenMesh.py '
              '--nodefile %s '
              '--elefile %s '
              '--xyz -1.0 0.0 0.0 2.5 -%.1f 0.0 '
              '--numElem 40 100 %.f' %
              (FEMGIT, nodefile, elemfile, fd*axialExtent,
               fd*axialExtent/nodeSpacing)
              )

    os.system('python %s/mesh/bc.py '
              '--pml '
              '--nodefile %s '
              '--elefile %s '
              '--bcfile bcPMLfoc%.fmm.dyn' %
              (FEMGIT, nodefile, elemfile, fd*10)
              )
