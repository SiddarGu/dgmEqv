import numpy as np
import matplotlib.pyplot as plt

data_labels = ["User Satisfaction (%)", "Site Speed (Score)", "Mobile Friendliness (Score)", "SEO Performance (Score)", "Security (Score)"]
line_labels = ["Website A", "Website B", "Website C", "Website D", "Website E"]

data = np.array([[85, 82, 88, 90, 92],
                 [80, 85, 88, 83, 90],
                 [80, 85, 95, 90, 88],
                 [85, 80, 85, 90, 95],
                 [90, 88, 92, 95, 95]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker="o", linestyle="-", linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)
ax.set_ylim([0, np.max(data)])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right")

ax.set_title("Website Performance Analysis in Technology Sector")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/126_202312302350.png")
plt.clf()