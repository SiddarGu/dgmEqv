import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ["Sales Revenue ($1000)", "Customer Retention (%)", "Profit Margin (%)", "Market Share (%)", "Return Rate (%)"]
line_labels = ["Amazon", "eBay", "Etsy", "Zalando", "AliExpress"]
data = np.array([[42, 37, 40, 38, 41],
                 [70, 60, 80, 85, 70],
                 [15, 17, 18, 16, 14],
                 [22, 20, 19, 18, 21],
                 [10, 8, 12, 11, 9]])

# Create figure and subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to close the loop
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each row as a separate line with different colors
colors = ['blue', 'green', 'red', 'orange', 'purple']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', color=colors[i], linewidth=2, label=line_labels[i])

# Set axis labels with proper rotation
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=45, wrap=True)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
ax.set_title("E-commerce Companies Performance Overview")

# Add background grid
ax.grid(True)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/67_202312302350.png")

# Clear the current image state
plt.clf()
