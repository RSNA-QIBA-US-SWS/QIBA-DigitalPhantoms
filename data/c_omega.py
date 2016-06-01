def calc(f, G0, GI, Beta):
    """ calculate SWS as a function of frequency

    :param f: vector of frequency (Hz)
    :param G0: G_o (Pa)
    :param GI: G_inf (Pa)
    :param Beta: exponential relaxation constant (s^-1)
    :returms: c_omega (SWS in m/s as a function of omega (rad/s)
    """

    import numpy as np

    omega = 2*np.pi*np.array(f);
    rho = 1000; # kg / m^3

    mu1 = GI;
    mu2 = G0-GI;
    eta = (G0-GI)/Beta;

    muprime = mu1 + (mu2 * omega**2 * eta**2) / (mu2**2 + omega**2 * eta**2)
    muprime2 = -(mu2**2 * omega * eta) / (mu2**2 +omega**2 * eta**2)
        
    alpha = np.sqrt(rho * omega**2 * (np.sqrt(muprime**2 + muprime2**2) - muprime) / (2 * (muprime**2 + muprime2**2)))
          
    c_omega = np.sqrt((1/rho) * (2 * (muprime**2 + muprime2**2)) / (muprime + np.sqrt(muprime**2 + muprime2**2)))

    return c_omega
