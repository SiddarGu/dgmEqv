import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['Red Cross', 'UNICEF', 'Save The Children', 'Greenpeace', 'WWF/n Fundraising Efficiency (%)']
line_labels = ['Aspect', 'Program Expense Ratio (%)', 'Working Capital Ratio (%)', 'Transparency Score (%)', 'Administrative Cost (%)']
data = np.array([[75, 80, 85, 90, 95],
                 [80, 85, 70, 75, 90],
                 [65, 70, 65, 80, 85],
                 [90, 95, 85, 90, 95],
                 [15, 10, 15, 20, 15]])

# Plot the radar chart
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end of that row for closed-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each data line with different colors
colors = ['blue', 'orange', 'green', 'red', 'purple']
for i, row in enumerate(data):
    ax.plot(angles, row, 'o-', linewidth=2, color=colors[i], label=line_labels[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)
max_val = np.max(data)
ax.set_ylim(0, max_val)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Add background grid
ax.grid(True)

# Set the title
plt.title("Comparative Analysis of Charity and Nonprofit Organizations Performance")

# Automatically resize the image and save
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/113_202312302350.png")

# Clear the current image state
plt.clf()