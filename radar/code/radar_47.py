
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Population Growth', 'Average Home Price', 'Home Ownership Rate', 'Rental Market Demand', 'Vacancy Rate']
line_labels = ['City A', 'City B', 'City C', 'City D']
data = np.array([[2, 4, 6, 8], [2, 4, 6, 8], [0.8, 0.9, 0.95, 1], [3, 6, 9, 12], [0.2, 0.15, 0.1, 0.05]])

angles = np.linspace(0, 2*np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, [data[0]]))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, polar=True)

for i in range(len(data[0])):
    ax.plot(angles, data[:, i], 'o-', linewidth=2, label=line_labels[i])
    ax.fill(angles, data[:, i], alpha=0.25)
    ax.set_rmax(max(data[:, i]) * 1.1)

ax.grid(True)
ax.spines['polar'].set_visible(True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.2, 1))
plt.title("Real Estate and Housing Market Trends - 2023")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/23.png")
plt.clf()