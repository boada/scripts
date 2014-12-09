#!/usr/bin/python
def mk_magnitude(flux,unit,band='V'):
    import math
    try:
        if unit == 'uJy':
            return  23.9-2.5*math.log10(flux)
        elif unit == 'nJy':
            return 31.4-2.5*math.log10(flux)
        elif unit == 'ADU':
            if band == 'B':
                zpt = 25.09
            elif band == 'V':
                zpt = 25.97
            elif band == 'I':
                zpt = 24.94
            elif band == 'Z':
                zpt = 24.38
            elif band == 'Y':
                zpt = 26.27
            elif band == 'J':
                zpt = 26.25
            elif band == 'H':
                zpt = 25.96
            else:
                print "You must specify a band either B, V, I, Z, Y, J, or H."
                return 1

            return zpt -2.5*math.log10(flux)
        else:
            print "You must specify units either 'uJy', 'nJy', or 'ADU'"
            return 1
    except:
        print "The maginute could not be calculated."
        print "This is probably because your flux is"
        print "less than or equal to zero. Try again."
        return 1

