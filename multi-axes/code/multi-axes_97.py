import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Electricity Generation (Billion kWh)', 'Natural Gas Production (Billion Cubic Meters)', 'Coal Output (Million Metric Tons)', 'Renewable Energy Consumption (Trillion Btu)']
line_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
data = np.array([
    [1305,610,793,3000],
    [1340,615,800,3100],
    [1378,620,810,3250],
    [1420,630,820,3400],
    [1460,640,830,3550],
    [1500,650,840,3700],
    [1540,665,850,3850],
    [1580,680,860,4000],
    [1620,690,870,4150],
    [1660,700,880,4300]])

# Create figure
fig = plt.figure(figsize=(22,10))

# Create subplot
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='blue', alpha=0.7)
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color='blue')
ax1.yaxis.set_major_locator(AutoLocator())

# Plot second dataset making sure it shares the x-axis with the first dataset
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-')
ax2.set_ylabel(data_labels[1], color='red')
ax2.yaxis.set_major_locator(AutoLocator())

# Plot third dataset making sure it shares the x-axis with the first dataset
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], 'g-')
ax3.set_ylabel(data_labels[2], color='green')
ax3.spines['right'].set_position(('outward', 60))
ax3.yaxis.set_major_locator(AutoLocator())

# Plot fourth dataset making sure it shares the x-axis with the first dataset
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color = 'purple', alpha = 0.5)
ax4.set_ylabel(data_labels[3], color='purple')
ax4.spines['right'].set_position(('outward', 120))
ax4.yaxis.set_major_locator(AutoLocator())

plt.title('Energy Generation and Consumption Trends in Energy and Utilities Industry')

ax1.legend([data_labels[0]], loc='upper left') 
ax2.legend([data_labels[1]], loc='upper right') 
ax3.legend([data_labels[2]], loc='center left') 
ax4.legend([data_labels[3]], loc='center right') 

# Automatically resize the figure
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/99_2023122292141.png')

# Clear the current image state
plt.clf()
