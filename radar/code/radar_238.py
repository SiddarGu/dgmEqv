import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

# Given data
given_data = '''Category,Exhibition A,Exhibition B,Exhibition C,Exhibition D/n Visitor Satisfaction,80,85,90,95/n Exhibition Quality,70,75,80,85/n Accessible for Everyone,85,90,95,100/n Culture Promotion,75,80,85,90/n Ticket Price,60,65,70,75'''
given_data = given_data.replace('/n', '\n').split('\n')

# Transform data
data_labels = given_data[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in given_data[1:]]
data = [list(map(int, row.split(',')[1:])) for row in given_data[1:]]

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Generate colors
colors = plt.cm.viridis(np.linspace(0, 1, len(line_labels)))

# Plot data
max_data = max([max(row) for row in data])

for i, row in enumerate(data):
    row.append(row[0])  # Close loop
    angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
    ax.plot(angles, row, color=colors[i], label=line_labels[i])
    gridlines = ax.plot(angles, np.full_like(angles, (i+1)*max_data/len(data)), color=colors[i], linestyle="dotted")

# Customize chart
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, max_data)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", fancybox=True)

# Add title and save figure
plt.title("Arts and Culture Exhibition Evaluation", size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/106_2023122292141.png", dpi=300)
plt.clf()
