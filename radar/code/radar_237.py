import matplotlib.pyplot as plt
import numpy as np

# Parse the raw data
raw_data = 'Aspect,Q1,Q2,Q3,Q4/n Assets,70,75,80,85/n Liabilities,50,55,60,65/n Net Income,60,65,70,75/n Revenue,80,85,90,95/n Equity,65,70,75,80'
raw_data = [i.split(',') for i in raw_data.split('/n ')]
data_labels = raw_data[0][1:]
data = np.array([list(map(int, i[1:])) for i in raw_data[1:]])
line_labels = [i[0] for i in raw_data[1:]]

# Prepare for drawing
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(polar=True)

# Draw multiple lines
for idx, row in enumerate(data):
    color = plt.cm.viridis(idx / len(data))
    ax.plot(np.append(angles[:-1], angles[0]),
            np.append(row, row[0]),
            color=color,
            label=line_labels[idx])
    ax.fill(angles, np.full_like(angles, (idx+1) * max(data.flatten()) / len(data)), 
            color=color,
            alpha=0.25)
    
# Axis settings
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_ylim(0, 100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=180)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", title='Financial Health Status - 2023')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/128_2023122292141.png')
plt.clf()
