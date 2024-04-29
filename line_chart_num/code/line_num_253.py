
import matplotlib.pyplot as plt
import numpy as np

# set figure size and dpi
plt.figure(figsize=(9, 6), dpi=100)

# data
years = [2001, 2002, 2003, 2004]
wheat = [100, 120, 80, 150]
maize = [80, 90, 110, 120]
rice = [120, 110, 130, 140]
barley = [150, 160, 120, 80]

# draw line chart
plt.plot(years, wheat, label="Wheat Production (million tons)")
plt.plot(years, maize, label="Maize Production (million tons)")
plt.plot(years, rice, label="Rice Production (million tons)")
plt.plot(years, barley, label="Barley Production (million tons)")

# set grids
plt.grid(True, linestyle='-.')

# set x ticks
plt.xticks(np.arange(min(years), max(years)+1, 1.0))

# set title
plt.title("Global Production of Major Grains in 2001-2004")

# set legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# annotate the value of each data point
plt.annotate('Wheat 100', xy=(2001, 100), xytext=(2002, 105),
            arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate('Maize 80', xy=(2001, 80), xytext=(2002, 85),
            arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate('Rice 120', xy=(2001, 120), xytext=(2002, 125),
            arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate('Barley 150', xy=(2001, 150), xytext=(2002, 155),
            arrowprops=dict(facecolor='black', shrink=0.01))

# adjust the figure
plt.tight_layout()

# save the figure
plt.savefig("line chart/png/482.png")

# clear the current image state
plt.clf()