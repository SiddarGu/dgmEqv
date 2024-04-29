import numpy as np
import matplotlib.pyplot as plt

data = np.array([[75, 85, 90, 95, 80, 70],
                 [80, 90, 60, 50, 70, 80],
                 [65, 95, 85, 70, 60, 55],
                 [70, 90, 75, 60, 65, 85],
                 [60, 70, 95, 85, 80, 90]])

data_labels = ["Online", "Physical In Store", "E-commerce Platform", "Marketplace", "Dropshipping", "Personal Shopping"]
line_labels = ["Electronics", "Clothing", "Groceries", "Furniture", "Books"]

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], linewidth=2, label=line_label)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.xaxis.set_tick_params(pad=10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(0.9, 0.9))

plt.title("Product Sales in Different Channels - Retail and E-commerce")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/185_202312310100.png")
plt.clf()