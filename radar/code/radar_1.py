
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Taxation (%)', 'National Security (Score)', 'Education (Score)', 'Infrastructure (Score)', 'Healthcare (Score)']
data = np.array([[50, 55, 60, 65], [80, 85, 90, 95], [85, 80, 75, 70], [75, 80, 85, 90], [70, 65, 60, 55]])

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, 100)

for i, line in enumerate(data):
    ax.plot(angles, line, linewidth=1.5, label=line_labels[i])
    ax.fill(angles, line, alpha=0.2)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95), fontsize=10)
ax.set_title('Government Performance - 2023', va='bottom', fontsize=15)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/7_202312262300.png')
plt.clf()