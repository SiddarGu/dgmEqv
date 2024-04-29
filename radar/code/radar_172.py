import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Wheat Farm', 'Dairy Farm', 'Vegetable Farm', 'Fruit Orchard', 'Poultry Farm']
data = np.array([[3.5, 2.8, 6.5, 5.3, 7.2],
                 [0, 4, 0, 0, 0],
                 [0, 0, 7.8, 0, 0],
                 [0, 0, 0, 6.8, 0],
                 [0, 0, 0, 0, 2.5]])

line_labels = ['Crop Yield (Tons/Acre)', 'Milk Production (Gallons/Day)', 'Vegetable Harvest (Tons/Acre)',
               'Fruit Yield (Tons/Acre)', 'Egg Production (Dozens/Day)']

# Concatenate the first column to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

for i, row in enumerate(data):
    ax.plot(angles, row, linewidth=2.2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')

plt.title('Agriculture and Food Production Statistics')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/162_202312310100.png')
plt.close(fig)