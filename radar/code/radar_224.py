import numpy as np
import matplotlib.pyplot as plt

# Set the data, labels, and line labels

data_labels = ['Hotel Occupancy', 'Tourist Satisfaction', 'Food and Beverage Revenue', 'Attractions Attendance', 'Labor Costs']
line_labels = ['Q1', 'Q2', 'Q3', 'Q4']

data = np.array([
    [75, 80, 85, 90],
    [87, 89, 91, 93],
    [80, 82, 86, 88],
    [80, 85, 90, 95],
    [65, 70, 75, 80]
]).T

# Calculate the angles for each dimension

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Create the figure and the polar subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Plot the radar chart for each row of the data
for i, row in enumerate(data):
    # Append first element to end for close-loop plotting
    expanded_row = np.append(row, row[0])
    ax.plot(angles, expanded_row, label=line_labels[i])

    # Generate the radius for the gridlines 
    radius = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, radius, color='gray', linestyle='--')

# Set the gridlines, labels, and other chart properties
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlabel_position(180)
ax.set_rlim(0, data.max() + 10)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_title("Tourism and Hospitality Performance - 2023", pad=40)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Save and show the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/93_2023122292141.png')

# Clear the current figure
plt.clf()
