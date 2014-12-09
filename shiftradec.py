#!/usr/bin/env python
# File: shiftradec.py
# Created on: Wed Jul 18 16:23:32 2012
# Last Change: Thu Jul 19 09:17:38 2012
'''
 PURPOSE:
     Computes new ra2 and dc2 shifted from ra1 and dc2 by deltaRa, deltaDec.
     based heavily on gcirc.pro

 EXPLANATION:
     Input position is decimal degress. All computations are double precision.
     Shifts (deltaRA, deltaDec) are in arcsec.  Output ra/dec also decimal
     degrees

 CALLING SEQUENCE:
      RA2, DEC2 = shiftRaDec(RA1, DEC1, deltaRA, deltaDec)

 INPUTS:
      RA1  -- Right ascension or longitude of point 1
      DC1  -- Declination or latitude of point 1
      deltaRa -- shift from refra in arcsec
      deltaDc -- shift from refdec in arcsec

 OUTPUTS:
      RA2  -- Right ascension or longitude of point 2
      DC2  -- Declination or latitude of point 2

 PROCEDURE:
      "Haversine formula" see
      http://en.wikipedia.org/wiki/Great-circle_distance

   MODIFICATION HISTORY:
      Written in Fortran by R. Hill -- SASC Technologies -- January 3, 1986
      Translated from FORTRAN to IDL, RSH, STX, 2/6/87
      Vector arguments allowed    W. Landsman    April 1989
      Prints result if last argument not given.  RSH, RSTX, 3 Apr. 1998
      Remove ISARRAY(), V5.1 version        W. Landsman   August 2000
      Added option U=2                      W. Landsman   October 2006
      Use double precision for U=0 as advertised R. McMahon/W.L.  April, 2007
      Use havesine formula, which has less roundoff error in the
             milliarcsecond regime      W.L. Mar 2009
      Hacked by C. Papovich -- Jan, 2012
      Rewritten in Python by S. Boada -- July, 2012

'''

import math as m

def shiftRaDec(ra1, dc1, deltara, deltadc):

    d2r = m.pi/180.
    as2r = m.pi/648000.

    # Covert everything to radians
    rara1 = ra1*d2r
    dcrad1 = dc1*d2r
    shiftRArad = deltara*as2r
    shiftDCrad = deltadc*as2r

    # Do the shifting
    deldec2 = 0.0
    sindis = m.sin(shiftRArad / 2.0)
    sindelRA = sindis / m.cos(dcrad1)
    delra = 2.0*m.asin(sindelRA) / d2r

    # Make Changes
    ra2 = ra1 + delra
    dc2 = dc1  + deltadc / 3600.0

    # Return new RA/DEC
    #print ra2, dc2
    return(ra2, dc2)
