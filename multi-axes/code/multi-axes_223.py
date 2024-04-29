
import matplotlib.pyplot as plt
import numpy as np

# transform data into three variables
data_labels = ['Power Usage (Gigawatts)', 'Cost (Dollars)', 'Power Generated (Megawatts)', 'Energy Efficiency']
line_labels = ['Gas', 'Oil', 'Solar', 'Wind', 'Hydroelectric', 'Nuclear', 'Renewable']
data = np.array([[238, 19050, 637, 58], [180, 9090, 737, 51], [300, 25000, 620, 72], [270, 29000, 1080, 45],
                 [320, 33000, 1420, 70], [450, 38500, 1930, 90], [1430, 45000, 3300, 67]]).T

# plot the data
plt.figure(figsize=(15, 10))
ax1 = plt.subplot(111)
ax1.set_title('Energy and Utilities: Power Generation, Cost, and Efficiency')
colors = ['r', 'g', 'pink', 'b']
for i in range(len(data_labels)):
    if i == 0:
        ax1.bar(line_labels, data[i], label=data_labels[i], color=colors[i])
        ax1.grid(True)
        ax1.legend(loc=1, bbox_to_anchor=(1, 1))
        ax1.set_xlabel('Category')
        ax1.set_ylabel(data_labels[0])
    else:
        ax2 = ax1.twinx()
        ax2.spines['right'].set_position(('axes', 1.0 + (i - 1) * 0.1))
        ax2.plot(line_labels, data[i], marker='o', linestyle='-', label=data_labels[i], color=colors[i])

        ax2.legend(loc=i + 1)
        ax2.set_ylabel(data_labels[i])
        ax2.yaxis.set_ticks_position('right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/48_2023122261325.png')
plt.close()