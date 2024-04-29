import numpy as np
import matplotlib.pyplot as plt

# Define the data
data_labels = ['Startup A', 'Startup B', 'Corporate C', 'Franchise D', 'SME E']
line_labels = ['Revenue in Million USD', 'Operating Expenses in Million USD', 'Net Profit Margin (%)', 'Growth Rate (%)', 'Market Share (%)']
data = np.array([[12, 15, 30, 20, 10],
                 [8, 10, 20, 12, 5],
                 [20, 25, 30, 32, 35],
                 [20, 22, 24, 26, 28],
                 [8, 10, 12, 15, 18]])

# Create figure and subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array
for i, row in enumerate(data):
    # Append the first numerical element of that row to the end of that row
    row = np.concatenate((row, [row[0]]))
    
    # Plot the data lines with different colors
    ax.plot(angles, row, label=line_labels[i])

# Set the axis labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels, rotation=45, wrap=True)

# Adjust the radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data) * 1.2)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
ax.set_title('Financial Metrics Comparison')

# Add background grids
ax.grid(True)

# Automatically resize the image
fig.tight_layout()

# Save the image
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/172_202312310100.png'
plt.savefig(save_path)

# Clear the current image state
plt.close(fig)