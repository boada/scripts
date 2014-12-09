import pylab as pl

  #  DESCRIPTION:
  #  
  #    This script takes in a 2D array and a
  #    corresponding column (optional) and
  #    returns the array sorted by the values
  #    stored in that column. It defaults to
  #    the first column if not specified.
  #
  #  EXAMPLE:
  #
  #    >>> array1 = [ [ 7, 4, 9 ],
  #                   [ 6, 5, 2 ],
  #                   [ 1, 3, 8 ] ]
  #
  #    >>> array2 = colsort( array1 , 2 )
  #    >>> print array2
  #        [ [ 1, 3, 8 ],
  #          [ 7, 4, 9 ],
  #          [ 6, 5, 2 ] ]
  #
  #
  #  Written by A. Tomczak --- Aug 11, 2011

def colsort( arr , col=1 ):

  #  First, take care of 1D arrays
    try: l=len(arr[0])
    except: return pl.sort(arr)

  #  This line forces the data structure of the
  #  array to be a "list" (if you're curious see
  #  the Python documentation about lists)...
  #  ... yes, this is necessary
    arr = [ i for i in arr ]


  #  This loop performs an insertion-sort using
  #  the values in the specified column.
    i=0
    while i < len(arr)-1:
        if arr[i+1][col-1]<arr[i][col-1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            if i>0: i-=2
        i+=1

    return arr
    #return pl.array(arr)

