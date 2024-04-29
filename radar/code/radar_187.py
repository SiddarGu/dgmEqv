
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Mobile Apps', 'Internet Security', 'Cloud Computing', 'Automation', 'Artificial Intelligence']
data = [[80, 85, 90, 95], [75, 80, 85, 90], [90, 95, 100, 105], [85, 90, 95, 100], [70, 75, 80, 85]]

max_data = max(max(i) for i in data)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i,row in enumerate(data):
    row = np.append(row, row[0])
    ax.plot(angles, [(i+1) * 20]*len(row), 'k--', c='grey', linewidth=2.5, label=None)
    ax.plot(angles, row, 'o-', c=plt.cm.Dark2(i/len(data)), linewidth=2.5, label=line_labels[i])
    ax.fill(angles, row, facecolor=plt.cm.Dark2(i/len(data)), alpha=0.25)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, max_data)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

plt.title('Technology and Internet Trends - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/11.png')
plt.clf()