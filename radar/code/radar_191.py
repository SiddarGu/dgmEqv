import numpy as np
import matplotlib.pyplot as plt

# Data
data_labels = ['Spring', 'Summer', 'Autumn', 'Winter']
line_labels = ['Crop Yield', 'Livestock Productivity', 'Fertilizer Use', 'Pesticide Use', 'Water Usage', 'Food Production']
data = [
    [65,85,65,30],
    [60,70,65,60],
    [70,80,65,50],
    [80,85,60,50],
    [85,95,70,55],
    [75,85,70,40]
]

# Create figure
fig = plt.figure(figsize=(8,8))

# Add subplot with polar projection
ax = fig.add_subplot(111, polar=True)

# Compute angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over the rows
for i, row in enumerate(data):
    row.append(row[0])  # Close the loop
    ax.plot(angles, row, label=line_labels[i])
    ax.fill(angles, row, alpha=0.25)

    # Draw gridlines
    radius = np.full_like(angles, (i+1) * max([item for sublist in data for item in sublist]) / len(data))
    ax.plot(angles, radius, color='gray', linestyle='--', linewidth=0.5)

# Configure axes
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)  # Set the axis labels
ax.set_rlim(0, max([item for sublist in data for item in sublist]))  # Adjust radial limits
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Legend plot
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set chart preferences
ax.spines['polar'].set_visible(False)  # Remove the circular background
ax.yaxis.grid(False) # Remove the radial gridlines
plt.title('Seasonal Evaluation of Agriculture and Food Production', size=20, color='black', y=1.1)

# Resize the image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/68_2023122292141.png')

# Clear the current image state
plt.clf()
