import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Coal', 'Nuclear', 'Solar', 'Wind', 'Hydropower']
data = np.array([[70, 75, 80, 85, 90], [50, 55, 60, 65, 70], 
                 [60, 65, 70, 75, 80], [80, 85, 90, 95, 100], 
                 [65, 70, 75, 80, 85]])
line_labels = ['Production Efficiency', 'Environmental Impact', 
               'Cost Efficiency', 'Energy Output', 'Market Penetration']

# Create radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Calculate angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data and gridlines
colors = plt.cm.get_cmap("hsv", len(data) + 1)  # list of colors for the different plots
for i, row in enumerate(data):
    row = np.append(row, row[0])  # ensure the loop closure of data

    # Plot data
    ax.plot(angles, row, color=colors(i), label=line_labels[i])

    # Plot gridlines
    gridline_values = np.full_like(angles, (i + 1) * np.amax(data) / len(data))
    ax.plot(angles, gridline_values, '-', color='grey', linewidth=0.5, alpha=0.3)

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Adjust radial limits
ax.set_rlim(0, np.amax(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-75)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", title="Lines")

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set title
ax.set_title('Energy and Utilities Sector Performance', size=20, color="black", y=1.1)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/122_2023122292141.png')

# Clear the current image state
plt.clf()
