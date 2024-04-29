

import matplotlib.pyplot as plt
import numpy as np

# plot data
data = np.array([[2.50, 1.90], [2.00, 1.50], [0.75, 0.60], [1.20, 0.90]])

# create figure
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)

# set x ticks
ax.set_xticks([0, 1])
ax.set_xticklabels(['Monthly users(million)', 'Daily active users(million)'])

# plot bar chart
x_pos = np.arange(len(data[0]))
ax.bar(x_pos, data[0], width=0.3, bottom=0, align='center', color='#fb8072', label='Facebook')
ax.bar(x_pos, data[1], width=0.3, bottom=data[0], align='center', color='#8dd3c7', label='YouTube')
ax.bar(x_pos, data[2], width=0.3, bottom=data[0]+data[1], align='center', color='#bebada', label='Twitter')
ax.bar(x_pos, data[3], width=0.3, bottom=data[0]+data[1]+data[2], align='center', color='#80b1d3', label='Instagram')

# set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fancybox=True, shadow=True)

# set title
ax.set_title('Social media platform usage in 2021')

# prevent content from clipping
plt.tight_layout()

# save image
plt.savefig('bar chart/png/403.png')

# clear figure
plt.clf()