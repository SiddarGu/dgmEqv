import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Anthropology', 'Sociology', 'Philosophy', 'Psychology', 'History', 'Political Science']
line_labels = ['Research Quality (Score)', 'Teaching Rate (Score)', 'Publication (Count)', 'Employability (Score)', 'Overall Satisfaction (Score)']
data = np.array([[85, 80, 90, 88, 92, 86], 
                 [90, 85, 94, 89, 93, 87], 
                 [75, 70, 80, 78, 82, 76], 
                 [80, 85, 78, 84, 82, 88], 
                 [90, 85, 93, 88, 94, 89]])

# Append first element of each row to the end of the row for closed-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set evenly spaced angles
angles = np.linspace(0, 2*np.pi, len(data_labels) + 1, endpoint=True)

# Plot data lines
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', color=colors[i], label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits based on maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Create legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Set title
plt.title('Academic Performance in Social Sciences and Humanities')

# Add background grids
ax.grid(True)

# Adjust layout and save figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/70_202312302350.png')

# Clear plot
plt.clf()