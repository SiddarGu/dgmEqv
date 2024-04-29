import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = ['Solar Power', 'Hydropower', 'Wind Energy', 'Bioenergy', 'Geothermal/n Emission Reduction (%)']
line_labels = ['Energy Efficiency (%)', 'Cost Effectiveness (%)', 
               'Sustainability Index (Score)', 'Market Potential (%)']
data = np.array([[90, 85, 95, 80, 85], [75, 80, 85, 90, 95], 
                 [80, 85, 90, 95, 95], [70, 65, 70, 75, 80]])

# Create figure before plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row and append the first numerical element of that row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot the data lines with different colors
colors = ['blue', 'green', 'red', 'orange']
for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], linewidth=2, color=colors[i], label=line_label)

# Plot the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower left')

# Add background grids
ax.grid(True, linestyle='--', linewidth=0.5)

# Set the figure title
plt.title('Sustainable Energy Performance Analysis')

# Automatically resize the image before savefig
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/182_202312310100.png')

# Clear the current image state
plt.clf()