#!/usr/bin/env python
# File: mk_vaccine_specz_cats.py
# Created on: Tue Aug 14 22:58:22 2012
# Last Change: Wed Aug 15 02:44:47 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pidly #get idl interactivity
import os
import sys

def format_vac_to_hs(wrk_dir):
    '''
    This calls an IDL routine to repackage the VACCINE
    output into a format that we can put through the SDSS
    pipline. See mkivar.pro for an example.
    '''
    # Get into the working directory
    os.chdir(wrk_dir)
    dir_list = os.listdir('.')

    # Start an IDL session
    idl = pidly.IDL()

    # Find the wavelength solution file first
    for index, files in  enumerate(dir_list):
        if 'ptow' in files and files.endswith('.dat'):
            wl_solution = files # the wavelength solution file

    for index, files in  enumerate(dir_list):
        if files.endswith('pefsmc.fits'): #Get the file we want
            hs_out = 'hs_'+ files.rstrip('pefsmc.fits')+'.fits'
            print files, wl_solution, hs_out
            idl.pro('mkivar',str(files), str(wl_solution), str(hs_out))

    idl.close()

def get_specz(wrk_dir, filename, fibers):
    '''
    Calls the run_zfind script to find the redshifts of the
    fibers that we have chosen. Creates files called
    spZbest-<filename>
    '''
    # Get into the working directory
    os.chdir(wrk_dir)

    # Start an IDL session
    idl = pidly.IDL()

    idl.pro('run_zfind',filename,str(fibers))

    idl.close()

def find_fibers(wrk_dir,filename):
    '''
    This is the fiber selection part of the whole thing.
    Going through file by file, you select which fibers have flux in
    them by pressing k to keep the fiber. These are stored in fibers
    '''
    import numpy as np

    # Get into the working directory
    os.chdir(wrk_dir)

    # Start an IDL session
    idl = pidly.IDL()

    command = "x=cjp_page_file("+"'"+str(filename)+"'"+",xr=[3500,6000])"

    # Run the IDL command to find the fibers -- This is glitchy
    idl(command)

    fibers = np.delete(idl.x,-1)

    print 'fibers kept',fibers

    idl.close()

    get_specz(wrk_dir, filename, fibers)

if __name__ == '__main__':
    #format_vac_to_hs(sys.argv[1])
    find_fibers(sys.argv[1],sys.argv[2])
    sys.exit()


