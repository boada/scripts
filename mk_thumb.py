#File: mk_thumb.py
#Created: Tue 27 Mar 2012 12:06:15 PM CDT
#Last Change: Thu May 23 14:42:08 2013
#Author: Steven Boada

import sys
import pyfits as pyf
from astLib import astImages
from astLib import astWCS

def mk_thumb(image,x_coor,y_coor,window,output='none'):

	''' This creates a small thumbnail from a much larger image.

	Inputs: the large image, the x and y coordinates(center) of
	the small window, the small window size, and the name of the
	output file.

	return = mk_thumb(image,x_coor,y_coor,window,output='none')	

	All values except the files should be floating points. 

	Returns: The clipped data from the large image. '''

	# Input checking

	if not isinstance(image,type('string')):
		print "the input file name must be a string"
		return 1
	if not isinstance(x_coor,type('float')):
		x_coor = float(x_coor)
	if not isinstance(y_coor,type('float')):
		y_coor = float(y_coor)
	if not isinstance(window,type('float')):
		if isinstance(window,type('int')):
			window = float(window)
		elif isinstance(window,type('array')):
			pass
		else:
			print "the window must either be a float or an array"
#			return 1
	if not isinstance(output,type('string')):
		print "the output file name must be a string"
		return 1

	f = pyf.open(image)
	data = f[0].data
	
	clipped = astImages.clipImageSectionPix(data,x_coor,y_coor,window)

	if not output == 'none':
		astImages.saveFITS(output,clipped)
		return 0
	else:	
		return clipped

def mk_thumb_wcs(header,data,ra,dec,window,output):

    try:
        wcs = astWCS.WCS(header,mode='pyfits')
    except:
        wcs = astWCS.WCS(header,mode='pyfits',extensionName='SCI')

    imdict = astImages.clipImageSectionWCS(data, wcs, ra, dec,
        window, returnWCS=True)
	thumb = imdict['data'] #data array
	newwcs = imdict['wcs'] #wcs info
	astImages.saveFITS(output, thumb, imageWCS=newwcs)
	return thumb

def mk_synth_thumb_wcs(header,data,ra,dec,window,output,userdata):
    try:
        wcs = astWCS.WCS(header,mode='pyfits')
    except:
        wcs = astWCS.WCS(header,mode='pyfits',extensionName='SCI')

    imdict = astImages.clipImageSectionWCS(data, wcs, ra, dec,
    window, returnWCS=True)
    #thumb = imdict['data'] #data array
    newwcs = imdict['wcs'] #wcs info
    astImages.saveFITS(output, userdata, imageWCS=newwcs)
    return userdata


if __name__ == "__main__":
	image = sys.argv[1]
	x_coor = float(sys.argv[2])
	y_coor = float(sys.argv[3])
	window = float(sys.argv[4])
	output = sys.argv[5]
	#sys.exit(mk_thumb(image,x_coor,y_coor,window,output))
	sys.exit(mk_thumb_wcs(image,x_coor,y_coor,window,output))
