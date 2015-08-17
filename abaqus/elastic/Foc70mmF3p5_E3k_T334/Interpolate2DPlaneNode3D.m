%% interpolate 2D plane from a 3D simulation
%
% Bo Qiang

%% house keeping
clear all
close all
clc

%% parameter
parsedFile = 'Foc70mmF3p5_E3k_T334.odbparse';
x = (0:0.25:25).*1e-3;
z = (0:0.25:100).*1e-3;
nCore = 10;
variableName = 'U';
interpolatedDataFile = 'Foc70mmF3p5_E3k_T334.mat';

%% load file
fid = fopen(parsedFile);
% read header
typeSize = fread(fid,1,'int');
info.type = fread(fid,typeSize,'char=>char')';
odbFileSize = fread(fid,1,'int');
info.odbFile = fread(fid,odbFileSize,'char=>char')';
instanceSize = fread(fid,1,'int');
info.instance = fread(fid,instanceSize,'char=>char')';
nodesetSize = fread(fid,1,'int');
info.nodeset = fread(fid,nodesetSize,'char=>char')';
variableSize = fread(fid,1,'int');
info.variable = fread(fid,variableSize,'char=>char')';
stepSize = fread(fid,1,'int');
info.step = fread(fid,stepSize,'char=>char')';
precisionSize = fread(fid,1,'int');
info.precision = fread(fid,precisionSize,'char=>char')';

% read node
numberOfNode = fread(fid,1,'int');
nodeLabel = fread(fid,numberOfNode,'int');
nodeCoordinate = reshape(fread(fid,numberOfNode*3,'double'),3,numberOfNode);
% sort
[nodeLabel,ind] = sort(nodeLabel);
nodeCoordinate = nodeCoordinate(:,ind);
% read variable
numberOfFrame = fread(fid,1,'int');
frameTime = fread(fid,numberOfFrame,'double');
frameNodeLabel = reshape(fread(fid,numberOfNode*numberOfFrame,'int'),numberOfNode,numberOfFrame);
frameNodeVariable = reshape(fread(fid,3*numberOfNode*numberOfFrame,'double'),3,numberOfNode,numberOfFrame);
% sort
for m = 1:numberOfFrame
    [frameNodeLabel(:,m),ind] = sort(frameNodeLabel(:,m));
    frameNodeVariable(:,:,m) = frameNodeVariable(:,ind,m);
end
fclose(fid);

%% interpolate
nx = length(x);
nz = length(z);
nt = numberOfFrame;
[xi,zi] = meshgrid(x,z);
variableX = zeros(nz,nx,nt);
vairableY = zeros(nz,nx,nt);
vairableZ = zeros(nz,nx,nt);
try
    matlabpool close
end
% matlabpool('open','local',nCore);
xx = nodeCoordinate(1,:);
zz = nodeCoordinate(3,:);
componentX = squeeze(frameNodeVariable(1,:,:));
componentY = squeeze(frameNodeVariable(2,:,:));
componentZ = squeeze(frameNodeVariable(3,:,:));
parfor_progress(nt);
for m = 1:nt
    variableX(:,:,m) = griddata(xx,zz,componentX(:,m),xi,zi,'cubic');
    variableY(:,:,m) = griddata(xx,zz,componentY(:,m),xi,zi,'cubic');
    variableZ(:,:,m) = griddata(xx,zz,componentZ(:,m),xi,zi,'cubic');
    parfor_progress;
end
parfor_progress(0);
% matlabpool close

%% rename variables
eval([variableName 'x=variableX;'])
eval([variableName 'y=variableY;'])
eval([variableName 'z=variableZ;'])
t = frameTime;
save(interpolatedDataFile,'info','x','z','t',[variableName 'x'],[variableName 'y'],[variableName 'z']);


