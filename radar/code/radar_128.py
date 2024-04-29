import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into variables
data_labels = ['Aspect', 'Small Business', 'Start-Up', 'Corporation', 'Non-profit Organization']
line_labels = ['Revenue (in Million $)', 'Expenses (in Million $)', 'Profit Margin (%)', 'Market Share (%)', 'Employee Satisfaction (Score)']
data = np.array([[75, 60, 90, 50, 85], [50, 65, 70, 45, 60], [20, 15, 25, 10, 30], [15, 10, 35, 5, 30], [80, 75, 85, 70, 90]])

# Create figure and plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Concatenate data for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each data line with different colors
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Plot axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title('Business and Finance Sector Evaluation')

# Save and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/180_202312310100.png')
plt.clf()