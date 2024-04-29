import numpy as np
import matplotlib.pyplot as plt

# given data
record = 'Subject,Quarter 1,Quarter 2,Quarter 3,Quarter 4/n Maths,72,75,78,81/n English,68,71,74,77/n Science,70,73,76,79/n Geography,65,68,71,74/n History,67,70,73,76'
record = record.replace('/n ', '\n').split('\n')

# transforming data
data_labels = record[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in record[1:]]
data = [list(map(int, row.split(',')[1:])) for row in record[1:]]

# creating figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# evenly space out the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

data = [row + [row[0]] for row in data] # making it close-loop 

colors = ['blue', 'orange', 'green', 'red', 'purple']

for i, row in enumerate(data):
    grid = np.full_like(angles, (i+1) * np.max(data) / len(data))

    ax.plot(angles, row, 'o-', label=line_labels[i], color=colors[i])

    ax.fill(angles, grid, 'lightgray', alpha=0.25)
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# set radial limits
ax.set_rlim(bottom=0, top=np.max(data))

# plot title
plt.title('Academic Progress over Quarters', size=20, color='black', y=1.1)

ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/61_2023122292141.png')
plt.clf()             
