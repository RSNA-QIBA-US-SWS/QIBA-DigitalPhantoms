function genLoads(FNUM, FOCDEPTH, FREQ, ALPHA)
% function genLoads(FNUM, FOCDEPTH, FREQ, ALPHA)
%
% Call FEM/field Field II functions to generate ARF loads.
%
% Mark Palmeri
% mlp6@duke.edu
% 2015-03-19

FDmm = FOCDEPTH * 1000;

nodeFile = sprintf('../mesh/nodesFoc%.fmm.dyn', FDmm);

inputIntensityFile = field2dyna(nodeFile, ALPHA, FNUM, [0 0 FOCDEPTH], FREQ, ...
                                'curvlin_qiba', 'gaussian');

normIntensityFile = 'dyna-I-f3.00-F2.0-FD0.070-a0.45.mat';

makeLoadsTemps(inputIntensityFile, ...
               normIntensityFile, ...
               1000, 500, 2.0, 0.01^3, 'q', 1);

% generate VTU files for paraview
system(sprintf('python ~/git/fem/mesh/create_pointloads_vtk.py --nodefile ../mesh/nodesFoc%imm.dyn --loadfile PointLoads-f3.00-F%.1f-FD0.0%i-a0.45.dyn --loadout nodeLoadsFoc%immF%.1f', FDmm, FNUM, FDmm, FDmm, FNUM));

quit
