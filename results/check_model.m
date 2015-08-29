clear all
close all
clc



%% Phantom Choice
f = 100:400;
rho = 1000;
Phantom = 'C';

switch Phantom
    case 'A'
        % Phantom A
        G0 = 10e3;
        Ginf = 2e3;
        beta = 6666.7;
    case 'B'
        % Phantom B
        G0 = 15e3;
        Ginf = 4e3;
        beta = 5500;
    case 'C'
        % Phantom C
        G0 = 20e3;
        Ginf = 4e3;
        beta = 4000;
end

%%
f0 = 200;
[vmin,ind] = min(abs(f-f0));
[c,alpha] = GMDispersion(Ginf,G0,beta,rho,f);
dcdf = gradient(c,mean(diff(f)));

figure
hold on
plot(f,c)
plot(f(ind),c(ind),'ro');

f(ind)
c(ind)
dcdf(ind)*1000
