
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Production', 'Quality', 'Distribution', 'Sales', 'Brand Awareness']
data = np.array([[50, 55, 60, 65], [70, 75, 80, 85], [60, 65, 70, 75], [80, 85, 90, 95], [65, 70, 75, 80]])

max_data = np.amax(data)

fig = plt.figure(figsize=(9, 7), dpi=100)
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    data_i = np.append(data[i], data[i][0])
    ax.plot(angles, data_i, label=line_labels[i], linewidth=1.5)
    ax.fill(angles, data_i, alpha=0.05)
    ax.plot(angles, (i + 1) * max_data / len(line_labels) * np.ones_like(angles), linewidth=1.5, color='black', alpha=0.2)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, max_data)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

ax.set_title("Food and Beverage Industry - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/1.png')

plt.clf()