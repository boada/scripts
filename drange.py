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


########################################
# Same as a 'for' loop but accepts and #
# returns floating point numbers.      #
########################################

def drange(start,stop,step):
	try:
        	r=start
        	while r<stop:
                	yield r
                	r+=step
	except:
		print "Something has happend in the drange function!"
#		return 1

