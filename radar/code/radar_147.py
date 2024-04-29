import numpy as np
import matplotlib.pyplot as plt


data = np.array([[40, 45, 50, 55, 60],
                 [30, 35, 40, 45, 50],
                 [60, 65, 70, 75, 80],
                 [70, 75, 80, 85, 90],
                 [20, 25, 30, 35, 40]])
data_labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
line_labels = ['Debt Ratio (%)', 'Liquidity Ratio (%)', 'Efficiency Ratio (%)', 'Profitability Ratio (%)', 'Market Share (%)']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i, row in enumerate(data):
    ax.plot(angles, row, marker='o', label=line_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

ax.set_title('Financial Health Evaluation - Q1-Q5 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/131_202312302350.png')
plt.close(fig)