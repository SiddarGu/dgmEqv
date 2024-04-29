
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Delivery Time (Days)', 'Cost Efficiency (%)', 'Customer Satisfaction (%)', 'Fleet Management (Score)', 'Logistics Efficiency (Score)']
data = [[2, 3, 4, 5], [65, 70, 75, 80], [60, 65, 70, 75], [75, 80, 85, 90], [80, 85, 90, 95]]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i, line in enumerate(data):
    line.append(line[0])
    ax.plot(angles, line, 'o-', linewidth=2, label=line_labels[i])
    ax.fill(angles, line, alpha=0.25)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data)+5)
handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.4, 1.1))
plt.title('Transportation & Logistics - 2021', va='bottom', fontsize=16)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/10_202312262150.png')
plt.clf()