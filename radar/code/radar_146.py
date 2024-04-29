
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Elementary', 'Middle', 'High', 'University']
line_labels = ['Math Score', 'Science Score', 'English Score', 'Social Studies Score', 'Arts Score']
data = np.array([[90, 80, 85, 95], [80, 85, 90, 95], [85, 90, 95, 100], [75, 80, 85, 90], [60, 70, 80, 90]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data)+5)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=30)

ax.grid(True)
colors = ['r', 'g', 'b', 'm', 'k']
for i in range(len(data)):
    ax.plot(angles, data[i], 'o-', linewidth=2, color=colors[i], label=line_labels[i])
ax.legend(loc='best')
plt.title('Education Achievement in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/2_202312262300.png')
plt.clf()