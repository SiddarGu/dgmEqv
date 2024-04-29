
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

data_labels = ['Number of Trees Planted (Thousands)', 'CO2 Reduction (Thousands of Tonnes)', 'Number of Pollution Incidents Reported']
line_labels = ['Forest Conservation', 'Renewable Energy', 'Water Conservation', 'Recycling', 'Air Quality Monitoring', 'Waste Management', 'Environmental Education', 'Green Building', 'Chemical and Hazardous Waste Reduction']
data = np.array([[1250, 950, 20], 
                 [1800, 1600, 25], 
                 [1400, 1300, 30], 
                 [700, 1200, 50], 
                 [200, 1400, 35], 
                 [850, 1400, 40], 
                 [500, 1000, 25], 
                 [300, 1300, 50], 
                 [200, 1200, 45]])

fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='green', alpha=0.8)
ax1.set_ylabel(data_labels[0], color='green', fontsize=15)
ax1.set_xticklabels(line_labels, rotation=30, fontsize=15)
ax1.tick_params(axis='y', colors='green')
ax1.set_title("Environmental Sustainability Efforts: An Overview", fontsize=20)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], marker='s', color='blue')
ax2.set_ylabel(data_labels[1], color='blue', fontsize=15)
ax2.tick_params(axis='y', colors='blue')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward',60))
ax3.plot(line_labels, data[:,2], label=data_labels[2], marker='o', color='red', linestyle='--')
ax3.set_ylabel(data_labels[2], color='red', fontsize=15)
ax3.tick_params(axis='y', colors='red')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward',120))
ax4.fill_between(line_labels, 0, data[:,2], label=data_labels[2], color='y', alpha=0.2)
ax4.set_ylabel(data_labels[2], color='y', fontsize=15)
ax4.tick_params(axis='y', colors='y')

plt.tight_layout()

ax1.yaxis.set_major_locator(ticker.MaxNLocator(10))
ax2.yaxis.set_major_locator(ticker.MaxNLocator(10))
ax3.yaxis.set_major_locator(ticker.MaxNLocator(10))
ax4.yaxis.set_major_locator(ticker.MaxNLocator(10))

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/31_2023122261325.png')
plt.clf()