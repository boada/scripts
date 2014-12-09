def mk_fits(fits, data, columns):
    import numpy
    import pyfits as pyf
    import os.path

    ''' return_code = mk_fits(fits, data, colums).
    Creates a new FITS file with name "<fits>.fits" which contains
    <data> in columns labeled <columns>. <columns> should be an array
    of strings for the column labels corresponding to the columns in
    <data>. <data> can either be a text file or a numpy array. Table
    values should be and are stored as floats.

    '''

    if os.path.isfile(fits):
        print fits, 'already exists. Overwrite ([y]/n)? ',
        answer = raw_input()
        if answer == 'y' or answer == '':
            os.remove(fits)
        elif answer == 'n':
            fits = str(raw_input('Please enter a new file name: '))
        else:
            print 'just n or y'
            return 1

    if isinstance(data,str):
        data = numpy.loadtxt(data)
    if type(data) == numpy.ndarray:
        cols = []
        for i in range(len(columns)):
            cols.append(pyf.Column(name=columns[i],format='E',array=data[:,i]))
        cols = pyf.ColDefs(cols)
        tbhdu = pyf.new_table(cols)
        tbhdu.writeto(fits)
    else:
        print '<data> type not recognized'
        return 1
    return 0

if __name__ == '__main__':
    mk_fits()
