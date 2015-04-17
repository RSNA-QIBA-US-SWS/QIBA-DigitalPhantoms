function [Th, impulseResponse] = curvlin_qiba(FIELD_PARAMS);
% function [Th, impulseResponse] = curvlin_qiba(FIELD_PARAMS);
%
% Create 'Th' transducer handle and define the impulse response and fractional
% bandwidth for a typical curvilinear array used for the QIBA digital phantom
% simulations.  This works with the fem simulation tools:
% https://github.com/RSNA-QIBA-US-SWS/fem
% 
% Mark Palmeri
% mlp6@duke.edu
% 2015-03-17

disp('Transducer: Curvilinear (QIBA)');

% define element size
kerf = 0.007e-3;
pitch = 0.477e-3;
width = pitch - kerf;
height = 14e-3;

% define # of elements based on F/#
no_elements = (FIELD_PARAMS.focus(3) / FIELD_PARAMS.Fnum) / pitch;
no_elements = floor(no_elements);

% lens focus & probe curvature
Rfocus = 50.0e-3;
Rconvex = 60/1000;

% mathematically sub-dice elements to make them ~1 lambda dimensions
no_sub_y = 2 * height/width;
no_sub_x = 2;

% define the transducer handle
Th = xdc_convex_focused_array(no_elements, width, height, kerf, Rconvex, Rfocus, ...
                              no_sub_x, no_sub_y, FIELD_PARAMS.focus);

% define the center frequency & fractional bandwidth
centerFrequency = 3.0e6;
fractionalBandwidth = 1.0;

% compute and load the experimentally-measured impulse response
impulseResponse = defineImpResp(fractionalBandwidth, centerFrequency, FIELD_PARAMS);
