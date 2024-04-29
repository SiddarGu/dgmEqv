
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1','Q2','Q3','Q4']
line_labels = ['Arts (Score)','Humanities (Score)','Social Sciences (Score)','Language Studies (Score)','Education (Score)']
data = np.array([[85,90,95,100],[50,55,60,65],[70,75,80,85],[60,65,70,75],[80,85,90,95]])
data = np.concatenate((data, data[:, 0:1]), axis=1) 

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_title('Academic Performance Evaluation - 2021', fontsize=15)
ax.set_rlim(0, 100)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.grid(True)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/12_202312262320.png')
plt.clf()