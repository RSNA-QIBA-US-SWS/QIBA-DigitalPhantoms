% Process FEM simulated QIBA result.
%
% Bo Qiang
% Mayo Clinic College of Medicine
% This work was supported in part by contract HHSN268201300071C and grants R01DK092255.
% Copyright 06/18/15

%% house keeping
clear all
close all
clc

%% parameters
% mayo file name parts
focus = '30';               % focus
fn = '2p0';                 % F#
mu1 = '1';                  % elastic modulus
pushT = '167';              % push duration
% duke file name parts
foc = 'foc30mm';            % focus
F = 'F2.0';                 % F#
E = 'E3.0kPa';              % young's modulus
EXCDUR = 'EXCDUR_167us';    % push duration
% last index in time for truncating data 
lastind = 250;
% time points for plot
tp = [6 21 51 101 201];
% index in depth for estimating group velocity
indz = 121;

%% generate file path for mayo and duke result
str = strcat('G',mu1,'KPA_FOCUS',focus,'_FN',fn,'_T',pushT);
sim_mayo.resultFile = ['./mayo_fem/' str '_U.mat'];
sim_duke.resultFile = ['./duke_fem/' E '/' foc '/' F '/' EXCDUR '/res_sim.mat'];

%% process result
% load data
duke = load(sim_duke.resultFile);
mayo = load(sim_mayo.resultFile);
% rescale mayo data
mayo_max = max(mayo.Uz(:));
mayo_min = min(mayo.Uz(:));
mayo.Uz = mayo.Uz(:,:,1:lastind)./(mayo_max-mayo_min);
mayo.t = mayo.t(1:lastind);
% rescale duke data
duke_max = max(duke.arfidata(:));
duke_min = min(duke.arfidata(:));
duke.arfidata = duke.arfidata./(duke_max-duke_min);
duke.t = duke.t(1:lastind);
% plot
figure(1)
set(gcf,'position',[100 100 800 750]);
for m = 1:5
    % duke result
    subplot(2,5,m);
    imagesc(duke.lat,duke.axial,duke.arfidata(:,:,tp(m)),[0 1])
    set(gca,'fontsize',14)
    title(sprintf('%4.2f ms',duke.t(tp(m)).*1000),'fontsize',14);
    % mayo result
    subplot(2,5,m+5);
    imagesc(mayo.x.*1000,mayo.z.*1000,mayo.Uz(:,:,tp(m)),[0 1])
    set(gca,'fontsize',14)
end
% group velocity duke (time of flight)
uline = squeeze(duke.arfidata(indz,:,:));
[temp,tof] = max(uline,[],2);

figure(2)
hold on
imagesc(duke.t.*1000,duke.lat,uline)
plot(duke.t(tof).*1000,duke.lat,'ko','linewidth',2)
xlabel('Time (s)','fontsize',16)
ylabel('X (mm)','fontsize',16)
set(gca,'fontsize',14)
axis tight ij
hold off

p = robustfit(duke.lat,duke.t(tof));

figure(3)
hold on
plot(duke.lat,duke.t(tof).*1000,'ko','linewidth',3);
plot(duke.lat,polyval([p(2) p(1)],duke.lat).*1000,'r','linewidth',3)
title(sprintf('%6.4f m/s',1/p(2)/1000),'fontsize',16)
xlabel('X (mm)','fontsize',16)
ylabel('TOF (ms)','fontsize',16)
set(gca,'fontsize',14)
grid on
box on
hold off

gV_duke = 1/p(2)/1000;

% group velocity mayo (time of flight)
uline = squeeze(mayo.Uz(indz,:,:));
[temp,tof] = max(uline,[],2);

figure(4)
hold on
imagesc(mayo.t.*1000,mayo.x.*1000,uline)
plot(mayo.t(tof).*1000,mayo.x.*1000,'ko','linewidth',2)
xlabel('Time (s)','fontsize',16)
ylabel('X (mm)','fontsize',16)
set(gca,'fontsize',14)
axis tight ij
hold off

p = robustfit(mayo.x,mayo.t(tof));

figure(5)
hold on
plot(mayo.x.*1000,mayo.t(tof).*1000,'ko','linewidth',3);
plot(mayo.x.*1000,polyval([p(2) p(1)],mayo.x).*1000,'r','linewidth',3)
title(sprintf('%6.4f m/s',1/p(2)),'fontsize',16)
xlabel('X (mm)','fontsize',16)
ylabel('TOF (ms)','fontsize',16)
set(gca,'fontsize',14)
grid on
box on
hold off

gV_mayo = 1/p(2);

% waveform and frequency content
% x = 5 mm
indx = 21;
nFFT = 4096;
duke_s = squeeze(duke.arfidata(indz,indx,:));
mayo_s = squeeze(mayo.Uz(indz,indx,:));
duke_S = abs(fftshift(fft(duke_s-mean(duke_s),nFFT)));
mayo_S = abs(fftshift(fft(mayo_s-mean(mayo_s),nFFT)));
dt = mean(diff(duke.t));
fs = 1/dt;
F = linspace(-fs/2,fs/2,nFFT);
figure(6)
set(gcf,'position',[100 100 1000 500])
subplot(1,2,1)
hold on
plot(duke.t.*1000,duke_s,'b','linewidth',2)
plot(mayo.t.*1000,mayo_s,'r','linewidth',2)
xlabel('Time (ms)','fontsize',16)
title('Time Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 0.8])
grid on
box on
hold off
subplot(1,2,2)
hold on
plot(F,duke_S,'b','linewidth',2)
plot(F,mayo_S,'r','linewidth',2)
xlim([0,1000])
xlabel('F (Hz)','fontsize',16);
title('Frequency Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 6])
grid on
box on
hold off
% x = 10 mm
indx = 41;
nFFT = 4096;
duke_s = squeeze(duke.arfidata(indz,indx,:));
mayo_s = squeeze(mayo.Uz(indz,indx,:));
duke_S = abs(fftshift(fft(duke_s-mean(duke_s),nFFT)));
mayo_S = abs(fftshift(fft(mayo_s-mean(mayo_s),nFFT)));
dt = mean(diff(duke.t));
fs = 1/dt;
F = linspace(-fs/2,fs/2,nFFT);
figure(7)
set(gcf,'position',[100 100 1000 500])
subplot(1,2,1)
hold on
plot(duke.t.*1000,duke_s,'b','linewidth',2)
plot(mayo.t.*1000,mayo_s,'r','linewidth',2)
xlabel('Time (ms)','fontsize',16)
title('Time Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 0.8])
grid on
box on
hold off
subplot(1,2,2)
hold on
plot(F,duke_S,'b','linewidth',2)
plot(F,mayo_S,'r','linewidth',2)
xlim([0,1000])
xlabel('F (Hz)','fontsize',16);
title('Frequency Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 6])
grid on
box on
hold off

% x = 15 mm
indx = 61;
nFFT = 4096;
duke_s = squeeze(duke.arfidata(indz,indx,:));
mayo_s = squeeze(mayo.Uz(indz,indx,:));
duke_S = abs(fftshift(fft(duke_s-mean(duke_s),nFFT)));
mayo_S = abs(fftshift(fft(mayo_s-mean(mayo_s),nFFT)));
dt = mean(diff(duke.t));
fs = 1/dt;
F = linspace(-fs/2,fs/2,nFFT);
figure(8)
set(gcf,'position',[100 100 1000 500])
subplot(1,2,1)
hold on
plot(duke.t.*1000,duke_s,'b','linewidth',2)
plot(mayo.t.*1000,mayo_s,'r','linewidth',2)
xlabel('Time (ms)','fontsize',16)
title('Time Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 0.8])
grid on
box on
hold off
subplot(1,2,2)
hold on
plot(F,duke_S,'b','linewidth',2)
plot(F,mayo_S,'r','linewidth',2)
xlim([0,1000])
xlabel('F (Hz)','fontsize',16);
title('Frequency Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 6])
grid on
box on
hold off

% x = 20 mm
indx = 81;
nFFT = 4096;
duke_s = squeeze(duke.arfidata(indz,indx,:));
mayo_s = squeeze(mayo.Uz(indz,indx,:));
duke_S = abs(fftshift(fft(duke_s-mean(duke_s),nFFT)));
mayo_S = abs(fftshift(fft(mayo_s-mean(mayo_s),nFFT)));
dt = mean(diff(duke.t));
fs = 1/dt;
F = linspace(-fs/2,fs/2,nFFT);
figure(9)
set(gcf,'position',[100 100 1000 500])
subplot(1,2,1)
hold on
plot(duke.t.*1000,duke_s,'b','linewidth',2)
plot(mayo.t.*1000,mayo_s,'r','linewidth',2)
xlabel('Time (ms)','fontsize',16)
title('Time Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 0.8])
grid on
box on
hold off
subplot(1,2,2)
hold on
plot(F,duke_S,'b','linewidth',2)
plot(F,mayo_S,'r','linewidth',2)
xlim([0,1000])
xlabel('F (Hz)','fontsize',16);
title('Frequency Domain','fontsize',16)
legend('Duke','Mayo Body Force')
set(gca,'fontsize',14)
% ylim([0 6])
grid on
box on
hold off
