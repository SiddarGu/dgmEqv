
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Consumption (GWh/year)', 'Revenue (Millions of Dollars)', 'Average of Customer Bill', 'Households']
line_labels = ['Natural Gas', 'Electricity', 'Solar', 'Wind', 'Oil', 'Nuclear']
data = np.array([
    [6450, 15590, 150, 890],
    [19800, 76000, 440, 740],
    [3100, 7800, 700, 220],
    [2120, 7000, 560, 110],
    [1000, 8000, 200, 50],
    [1220, 5600, 400, 90]
])

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels,data[:, 0], color='b', alpha=0.4, label=data_labels[0])
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0])
ax1.set_title('Energy and Utilities Consumption and Revenue Analysis')
ax1.legend(loc=1)
ax1.grid(linestyle='--')

ax2 = ax1.twinx()
ax2.set_ylabel(data_labels[1])
ax2.plot(line_labels,data[:, 1], color='g', alpha=0.8, label=data_labels[1])
ax2.legend(loc=2)

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.set_ylabel(data_labels[2])
ax3.plot(line_labels,data[:, 2], color='m', alpha=0.8, label=data_labels[2])
ax3.legend(loc=3)

ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.set_ylabel(data_labels[3])
ax4.plot(line_labels,data[:, 3], color='y', alpha=0.8, label=data_labels[3])
ax4.legend(loc=4)

ax1.xaxis.set_ticks(line_labels)
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()
ax4.autoscale_view()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/27_2023122261325.png')
plt.clf()