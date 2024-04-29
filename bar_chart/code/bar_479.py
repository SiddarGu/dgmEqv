
import matplotlib.pyplot as plt
import numpy as np

# set up figure
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()

# data
states = ('California','Texas','Florida','New York')
consumption = (100000,110000,90000,120000)
maximum_supply = (120000,140000,130000,150000)
minimum_supply = (80000,90000,70000,100000)

# plot data
x = np.arange(len(states))
ax.bar(x-0.2, consumption, width=0.2, label='Consumption', color='b', align='center')
ax.bar(x, maximum_supply, width=0.2, label='Maximum Supply', color='c', align='center')
ax.bar(x+0.2, minimum_supply, width=0.2, label='Minimum Supply', color='m', align='center')

# set xticks
ax.set_xticks(x)
ax.set_xticklabels(states)

# set title
ax.set_title('Energy consumption and supply in four states in 2021')

# set legend
ax.legend()

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('bar chart/png/135.png')

# clear figure
plt.clf()