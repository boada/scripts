#!/usr/bin/env python
# File: mk_donutplot.py
# Created on: Wed 16 Jan 2013 10:00:32 AM CST
# Last Change: Thu Jan 17 15:17:07 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

from numpy import pi
import matplotlib.cm as cm

def donutplot(ax, percentages, colors, theta=0., bottom=2.):
    """ Makes a donut type pie chart instead of the more traditional pie chart.

    @type ax: Matplotlib figure axis
    @param ax: The working figure axis
    @type percentages: list or tuple
    @param percentages: the fractions for the pie parts
    @type colors: list or tuple
    @param colors: the colors of the pie parts
    @type theta: float
    @param theta: the starting theta, 0 - 2pi
    @type bottom: float
    @param bottom: Optional, gives the ability to create multi-level plots

    """

    if not len(percentages) == len(colors):
        raise Exception, 'percentages and colors must be same length'
    radii = 1.;
    # make the fractions
    for percent, color in zip(percentages, colors):
        width = 2.*pi*percent
        bar = ax.bar(theta, radii, width=width, bottom=bottom, fc=color)
        theta += width

