import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Number of Orders (thousands)", "Total Revenue (millions of dollars)", "Average Order Value (dollars)", "Conversion Rate"]
line_labels = ["Apparel", "Electronics", "Home Goods", "Beauty and Personal Care", "Sports and Outdoor", "Books and Media", "Automative", "Grocery and Household", "Toys and Games", "Health and Wellness"]
data = np.array([
    [350, 450, 124, 8],
    [250, 600, 240, 12],
    [300, 350, 110, 10],
    [200, 200, 100, 6],
    [150, 300, 200, 4],
    [100, 150, 150, 3],
    [50, 100, 200, 2],
    [400, 500, 125, 16],
    [200, 400, 200, 5],
    [250, 300, 120, 9]
])

fig = plt.figure(figsize=(30,20))
ax1 = fig.add_subplot(111)

colors = ['b','g', 'r', 'c']
ax = [ax1]
for i in range(1, data.shape[1]):
    ax.append(ax[0].twinx())

barWidth = 0.15
r = np.arange(len(data[:, 0]))

# Plotting the data
for i in range(data.shape[1]):
    if i == 0:
        ax[i].bar(r - barWidth/2, data[:,i],  color=colors[i], width=barWidth)
    else:
        ax[i].plot(r, data[:,i], color=colors[i])
    ax[i].set_ylabel(data_labels[i], color=colors[i])
    ax[i].tick_params(axis='y', colors=colors[i])
    ax[i].yaxis.set_major_locator(AutoLocator())
    ax[i].legend([data_labels[i]], loc='upper left')

# Final Adjustments
ax[0].set_title('Retail and E-Commerce Industry Performance Analysis')
ax[0].set_xlabel('Category')
ax[0].set_xticks(r)
ax[0].set_xticklabels(line_labels, rotation=30, ha='right')
for i in range(2, len(ax)):
    ax[i].spines['right'].set_position(('outward', (60*(i-1)) ))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/319_202312311430.png')
plt.close(fig)
