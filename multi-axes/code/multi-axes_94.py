import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

data_labels = ['Number of Houses Sold (Thousands)', 'Total Revenue (Millions of Dollars)',
               'Average House Price (Thousands of Dollars)', 'Houses for Rent (Thousands)']
data = np.array([[5600, 1325000, 236.6, 1500],
                 [5700, 1340000, 235.1, 1600],
                 [5900, 1380000, 233.9, 1650],
                 [6150, 1440000, 234.1, 1700],
                 [6300, 1480000, 234.9, 1800],
                 [6550, 1520000, 232.0, 1850],
                 [6700, 1560000, 232.8, 1920],
                 [6850, 1600000, 233.6, 2000],
                 [7050, 1650000, 233.9, 2100],
                 [7250, 1700000, 234.5, 2200],
                 [7500, 1750000, 233.3, 2300]])
line_labels = np.linspace(2010, 2020, num=11)

plt.figure(figsize=(20, 10))
ax1 = plt.subplot(111)

ax1.plot(line_labels, data[:, 0], label=data_labels[0], color='blue')
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color='blue')
ax1.xaxis.grid()
ax1.yaxis.grid()

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], label=data_labels[1], color='green')
ax2.set_ylabel(data_labels[1], color='green')
ax2.xaxis.grid()

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], label=data_labels[2], color='red')
ax3.set_ylabel(data_labels[2], color='red')
ax3.spines["right"].set_position(("axes", 1.1))

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], color='cyan', alpha=0.5, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='cyan')
ax4.spines["right"].set_position(("axes", 1.2))

# Automatically adjust ylim and xlim for all axes
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())
ax4.yaxis.set_minor_locator(AutoMinorLocator())

fig = plt.gcf()
fig.suptitle('Real Estate and Housing Market Trends Over a Decade')

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/152_202312310108.png')
plt.close()
