import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
raw_data = 'Aspect,Museum A,Museum B,Museum C,Museum D,Museum E\n Visitor Satisfaction,78,82,85,89,92\n Exhibition Quality,80,84,88,91,95\n Cultural Significance,75,79,83,86,90\n Staff Friendliness,82,86,89,93,96\n Locational Advantage,70,74,78,82,86'
raw_data = raw_data.split('\n')

line_labels = [i.split(",")[0] for i in raw_data[1:]]
data_labels = raw_data[0].split(',')[1:]
data = [i.split(",")[1:] for i in raw_data[1:]]

# Convert data to float
data = [[float(j) for j in i] for i in data]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 10))
fig.tight_layout()

# Set polar to True
ax = fig.add_subplot(111, polar=True)

# Define angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Define color array
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))

for i, row in enumerate(data):
    row.append(row[0])  # close the loop of data lines
    ax.plot(angles, row, color=colors[i], label=line_labels[i])

    # generate radius vector
    radius = np.full_like(angles, (i+1) * max([max(i) for i in data]) / len(data))
    ax.plot(angles, radius, color=colors[i], linestyle='dashed')

# Set the gridlines and labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Set radial limits
ax.set_ylim(0, np.ceil(max([max(i) for i in data])/10)*10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Remove circular gridlines and background
ax.yaxis.grid(False)  
ax.spines['polar'].set_visible(False)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set the title
plt.title('Arts and Cultural Museums Performance Evaluation', size=20, color='black', y=1.1)

# Controls word display
plt.axis(False)

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/69_2023122292141.png', bbox_inches = 'tight')

# Clear the current image state
plt.clf()
