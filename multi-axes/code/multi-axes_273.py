import matplotlib.pyplot as plt
import numpy as np

# Transformed the data into three variables
data_labels = ["Amount of Recycled Waste (in tons)", "Energy Saved (in Gigajoules)", "CO2 Emission Reduced (in tons)", "Water Saved (in cubic meters)"]
line_labels = ["2015", "2016", "2017", "2018", "2019", "2020"]
data = np.array([
    [210000,36000,40000,300000],
    [230000,38000,41000,310000],
    [260000,41000,47000,340000],
    [280000,45000,51000,350000],
    [310000,48000,55000,390000],
    [350000,52000,61000,450000]
])

# Create a figure
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.bar(line_labels, data[:,2], color='r', label=data_labels[2], alpha=0.5)
ax3.set_ylabel(data_labels[2], color='r')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
ax4.fill_between(line_labels, 0, data[:,3], color='c', alpha=0.3, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='c')

fig.suptitle("Annual Environmental Sustainability Metrics: Waste Recycling, Energy and Water Savings")

ax1.grid(True)

# Set automatic y-axis locator
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())
ax4.yaxis.set_major_locator(plt.AutoLocator())

# Showing legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower left')
ax4.legend(loc='lower right')

fig.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/120_202312310108.png')
plt.clf()
