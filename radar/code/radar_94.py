import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Residential", "Commercial", "Industrial", "Rural", "Farmland"]
data = np.array([[250, 300, 275, 220, 180],
                [100, 80, 60, 40, 20],
                [30, 50, 40, 20, 10],
                [80, 85, 90, 95, 75],
                [10, 12, 11, 9, 8]])

line_labels = ["Average Price (thousands)", "Sales Volume (units)", "Market Growth (%)",
               "Housing Demand (%)", "Return on Investment (%)"]

fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['r', 'g', 'b', 'm', 'c']

for i in range(len(data)):
    ax.plot(angles, data[i], color=colors[i], marker='o', label=line_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)

ax.set_yticklabels([])

max_data = np.max(data)
ax.set_ylim(0, max_data)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

plt.title("Real Estate and Housing Market Overview")

plt.tight_layout()

plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/196_202312310100.png")

plt.close()