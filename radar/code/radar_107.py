import numpy as np
import matplotlib.pyplot as plt

data = np.array([[70, 75, 80, 65, 60],
                 [8, 9, 7, 5, 6],
                 [90, 85, 80, 95, 90],
                 [20, 25, 30, 35, 40],
                 [30, 35, 40, 45, 50]])

data_labels = ['Clothing', 'Electronics', 'Toys', 'Groceries', 'Beauty Products']
line_labels = ['Sales (%)', 'Returns (%)', 'Customer Satisfaction (Score)', 'Market Share (%)', 'Profit Margin (%)']

# Close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Set up figure and axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

# Set evenly spaced angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data lines
colors = ['blue', 'green', 'red', 'orange', 'purple']
for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], linewidth=2, label=line_label, color=colors[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title('Retail and E-commerce Performance Analysis')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/148_202312302350.png')

# Clear current image state
plt.close()
