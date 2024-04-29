
import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Education Quality (Score)", "Economic Development (Score)", "Gender Equality (Score)", "Cultural Diversity (Score)", "Social Wellbeing (Score)"]
line_labels = ["Country A", "Country B", "Country C", "Country D", "Country E"]
data = np.array([[90, 85, 80, 75, 70],
                 [75, 80, 85, 90, 95],
                 [80, 85, 90, 95, 95],
                 [70, 65, 60, 55, 60],
                 [65, 70, 75, 80, 85]])

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)
ax.set_rlim(0, 100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)
ax.legend(loc='best', bbox_to_anchor=(0.1, 0.1))
plt.title('Comparing Social Development Across Countries', fontsize=15)
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/41_202312262320.png')
plt.clf()