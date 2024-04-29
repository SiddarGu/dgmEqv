import numpy as np
import matplotlib.pyplot as plt

data_string = '''Aspect,Theatre A,Theatre B,Theatre C,Theatre D
Audience Ratings,85,80,90,88
Artistic Quality,88,89,92,90
Facility Comfort,75,85,80,88
Marketing Effectiveness,80,75,83,85
Cultural Impact,70,75,80,82'''

# Parse the data
data_lines = data_string.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = np.array([[int(num) for num in line.split(',')[1:]] for line in data_lines[1:]])

# Create a figure
fig = plt.figure(figsize=(8,8))

# Add a subplot with polar coordinates
ax = fig.add_subplot(111, polar=True)

# Calculate the angles for each axis
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data and gridlines
for i, row in enumerate(data):
    # Append the first value to the end of the row to close the loop
    values = np.append(row, row[0])
    ax.plot(angles, values, label=line_labels[i])

    # Create radius vector for gridlines
    radius = np.full_like(angles, (i+1) * np.max(data) / len(data))
    ax.plot(angles, radius, color='gray', ls='--')

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Adjust the radial limits
ax.set_rlim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=180)

# Set the legend labels
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set the title
plt.title('Cultural Venues Performance Analysis', size=20, color='black', style='italic')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/157_2023122292141.png')

# Clear the current figure
plt.clf()
