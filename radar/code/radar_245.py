import numpy as np
import matplotlib.pyplot as plt

# Transforming the provided data into three variables
data_labels = ['Critical Thinking', 'Research Skills', 'Ethical Understanding', 'Cross-Cultural Awareness', 'Creativity', 'Interdisciplinary Integration']
line_labels = ['Philosophy', 'Psychology', 'Sociology', 'Anthropology']
data = np.array([[85, 75, 80, 85, 90, 70], [80, 80, 85, 75, 85, 75], [75, 85, 90, 80, 80, 80], [90, 70, 75, 90, 95, 85]])

# Creating a figure and plotting a radar chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1, polar=True)

# Spacing the axes evenly
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Adjusting the radial limits to accommodate the maximum data
ax.set_ylim(0, np.max(data))

# Iterating over each row in the data array
for i, row in enumerate(np.around(data, decimals=2)):
    data_line = np.concatenate((row, [row[0]]))  # Closing the loop on data lines
    ax.plot(angles, data_line, label=line_labels[i])
    ax.fill(angles, data_line, alpha=0.25)
    
    # Drawing gridlines
    ax.plot(angles, np.full_like(angles, (i + 1) * np.max(data) / len(data)), color='gray', linestyle='dotted')

# Removing circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plotting the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Setting the title of the figure
ax.set_title('Comparative Analysis in Social Sciences and Humanities', size=20, color='black', y=1.1)

# Automatically resizing the image
plt.tight_layout()

# Saving the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/45_2023122292141.png')

# Clearing the current figure
plt.clf()
