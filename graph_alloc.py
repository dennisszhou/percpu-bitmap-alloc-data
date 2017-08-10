#!/usr/bin/env python

import sys

sys.path.insert(0, "/Users/dennisz/workplace/z-plot")

from zplot import *

t = table(sys.argv[1], separator=',')

canvas = pdf(sys.argv[2], dimensions=['6in','4in'])

# on the x-axis, we want categories, not numbers.  Thus, we
# determine the number of categories by checking the max
# "rownumber" (a field automatically added by zplot).  We want a
# half bar width (0.5) to the left and right of the bar locations
# so we don't overflow the drawable.
d = drawable(canvas, coord=['.75in', '.6in'], dimensions=['5in','3in'],
             xrange=[-0.5,t.getmax('rownumber')+0.5],
             yrange=[0,t.getmax(column='y_val')*1.2])

y_labels = list()

for i in range(1,8):
    y_labels.append([1 * i, 1000 * i])

p = plotter()
L = legend()
barargs = {'drawable':d, 'table':t, 'xfield':'rownumber',
                   'linewidth':0, 'fill':True, 'barwidth':0.8,
                              'legend':L, 'stackfields':[]}

barargs['yfield'] = 'y_val'
barargs['legendtext'] = 'area map'
barargs['fillcolor'] = 'darkgray'
p.verticalbars(**barargs)

barargs['yfield'] = 'y_val'
barargs['legendtext'] = 'bitmap'
barargs['fillcolor'] = ''
barargs['fillcolorcol'] = 'color'
p.verticalbars(**barargs)

axis(d, title='Allocation Time for 1M Objects',
        titleshift=[0,-7], titlesize=12,
        xtitle='Object Size',
        xmanual=t.query(select='x_val,rownumber'),
        ytitle='Time Taken (s)',ytitleshift=[-5,0],
        ymanual=y_labels,
        yauto=[0,t.getmax(column='y_val')*1.1,3000])

# we want legend entries to be all on one line.  Thus, we use
# skipnext=1 to get one row.  We specify the horizontal space
# between legend symbols (not considering text) with skipspace.
L.draw(canvas, coord=[d.left()+30, d.top()-20], skipspace=40)
  
canvas.render()
