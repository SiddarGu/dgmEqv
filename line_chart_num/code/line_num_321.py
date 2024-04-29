
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# data
year = [2000, 2001, 2002, 2003, 2004]
vep = [200, 210, 220, 230, 240]
voters = [150, 160, 170, 180, 190]
turnout = [75, 76, 77, 78, 79]

# plot a line chart
ax.plot(year, vep, color='b', linestyle='-', label='Voting Eligible Population (million)')
ax.plot(year, voters, color='r', linestyle='-', label='Number of Voters (million)')
ax.plot(year, turnout, color='g', linestyle='-', label='Voter Turnout (%)')

# set x ticks to prevent interpolation
x_ticks = np.arange(2000, 2005, 1) 
plt.xticks(x_ticks)

# label the value of each data point directly on the figure
for a, b, c in zip(year, vep, voters):
    plt.annotate('VEP={}, Voters={}'.format(b, c), xy=(a, b))

# add title and legend
plt.title("Voter Turnout in the United States from 2000 to 2004")
plt.legend(loc='upper left')

# draw background grids
plt.grid(linestyle='-.')

# adjust the image size
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/56.png')

# clear the current image state
plt.clf()