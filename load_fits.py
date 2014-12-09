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

def load_fits(reffile):
	'''Reads and returns a FITS data table. Call with
	data = load_fits(<file>), where <file> should be 
	a string to the desired file. '''

        if not isinstance(reffile,type('string')):
                print "The catalog filename must be a string"
                return 1

        import pyfits
        hdulist = pyfits.open(reffile)
        tbdata = hdulist[1].data

        return tbdata

