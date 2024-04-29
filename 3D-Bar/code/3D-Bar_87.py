import matplotlib.pyplot as plt
import numpy as np


data_str = r'''
Discipline,Enrollment Rate (%),Research Funding ($M),Publication Count
Sociology,30,50,90
Psychology,40,70,120
Philosophy,20,30,70
Linguistics,35,60,100
Anthropology,25,40,85
'''

data = np.array([line.split(',') for line in data_str.strip().split('\n')])[1:, 1:].astype(np.float32)
y_values = np.array([line.split(',') for line in data_str.strip().split('\n')])[0][1:]
x_values = np.array([line.split(',') for line in data_str.strip().split('\n')])[1:, 0]

fig = plt.figure(figsize=(15, 10))
ax = plt.axes(projection="3d")

colors = ['b', 'r', 'g']

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 1, 1, data[:, i], color=colors[i%len(colors)], shade=True, alpha=0.6)

ax.set_xticks(range(len(x_values)))
ax.set_yticks(range(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Overview of Social Sciences and Humanities Disciplines')
ax.set_xlabel('Discipline')
ax.set_zlabel('Value')
ax.view_init(elev=20, azim=-65)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/136_202312302235.png')
plt.clf()
