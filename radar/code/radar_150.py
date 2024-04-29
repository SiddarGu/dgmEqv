
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Societal Impact', 'Environmental Impact', 'Economic Impact', 'Political Impact']
line_labels = ['Education (Score)', 'Culture (Score)', 'Health (Score)', 'Environment (Score)', 'Social Justice (Score)']
data = [[85, 90, 95, 80], [80, 85, 90, 95], [75, 80, 85, 90], [70, 75, 80, 85], [65, 70, 75, 80]]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

ax.set_rlim(0,100)

for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], label=line_labels[i], color=np.random.rand(3,))
    ax.fill(angles, data[i], alpha=0.05)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
ax.set_title('Social and Humanitarian Impact Evaluatio', va='bottom', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/10_202312262300.png')
plt.clf()