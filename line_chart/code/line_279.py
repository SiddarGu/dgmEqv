
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(10, 6))

# create subplot
ax = plt.subplot()

# set up data
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
data1 = [50, 100, 200, 400, 700, 1200, 1800]
data2 = [10, 20, 50, 100, 200, 400, 600]
data3 = [0, 0, 10, 50, 100, 200, 400]
data4 = [0, 0, 0, 10, 50, 100, 200]

# plot data
ax.plot(year, data1, label='Facebook users (million)')
ax.plot(year, data2, label='Twitter users (million)')
ax.plot(year, data3, label='Instagram users (million)')
ax.plot(year, data4, label='Snapchat users (million)')

# add x-axis label
ax.set_xlabel('Year')

# add y-axis label
ax.set_ylabel('Users (million)')

# add title
ax.set_title('Social Media User Growth From 2010 to 2016')

# add legend
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# set ticks
ax.set_xticks(year)

# set grid
ax.grid(ls='--', lw=0.5, c='lightgray')

# adjust figure
plt.tight_layout()

# save figure
plt.savefig('line chart/png/298.png', dpi=300)

# clear state
plt.cla()