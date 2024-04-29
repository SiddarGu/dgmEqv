import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Define the data
data_labels = ["Audience (Millions)", "Revenue (Billion Dollars)", "Average Ticket Price (Dollars)"]
line_labels = ["Football", "Basketball", "Baseball", "Soccer", "Cricket", "Tennis", "Golf", "Boxing", "Rugby", "Ice Hockey", "Esports"]
data = np.array([[139,15,101],[108,7.4,89],[68,10.7,33],[280,4.5,25],[129,2.5,20],[45,2.1,78],[36,2.9,64],[90,3.5,55],[87,1.8,70],[65,4.8,50],[495,1.1,15]])

# Create the figure and the axes
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)

# Plot bar chart
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.7, width=0.4)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')

# Overlay line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='r')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('r')

# Overlay scatter chart
ax3 = ax2.twinx()
scatter = ax3.scatter(line_labels, data[:, 2], color='g')
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('g')
ax3.spines['right'].set_position(('outward', 70))

# Title and legends
plt.title("Comparative Analysis of Sports Entertainment: Revenue, Audience, and Average Ticket Price")
ax1.legend(["bar chart"], loc='upper left')
ax2.legend(["line chart"], loc='lower left')
ax3.legend(["scatter chart"], loc='lower right')

# AutoLocator and grid
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())
plt.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/199_202312311051.png")
plt.clf()
