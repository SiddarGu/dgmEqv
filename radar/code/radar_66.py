import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"]
line_labels = ["User Engagement (%)", "Ad Revenue ($M)", "Daily Active Users (Millions)", "Content Quality (Score)", "Security Measures (Score)"]
data = np.array([[85, 80, 75, 70, 85], [90, 85, 82, 95, 105], [150, 120, 100, 50, 200], [80, 90, 85, 75, 85], [75, 70, 80, 85, 90]])

figure = plt.figure()
ax = figure.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)
colors = ['r', 'g', 'b', 'c', 'm']

for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], linewidth=2, label=line_labels[i])
    ax.fill(angles, row, facecolor=colors[i], alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12, rotation=0, wrap=True)
ax.spines["polar"].set_visible(False)
ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="best")

ax.set_rlim(0, np.max(data) * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

plt.tight_layout()
plt.title("Social Media Platforms Performance Analysis")

plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/66_202312302350.png")
plt.clf()