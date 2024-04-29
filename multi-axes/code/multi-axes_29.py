
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Criminal Cases', 'Civil Cases', 'Arbitration Cases', 'Administrative Cases']
line_labels = ['Property', 'Contracts', 'Torts', 'Employment', 'Immigration', 'Taxation', 'Environmental', 'Intellectual Property', 'Consumer Protection']
data = np.array([[54351, 100000, 7500, 3200], [50000, 80000, 5000, 4000], [40000, 60000, 6000, 4000], [30000, 50000, 3000, 2000], [25000, 40000, 6000, 3000], [20000, 30000, 4500, 1000], [41000, 90000, 7000, 5000], [12000, 40000, 3000, 1000], [28000, 35000, 2000, 2000]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

x = np.arange(len(line_labels))
width = 0.2

ax1.bar(x-width*1.5, data[:,0], width, label=data_labels[0], color='b')
ax2 = ax1.twinx()
ax2.bar(x-width*0.5, data[:,1], width, label=data_labels[1], color='g')
ax3 = ax1.twinx()
ax3.bar(x+width*0.5, data[:,2], width, label=data_labels[2], color='r')
ax4 = ax1.twinx()
ax4.bar(x+width*1.5, data[:,3], width, label=data_labels[3], color='y')

ax1.set_xlabel('Categories')
ax1.set_xticks(x)
ax1.set_xticklabels(line_labels, rotation=20, wrap=True)
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='r')
ax4.set_ylabel(data_labels[3], color='y')

ax4.spines['right'].set_position(('outward', 120))
ax3.spines['right'].set_position(('outward', 60))

ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='center right')

ax1.grid()
ax1.autoscale(enable=True, axis='both', tight=True)
ax2.autoscale(enable=True, axis='y', tight=True)
ax3.autoscale(enable=True, axis='y', tight=True)
ax4.autoscale(enable=True, axis='y', tight=True)

plt.title('Legal Affairs in the US: Court Cases Overview')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/39_2023122261325.png')
plt.close()