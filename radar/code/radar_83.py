import numpy as np
import matplotlib.pyplot as plt

# Given data
data = np.array([[25, 80, 5, 70, 2.5],
                 [50, 60, 8, 60, 3.5],
                 [75, 50, 10, 50, 4.5],
                 [10, 30, 12, 40, 5.5],
                 [15, 90, 2, 80, 1.5]])

data_labels = ["Average Cost ($)", "Availability (%)", "Rental Yield (%)", "Demand (%)", "Mortgage Rate (%)"]
line_labels = ["Residential", "Commercial", "Industrial", "Vacation", "Agricultural"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)

ax.set_title("Analysis of Different Property Markets at Regional Level")
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rmax(np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/132_202312302350.png')
plt.close()