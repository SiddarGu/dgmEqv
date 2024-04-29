
import matplotlib.pyplot as plt
import numpy as np

# set font size and font style
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'serif'

# set figure size and aspect ratio
plt.figure(figsize=(7,5),dpi=100)
# set a subplot
ax = plt.subplot(1,1,1)
# create data
year = [2001,2002,2003,2004]
crop_yield_a = [10,12,8,15]
crop_yield_b = [8,9,11,12]
crop_yield_c = [12,11,13,14]
# set x ticks
plt.xticks(year)
# plot data
ax.plot(year, crop_yield_a, label='Crop Yield A', color='b',marker='o')
ax.plot(year, crop_yield_b, label='Crop Yield B', color='r',marker='o')
ax.plot(year, crop_yield_c, label='Crop Yield C', color='g',marker='o')
# add grid
plt.grid(linestyle='--')
# add title
plt.title('Crop yield variation in India from 2001-2004', fontsize=14)
# add legend
plt.legend(loc=2)
# add labels
for i,j in zip(year,crop_yield_a):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,crop_yield_b):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,crop_yield_c):
    ax.annotate(str(j),xy=(i,j))
# automatically resize the image
plt.tight_layout()
# save figure
plt.savefig('line chart/png/380.png')
# clear the current image state
plt.clf()