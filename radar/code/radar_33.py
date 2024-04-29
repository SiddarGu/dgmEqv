
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Class 1','Class 2','Class 3','Class 4']
data = [[90,95,100,105],[85,90,95,100],[80,85,90,95],[75,80,85,90],[70,75,80,85]]
line_labels = ['Math (Score)', 'English (Score)', 'Science (Score)', 'History (Score)', 'Art (Score)']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0,110)

for line in data:
    line_val = np.append(line,line[0]) 
    ax.plot(angles, line_val, lw=2, label=line_labels)
    ax.fill(angles, line_val, alpha=0.2)

ax.grid(True)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc=(0.9, 0.95),fontsize=15)
plt.title('Academic Achievement Comparison - 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/14_202312262150.png')
plt.clf()