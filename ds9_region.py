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


def ds9_region(filename,local,size=0.5,width=1,color='green'):
    '''Writes a DS9 region file. It accepts either a single tuple
    for coordinates or a list of tuples for multiple objects. It
    CANNOT be called in succession to update a regions file.

    return code = ds9_region(filename,coords,size=0.5,width=1,color='green')

    With <filename> = string, <coords> = tuple, <size>(in arcseonds) = float
    <width> = int and <color> = string.

    '''

    import os.path

    if not isinstance(filename,str):
        print 'The filename must be a string'
        return 1

    if os.path.isfile(filename):
        print filename, 'already exists. Overwrite ([y]/n)? ',
        answer = raw_input()
        if answer == 'y' or answer == '':
            os.remove(filename)
        elif answer == 'n':
            filename = str(raw_input('Please enter a new file name: '))
        else:
            print 'try again.'
            return 1

    f = open(filename,'wt') 
    f.writelines('# Region file format: DS9 version 4.1\n')
    f.writelines('# Filename: '+filename+'\n')
    f.writelines('FK5\n')

    if isinstance(local,list):
        for i in range(len(local)):
            f.writelines('circle('+str(local[i][0])+','+str(local[i][1])+
                    ','+str(size)+'") ')
            f.writelines('# width='+str(width)+' color='+color)
            f.writelines('\n')

    else:
        f.writelines('circle('+str(local[0])+','+str(local[1])+
                        ','+str(size)+'") ')
        f.writelines('# width='+str(width)+' color='+color)
        f.writelines('\n')

    f.close()

    return 0

