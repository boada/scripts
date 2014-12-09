#!/usr/bin/env python
# File: boxplot_percentile.py
# Created on: Fri Aug  9 14:43:27 2013
# Last Change: Tue Aug 13 13:25:26 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

from scipy.stats import scoreatpercentile
import warnings

class boxplotter(object):
    def __init__(self, median, top, bottom, whisk_top=None,
                 whisk_bottom=None):
        self.median = median
        self.top = top
        self.bott = bottom
        self.whisk_top = whisk_top
        self.whisk_bott = whisk_bottom
        #print whisk_top, top, median, bottom, whisk_bottom
    def draw_on(self, ax, index, box_color = "blue",
                median_color = "red", whisker_color = "black"):
        #width = .7
        width = 0.5
        w2 = width / 2

        # Quartiles and Median
        ax.broken_barh([(index - w2, width)],
                       (self.bott,self.top - self.bott),
                       facecolor="None", edgecolor=box_color, lw=2)
        ax.broken_barh([(index - w2, width)],
                       (self.median,0),
                       facecolor="None", edgecolor=median_color, lw=2)
        # Top Whisker
        if self.whisk_top is not None:
            # Cap
            ax.broken_barh([(index - w2, width)],
                           (self.whisk_top,0),
                           facecolor="white", edgecolor=whisker_color, lw=2)
            #ax.broken_barh([(index , 0)],
            #               (self.whisk_top, self.top-self.whisk_top),
            #               edgecolor=box_color,linestyle="dashed", lw=2)

        # Bottom Whisker
        if self.whisk_bott is not None:
            # Cap
            ax.broken_barh([(index - w2, width)],
                           (self.whisk_bott,0),
                           facecolor="white", edgecolor=whisker_color, lw=2)
            #ax.broken_barh([(index , 0)],
            #               (self.whisk_bott,self.bott-self.whisk_bott),
            #               edgecolor=box_color,linestyle="dashed", lw=2)

def percentile_box_plot(ax, data, indexer=None, box_top=75,
                        box_bottom=25, whisker_top=95, whisker_bottom=5):
    if indexer is None:
        indexed_data = zip(range(1,len(data)+1), data)
    elif isinstance(indexer, list):
        indexed_data = zip(indexer, data)
    else:
        indexed_data = [(indexer(datum), datum) for datum in data]
    def get_whisk(vector, w):
        if w is None:
            return None
        return scoreatpercentile(vector, w)

    for index, x in indexed_data:
        if len(x) > 0:
            print len(x)
            bp = boxplotter(scoreatpercentile(x, 50),
                        scoreatpercentile(x, box_top),
                        scoreatpercentile(x, box_bottom),
                        get_whisk(x, whisker_top),
                        get_whisk(x, whisker_bottom))
            bp.draw_on(ax, index)
        else:
            warnings.warn("Boxplot Percentile: Not enough points")


def example():

    from pylab import rand, ones, concatenate
    import matplotlib.pyplot as plt
    # EXAMPLE data code from:
    # http://matplotlib.sourceforge.net/pyplots/boxplot_demo.py
    # fake up some data
    spread= rand(50) * 100
    center = ones(25) * 50
    flier_high = rand(10) * 100 + 100
    flier_low = rand(10) * -100
    data =concatenate((spread, center, flier_high, flier_low), 0)

    # fake up some more data
    spread= rand(50) * 100
    center = ones(25) * 40
    flier_high = rand(10) * 100 + 100
    flier_low = rand(10) * -100
    d2 = concatenate( (spread, center, flier_high, flier_low), 0 )
    data.shape = (-1, 1)
    d2.shape = (-1, 1)
    #data = [data, d2, d2[::2,0]]
    data = [data, d2]

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_xlim(0,4)
    percentile_box_plot(ax, data, [2,3])
    plt.show()

if __name__ == "__main__":
    example()
