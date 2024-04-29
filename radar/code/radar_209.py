import matplotlib.pyplot as plt
import numpy as np

# Transformation of given data
data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Stock Market', 'Investment Returns', 'Business Growth', 'Profit Margin', 'Debt Ratio']
data = np.array([
    [80, 85, 90, 95],
    [78, 82, 86, 90],
    [83, 88, 93, 98],
    [80, 85, 89, 93],
    [70, 73, 76, 79]
])

num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)
max_val = np.max(data)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Iterating over each row
for i, row in enumerate(data):
    color = plt.cm.viridis(i/data.shape[0])
    row = np.append(row, row[0])  # close the loop
    ax.plot(angles, row, color=color, label=line_labels[i])
    ax.fill(angles, row, color=color, alpha=0.25)
    radius = np.full_like(angles, (i+1)*max_val/data.shape[0])
    ax.plot(angles, radius, color=color, ls='dotted')

ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)
ax.set_ylim(0, max_val)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))

plt.title('Financial Snapshot - 2023', size=20, color='blue', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/74_2023122292141.png')
plt.clf()
