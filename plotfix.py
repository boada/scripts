#!/usr/bin/env python
# File: plotfix.py
# Created on: Thu Sep 13 15:04:30 2012
# Last Change: Thu Sep 13 15:10:41 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada
def plotfix(axes):
    """
    this function makes the axis lines and ticks thicker, for publication
    quality images
    required inputs:
            axes: an instance of pyplot.plot.axes
    returns:
            axes: with thicker lines and thicker labels
    """
    fontsize     = 14
    marker_width = 2
    for tick in axes.xaxis.get_major_ticks():
        tick.label1.set_fontsize( fontsize )
        tick.label1.set_fontweight('bold')
    for tick in axes.yaxis.get_major_ticks():
        tick.label1.set_fontsize( fontsize )
        tick.label1.set_fontweight('bold')
    for line in axes.xaxis.get_ticklines():
        line.set_markeredgewidth( marker_width )
    for line in axes.yaxis.get_ticklines():
        line.set_markeredgewidth( marker_width )
    return axes
