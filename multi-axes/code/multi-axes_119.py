import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Transforming data
data_labels = ["Electricity Generation (Megawatts)", "Renewable Energy Production (Megawatts)", "Carbon Emissions (Metric Tons)"]
line_labels = ["Natural Gas", "Coal", "Nuclear Power", "Hydroelectric Power", "Solar Power", "Wind Power", "Geothermal Power"]
data = np.array([[5000, 1500, 5000], [3000, 100, 10000], [2000, 0, 0], [1000, 500, 0], [500, 500, 0], [1000, 1000, 0], [200, 200, 0]])

# Create figure and axis
fig = plt.figure(figsize=(24, 24))
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(np.arange(len(line_labels)), data[:, 0], alpha=0.6, color='red')
ax1.set_ylabel(data_labels[0], color='red')

# Line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'g-')
ax2.set_ylabel(data_labels[1], color='green')

# Scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='blue')
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='blue')

# Set title
plt.title('Energy Generation and Environmental Impact Analysis')

# Other setup
ax1.xaxis.set_tick_params(rotation=45)
ax1.xaxis.set_ticks_position('both')
for ax in [ax1, ax2, ax3]:
    ax.yaxis.set_major_locator(AutoLocator())
    ax.grid(True)

# Setup and show legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Save image and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/329_202312311430.png')
plt.clf()
