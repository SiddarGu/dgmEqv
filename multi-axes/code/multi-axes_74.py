import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Prepare the data
data_string = '2005,20913,17764,30775,28166 ' \
              '2006,21167,18192,30998,28614 ' \
              '2007,21659,18563,31541,29179 ' \
              '2008,22416,19169,32215,29851 ' \
              '2009,23099,19804,32873,30639 ' \
              '2010,23758,20461,33696,31378 ' \
              '2011,24395,21238,34387,32198 ' \
              '2012,25092,21854,35243,32954 ' \
              '2013,25872,22501,36077,33826 ' \
              '2014,26592,23268,37048,34588'

data_array = np.array([[int(i) for i in line.split(',')] for line in data_string.split(' ')])
data_labels = ['Residential Energy Consumption (Billion Btu)',
               'Commercial Energy Consumption (Billion Btu)',
               'Industrial Energy Consumption (Billion Btu)',
               'Transportation Energy Consumption (Billion Btu)']
line_labels = data_array[:, 0]
data = data_array[:, 1:]

# Create figure
fig = plt.figure(figsize=(30, 10))
ax1 = fig.add_subplot(111)
ax1.set_title('Yearly Energy Consumption in Residential, Commercial, Industrial, and Transportation sectors',fontsize=16)

# Plot the data
colors = ['blue', 'green', 'red', 'purple']
for i in range(data.shape[1]):
    ax = ax1 if i == 0 else ax1.twinx()
    ax.plot(line_labels, data[:, i], color=colors[i], linestyle='-')
    ax.set_ylabel(data_labels[i], color=colors[i],fontsize=12)
    ax.grid(True)
    ax.yaxis.set_major_locator(AutoLocator())
    if i != 0:
        ax.spines['right'].set_position(('outward', (60*(i-1))))
    ax.legend([data_labels[i]], loc=(1.03, 0.9 - (0.1 * i)))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/84_2023122292141.png')
plt.clf()
