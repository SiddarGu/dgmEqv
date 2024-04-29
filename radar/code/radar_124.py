import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = np.array(["Studio", "1-Bedroom", "Apartments", "Detached House", "Terrace House"])
line_labels = np.array(["Average Price (USD)", "Location Score", "Age of Property (years)", "Size (Square Feet)", "Rental Yield (%)"])
data = np.array([[15, 20, 30, 50, 35],
                 [60, 80, 85, 75, 70],
                 [5, 2, 15, 20, 10],
                 [50, 70, 15, 30, 18],
                 [5.5, 6.0, 6.5, 4.0, 4.5]])

# Create figure and plot data
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each row of data with different colors
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
max_data = np.amax(data)
ax.set_ylim(0, max_data + max_data * 0.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='lower center')

# Add background grids
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

# Set title
plt.title("Real Estate and Housing Market Analysis")

# Automatically resize the image before saving
plt.tight_layout()

# Save the chart as image
save_path = "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/71_202312302350.png"
plt.savefig(save_path)

# Clear the current image state
plt.clf()