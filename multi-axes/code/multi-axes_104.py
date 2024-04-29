import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

#prepare the data
data_labels = ["Deforestation Rate (Hectares)", "Carbon Emission (Metric Tons)", "Renewable Energy Production (GWh)", "Waste Generation (Tonnes)"]
line_labels = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
data = np.array([
    [5000,6500,430,4900],
    [4500,6700,480,5100],
    [4200,6900,510,5500],
    [4000,7100,560,5700],
    [3700,7000,610,5900],
    [3500,7200,670,6100],
    [3300,7300,720,6300],
    [3000,7400,810,6500],
    [2700,7200,870,6700],
    [2400,7000,930,6900],
    [2100,6800,980,7100]
])

#create figure and setup axes
fig = plt.figure(figsize=(25,15))
ax1 = fig.add_subplot(111)

#first plot
ax1.plot(line_labels, data[:,0], linewidth=2.0)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')
ax1.set_title('Environmental Sustainability Metrics: 2010-2020')

#second plot
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], linewidth=2.0)
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('green')

#third plot, scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='red')
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('red')

#clear x-axis and show the new spine of ax3
ax3.spines['right'].set_position(('outward', 60))
ax3.set_frame_on(False)
ax3.patch.set_visible(False)
for sp in ax3.spines.values():
    sp.set_visible(False)
ax3.spines['right'].set_visible(True)

#fourth plot
ax4 = ax1.twinx()
ax4.fill_between(line_labels, 0, data[:,3], color='orange', alpha=0.5)
ax4.set_ylabel(data_labels[3])
ax4.yaxis.label.set_color('orange')
ax4.spines['right'].set_position(('outward', 120))

#set Autolocator for all ax
for ax in [ax1, ax2, ax3, ax4]:
    ax.yaxis.set_major_locator(AutoLocator())

#set legends
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='lower left')
ax3.legend([data_labels[2]], loc='upper right')
ax4.legend([data_labels[3]], loc='lower right')

plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/73_2023122292141.png')
plt.clf()
