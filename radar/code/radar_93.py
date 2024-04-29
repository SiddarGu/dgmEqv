import numpy as np
import matplotlib.pyplot as plt

# Transform data into variables
data_labels = np.array(["Detached House", "Townhouse", "Condo", "Apartment", "Duplex"])
line_labels = np.array(["Sale Price ($100k)", "Market Demand (%)", "Rental Yield (%)", "Property Tax ($k)","Mortgage Rate (%)"])
data = np.array([[2.5, 3.0, 2.0, 1.5, 2.75],
                 [7, 8, 7.5, 6.5, 7.5],
                 [5, 4.5, 6, 6.5, 5.5],
                 [2, 2.5, 1.8, 1.5, 2.3],
                 [3, 2.8, 3.2, 3.5, 2.9]])

# Create figure and subplot for the radar chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each row of data with different colors
colors = ['blue', 'green', 'red', 'purple', 'orange']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', color=colors[i], label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title("Real Estate and Housing Market Analysis")

# Add background grids
ax.grid(True, linestyle='--')

# Autoresize image
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/radar/png_train/radar_93.png")

# Clear current image state
plt.clf()