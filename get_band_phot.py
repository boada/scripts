#File: get_band_phot.py
#Created: Sun 14 Oct 2012 02:54:10 PM CDT
#Last Change: Sat Feb  2 14:40:52 2013
#Author: Steven Boada
#  This script returns a magnitude in the provided
#  bandpass of the given spectrum. Make sure that
#  wavelength units are the same for both inputs.
#
#  flux units must be:     FLUX / Angstrom
#
#  zero_point = -48.6 assumes the the FLUX units above
#                     are:  erg / cm**2 / s
#
#
#
#  Inputs may either be the names of text files
#  or arrays in the following format...
#
#        Spectrum             Bandpass
#
#  [ [lam1 , flux1]    ,  [ [lam1 , trans1]
#    [lam2 , flux2]    ,    [lam2 , trans2]
#    [lam3 , flux3]    ,    [lam2 , trans3]
#        .....                  .....
#    [lamX , fluxX] ]  ,    [lamY , transY] ]
#
#
#
#   NOTE: I originally wrote this script for wavelegths
#         in Angstroms and flux in erg/cm**2/s/Ang


def get_band_phot( spectrum , bandpass, z, a=1, zero_point=48.6 ):
    import numpy as np

    c = (3.0e18)      #  Angs / s

  #  These conditionals import text files if necessary

    if isinstance( spectrum , type('string') ): spectrum = np.loadtxt(spectrum)
    if isinstance( bandpass , type('string') ): bandpass = np.loadtxt(bandpass)

    interp_flux = np.interp(bandpass[:,0], spectrum[:,0]*(1.0+z),
        spectrum[:,a] )

    weighted_flux = []
    nu_arr = []
    weights = []

    nu_arr = c / bandpass[:,0]
    weighted_flux = interp_flux * bandpass[:,1] * bandpass[:,0]/nu_arr/nu_arr
    weights = bandpass[:,1] / nu_arr

    numer = np.trapz( weighted_flux , x=nu_arr )
    denom = np.trapz( weights , x=nu_arr)

    #return -2.5*np.log10( numer / denom ) + zero_point   # <--- "MAGNITUDE"
    return -2.5*np.log10(numer/denom/zero_point)# - zero_point   # <--- "MAGNITUDE"

