
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Number of Trees Planted (Millions)', 'Amount of Waste Reduced (Tons)', 'CO2 Emission Reduced (Tons)']
line_labels = ['Renewable Energy', 'Recycling', 'Reforestation', 'Energy Efficiency', 'Water Conservation', 'Sustainable Agriculture', 'Environmental Education', 'Carbon Capture']
data = np.array([[14, 760, 1890], [21, 580, 1430], [25, 1000, 2250], [18, 700, 1680], [29, 1220, 2820], [25, 950, 2300], [30, 650, 1550], [20, 1050, 2400]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:, 0], width=0.2, color='tab:blue', alpha=0.8)
ax1.set_ylabel(data_labels[0], color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], '-r', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='red')
ax2.tick_params(axis='y', labelcolor='red')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], '-g', label=data_labels[2])
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_ylabel(data_labels[2], color='green')
ax3.tick_params(axis='y', labelcolor='green')

ax1.set_xlabel('Category')
ax1.set_title('Environmental Sustainability Progress Overview')
ax1.set_xticklabels(line_labels, rotation=45, ha="right", wrap=True)

ax1.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()

ax1.legend(data_labels[0], loc='upper left')
ax2.legend(data_labels[1], loc='upper center')
ax3.legend(data_labels[2], loc='upper right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/24_2023122261325.png')
plt.clf()