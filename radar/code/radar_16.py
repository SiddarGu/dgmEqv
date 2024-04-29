
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ["Production (KTonnes)", "Quality (Points)", "Cost (KUSD)", "Yield (KTonnes/Acre)", "Demand (KTonnes)"]
line_labels = ["Corn", "Rice", "Wheat", "Vegetables", "Fruits"]
data = np.array([[10, 9, 10, 5, 15],
                [8, 8.5, 8, 4.5, 10],
                [6, 7.5, 6, 4, 8],
                [4, 8, 4, 3.5, 5],
                [2.5, 8.5, 2.5, 3, 3.5]])

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0, np.max(data))
ax.set_title('Agriculture and Food Production - 2021', fontsize=20)

colors = ['b', 'r', 'g', 'm', 'y']
for i in range(len(data)):
    ax.plot(angles, data[i], 'o-', linewidth=2, color=colors[i], label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25, color=colors[i])

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='best', fontsize=14)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/40_202312262320.png')
plt.clf()