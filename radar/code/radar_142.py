
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Production Efficiency', 'Quality Control', 'Resource Management', 'Cost Reduction', 'Innovation']
data = [[90, 95, 100, 105], [80, 85, 90, 95], [75, 80, 85, 90], [65, 70, 75, 80], [80, 85, 90, 95]]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    row = np.append(row, row[0])
    ax.plot(angles, row, linewidth=2, label=line_labels[i], color=plt.cm.Set1(i))
    ax.fill(angles, row, alpha=0.25, color=plt.cm.Set1(i))
    ax.plot(angles, np.full_like(angles, (i+1) * (max(row) / len(data))), linewidth=2, linestyle='--', color='grey')

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12, rotation=45, wrap=True)
ax.set_rlim(0, (len(data) + 1) * (max(row) / len(data)))

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
legend = ax.legend(loc=(0.5, 0.8), labelspacing=1, fontsize=12)
plt.title("Manufacturing and Production Performance in 2023", fontsize=14, y=1.2)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/7.png')
plt.clf()