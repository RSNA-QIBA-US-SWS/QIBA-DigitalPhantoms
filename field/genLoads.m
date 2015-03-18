function genLoads(FNUM, FOCDEPTH, FREQ, ALPHA)
% function genLoads(FNUM, FOCDEPTH, FREQ, ALPHA)
%
% Call FEM/field Field II functions to generate ARF loads.
%
% Mark Palmeri
% mlp6@duke.edu
% 2015-03-17

nodeFile = sprintf('../mesh/nodesFoc%.fmm.dyn', FOCDEPTH*1000);

inputIntensityFile = field2dyna(nodeFile, ALPHA, FNUM, [0 0 FOCDEPTH], FREQ, ...
                                'curvlin_qiba', 'gaussian');

normIntensityFile = 'dyna-I-f3.00-F2.0-FD0.070-a0.45.mat';

makeLoadsTemps(inputIntensityFile, ...
               normIntensityFile, ...
               1000, 500, 2.0, 0.025^3, 'q', 1);
