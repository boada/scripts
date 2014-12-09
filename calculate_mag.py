#!/usr/bin/python

# Copyright (C) 2011  Steven Boada

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def calculate_mag(spectrum, bandpass, a, z, zero_point = -48.6):
    ''' This script returns a magnitude in the provided bandpass of the
    given spectrum.

    Make sure that wavelength units are the same for both inputs.
    flux units must be:     FLUX / Angstrom

    zero_point = -48.6 assumes the the FLUX units above are:  erg / cm**2 / s

    Inputs may either be the names of text files or arrays in the following
    format...
    Spectrum             Bandpass
    [ [lam1 , flux1]    ,  [ [lam1 , trans1]
    [lam2 , flux2]    ,    [lam2 , trans2]
    [lam3 , flux3]    ,    [lam2 , trans3]
        .....                  .....
    [lamX , fluxX] ]  ,    [lamY , transY] ]

    TIPS: If you would like to feed this a script a python tuple you can
    up-convert it to a numpy array.
    '''
    import math
    from scipy import interpolate
    from scipy.integrate import simps
    #from lumdist import LumDist
    import numpy as np
    M1 = 0.3
    L1 = 0.7
    K1 = 1.0 - M1 - L1

    if isinstance(spectrum, type('string')):
        spectrum = np.loadtxt(spectrum)
    if isinstance(bandpass, type('string')):
        bandpass = np.loadtxt(bandpass)

    # convert to ergs/s * cm^-2 * hz^-1
    #spectrum[:,a] = ((1.0+z)*spectrum[:,a])/(4.0*math.pi*LumDist(M1,L1,K1,z)**2)
    spectrum[:,a] = spectrum[:,a] * (spectrum[:,0]**2/3.0e18)
    spectrum[:,0] = spectrum[:,0]*(1.0+z)

    # interp to same spacing
    #bandpass_interp = np.interp(spectrum[:,0],bandpass[:,0],bandpass[:,1])
    interp = interpolate.interp1d(bandpass[:,0], bandpass[:,1],
        bounds_error=False, fill_value=0.0)
    bandpass_interp = interp(spectrum[:,0])
    #interp = interpolate.Rbf(bandpass[:,0],bandpass[:,1],function='linear')
    #bandpass_interp = interp(spectrum[:,0])
    #print z, "interp done"

    nu = []
    num_integrand = []
    denom_integrand = []

    for i in range(len(bandpass_interp)):
        nu.append(3.0e18/spectrum[i][0])
        num_integrand.append(spectrum[i][a]*bandpass_interp[i]/nu[i])
        denom_integrand.append(bandpass_interp[i]/nu[i])

    numer = simps(num_integrand,nu)
    denom = simps(denom_integrand,nu)

    return -2.5*np.log10(numer/denom) + zero_point

