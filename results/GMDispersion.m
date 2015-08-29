function [c,alpha] = GMDispersion(Ginf,G0,beta,rho,f)
% Calculate generalized maxwell model dispersion.
%
% Bo Qiang
%

omega = 2.*pi.*f;
G1 = G0-Ginf;
eta = G1/beta;

storageGTheory = Ginf+eta.^2.*omega.^2.*G1./(G1.^2+eta.^2.*omega.^2);
lossGTheory = eta.*omega.*G1.^2./(G1.^2+eta.^2.*omega.^2);

c = sqrt(2.*(storageGTheory.^2+lossGTheory.^2)./rho./(sqrt(storageGTheory.^2+lossGTheory.^2)+storageGTheory));
alpha = 2.*pi.*f.*sqrt(rho.*(sqrt(storageGTheory.^2+lossGTheory.^2)-storageGTheory)./2./(storageGTheory.^2+lossGTheory.^2));
