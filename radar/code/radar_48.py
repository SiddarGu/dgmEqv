
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Q1", "Q2", "Q3", "Q4"]
line_labels = ["Business Growth (%)","Profit Margin (%)","Investment Returns (%)","Cost Management (%)","Market Share (%)"]
data = np.array([[60, 65, 70, 75],
                 [70, 75, 80, 85],
                 [60, 65, 70, 75],
                 [50, 55, 60, 65],
                 [65, 70, 75, 80]])

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)

ax.plot(angles, data[0], linewidth=1, linestyle='solid', label=line_labels[0])
ax.fill(angles, data[0], 'b', alpha=0.1)

ax.plot(angles, data[1], linewidth=1, linestyle='solid', label=line_labels[1])
ax.fill(angles, data[1], 'r', alpha=0.1)

ax.plot(angles, data[2], linewidth=1, linestyle='solid', label=line_labels[2])
ax.fill(angles, data[2], 'g', alpha=0.1)

ax.plot(angles, data[3], linewidth=1, linestyle='solid', label=line_labels[3])
ax.fill(angles, data[3], 'y', alpha=0.1)

ax.plot(angles, data[4], linewidth=1, linestyle='solid', label=line_labels[4])
ax.fill(angles, data[4], 'm', alpha=0.1)

ax.set_rlim(0,100)
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.2, 1.0))

ax.grid(True)
plt.title("Business Performance - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/39_202312262320.png')
plt.clf()