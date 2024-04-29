

import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(10, 8))

# create data
mode = ['Ship', 'Train', 'Bus', 'Plane']
distance = [3000, 2000, 1000, 4000]
cost = [20000, 15000, 10000, 25000]

# create bar chart
ax = fig.add_subplot(111)
ax.bar(mode, distance, label='Distance(km)', width=0.4, bottom=0, color='orange')
ax.bar(mode, cost, label='Cost', width=0.4, bottom=distance, color='royalblue')

# set title
plt.title("Cost and distance of transportation modes in 2021")

# set x-axis label
plt.xlabel("Mode")

# set y-axis label
plt.ylabel("Distance(km)/Cost")

# set xticks
plt.xticks(mode, mode, rotation=45)

# add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('bar_342.png')

# clear current figure
plt.clf()