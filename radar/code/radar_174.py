import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Hawaii Resort", "French B&B", "Bali Spa", "Canadian Ski Lodge", "Australian Outback Tour"]
data = np.array([[87, 82, 78, 75, 71],
                 [90, 85, 80, 75, 70],
                 [80, 85, 90, 95, 90],
                 [75, 80, 85, 90, 85],
                 [85, 80, 75, 70, 65]])

line_labels = ["Customer Satisfaction (Score)", "Food and Beverage Quality (Score)",
               "Room Comfort (Score)", "Location Accessibility (Score)", "Value for Money (Score)"]

fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['r', 'g', 'b', 'c', 'm']

for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

max_value = np.max(data)
ax.set_rlim(0, max_value)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles, labels, loc="upper right")

plt.title("Tourism and Hospitality Performance Comparison")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/183_202312310100.png")

plt.clf()