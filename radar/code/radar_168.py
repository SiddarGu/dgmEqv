
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1','Q2','Q3','Q4']
line_labels = ['Vaccination Rate (%)','Doctor-Patient Ratio (%)','Hospital Bed Availability (%)','Medical Equipment Quality (%)','Insurance Coverage (%)']
data = np.array([[70,75,80,85],[50,55,60,65],[60,65,70,75],[80,85,90,95],[65,70,75,80]])
data = np.concatenate((data, data[:,0:1]),axis=1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)
for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=1, linestyle='solid', label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.2)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12, rotation=0, wrap=True)
ax.set_rlim(0,100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

plt.title('Healthcare Quality Evaluation - 2021', fontsize=14)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower right')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/48_202312262320.png')
plt.clf()