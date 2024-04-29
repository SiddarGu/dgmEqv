
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Fruit Production','Vegetables Production','Animal Production','Grain Production']
line_labels = ['Canada', 'USA', 'Mexico', 'France', 'Germany']
data = np.array([[90, 95, 80, 85],
                 [85, 90, 75, 80],
                 [80, 85, 70, 75],
                 [75, 80, 65, 70],
                 [70, 75, 60, 65]])

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data))

for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], 'o-', linewidth=1, label=line_label)
    ax.fill(angles, data[i], alpha=0.25)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(0.1, 0.1))
ax.set_title('Global Agriculture and Food Production - 2021', va='bottom', fontsize=12)

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/26_202312262320.png')

plt.clf()