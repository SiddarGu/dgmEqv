import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Innovation Index', 'Safety Standards Score', 'Sustainability Rating', 'Collaboration Efficiency', 'Research Impact (Score)']
data = np.array([
    [87, 90, 75, 82, 77],
    [83, 94, 78, 85, 80],
    [89, 92, 72, 81, 75],
    [85, 95, 76, 83, 78]
])
line_labels = ["Engineering A", "Engineering B", "Engineering C", "Engineering D"]

# Create figure and subplot for radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels)+1, endpoint=True)

# Iterate over each row in the data array
colors = ['b', 'r', 'g', 'm']
for idx, row in enumerate(data):
    # Append the first numerical element of that row to its end for close-loop plotting of data lines
    row = np.append(row, row[0])
    ax.plot(angles, row, color=colors[idx])
    # Generate a angle-like radius vector with constant values
    radius = np.full_like(angles, (idx+1) * np.amax(data) / len(data))
    ax.plot(angles, radius, color='grey', ls='--')

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True, fontsize=9)
ax.set_rgrids(np.arange(20, np.amax(data)+1, 20), labels=None, angle=0 )
# Adjust the radial limits to accommodate
ax.set_rlim(0, np.amax(data)+10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend   
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove the circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set title and save image
plt.title("Engineering Practices Performance Evaluation", size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/191_2023122292141.png')

# Clear the current image state
plt.clf()
