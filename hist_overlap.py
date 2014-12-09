#!/usr/bin/env python
# File: hist_overlap.py
# Created on: Sun 21 Oct 2012 12:30:14 PM CDT
# Last Change: Mon Oct 22 15:59:21 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

# Calculates the histogram allowing for overlapping bins, which are given by
#
# @param a
# @param bins a sequence of pairs (left,right), limits for each bin
#
# @return hist (numpy array)
#         bin_centers (numpy array)

def hist_overlap(a, bins):
    """
    Compute the histogram of a set of data.

    Parameters
    ----------
    a : array_like
      Input data.
      bins : sequence of pairs
      It defines the bin edges (left,right), allowing for non-uniform bin widths.

    Returns
    -------
    hist : array
    The values of the histogram. See `normed` and `weights` for a
    description of the possible semantics.
    bin_centers : array of dtype float
    Return the bin centers ``(length(hist))``.

    Notes
    -----
    All but the last (righthand-most) bin is half-open.  In other words, if
    `bins` is::

    [1, 2, 3, 4]

    then the first bin is ``[1, 2)`` (including 1, but excluding 2) and the
    second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which *includes*
    4.

    Examples
    --------
    >>> myhistogram([1,2,1], bins=[(0,1),(1,1.5),(1.5,2.5),(2,3)])
    (array([0.5, 1.25, 2, 2.5]), array([0, 0, 1, 2, 3]))
    """
    import numpy as np
    bins = np.asarray(bins) # bins are 2-dimensional arrays of shape (n,2)
    if len(bins.shape) != 2 or bins.shape[1] != 2:
        raise AttributeError, 'bins must be a list/array of 2-tuples.'

    a = np.asarray(a)
    a =  a.ravel()
    n = np.zeros(len(bins), int)

    block = 65536
    for i in np.arange(0, len(a), block):
        sa = np.sort(a[i:i+block])
        n += np.r_[sa.searchsorted(bins[:-1,1], 'left'),
        sa.searchsorted(bins[-1,1], 'right')]\
         - np.r_[sa.searchsorted(bins[:-1,0], 'left'),
        sa.searchsorted(bins[-1,0], 'right')]
    return n, (bins[:,0]+bins[:,1])/2.
