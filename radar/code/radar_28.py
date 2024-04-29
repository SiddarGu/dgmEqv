
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Tourist Traffic (%)', 'Sightseeing Attractions (Score)', 'Hospitality (Score)', 'Shopping and Dining (Score)', 'Entertainment (Score)']
line_labels = ['Tokyo', 'Seoul', 'New York', 'Rome', 'Beijing']
data = np.array([[70, 90, 75, 80, 70], [75, 95, 80, 85, 65], [80, 85, 85, 90, 60], [85, 80, 90, 95, 55], [90, 75, 95, 95, 60]])

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
angles=np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)
data = np.concatenate((data, data[:,0:1]), axis=1)
for i in range(0, len(line_labels)):
    ax.plot(angles, data[i], 'o-', label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0))
ax.grid(True)

ax.set_thetagrids(angles[:-1]*180/np.pi, data_labels)
ax.set_rlim(0, 100)
plt.title("Tourism and Hospitality Performance - 2021")
fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/44_202312262320.png")
plt.clf()