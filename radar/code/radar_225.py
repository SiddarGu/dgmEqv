import matplotlib.pyplot as plt
import numpy as np

# transformation of data
data_string = '''Juice Sales (Million $),20,22,23,25,27,30
Dairy Products Sales (Million $),30,32,35,38,40,43
Alcohol Beverages Sales (Million $),40,42,45,48,50,53
Non-alcohol Beverages Sales (Million $),20,23,25,27,29,32
Bakery Products Sales (Million $),25,30,35,40,45,50
Meat Products Sales (Million $),35,37,40,43,45,48'''
data_lines = data_string.split('\n')
line_labels = [line.split(',')[0] for line in data_lines]
data = [list(map(float, line.split(',')[1:])) for line in data_lines]
data_labels = ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6']

# create radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i, row in enumerate(data):
    row.append(row[0])
    ax.plot(angles, row, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * max(max(data)) / len(data))
    ax.plot(angles, radius, color='grey', linewidth=0.5, alpha=0.5)

# set labels and limits
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)
ax.set_rlim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.4, 1.1))

# set title and savefig
plt.title('Six Months Sales in Food and Beverage Industry', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/185_2023122292141.png', dpi=300)
        
plt.clf()
