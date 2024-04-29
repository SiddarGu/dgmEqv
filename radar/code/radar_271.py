import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data = [
    [80, 85, 75, 70],
    [85, 90, 70, 65],
    [70, 80, 90, 85],
    [60, 70, 80, 75],
    [95, 90, 85, 80]
]
data_labels = ['Case Success Rate', 'Client Satisfaction', 'Staffing Efficiency', 'Case Load', 'Compliance Rate']
line_labels = ['Small Firm', 'Large Firm', 'Government', 'Non-profit']

# Create figure before plotting.
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(polar=True)

# Evenly space the angles.
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row and plot data.
for i, row in enumerate(np.array(data).T):
    row = np.append(row, row[0])  # Close the plot.
    ax.plot(angles, row, label=line_labels[i])
    ax.fill(angles, row, 'b', alpha=0.1)
    radius = np.full_like(angles, (i + 1) * np.amax(data) / len(data))
    plt.polar(angles, radius, ls='--', color='grey')

# Plot the axis label.
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(top=np.amax(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=15)

# Plot the legend.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove the circular gridlines and background.
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Title of the figure.
plt.title('Comparative Analysis of Legal Firms', size=20, color='black', y=1.1)

# Save the image.
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/37_2023122292141.png')

# Clear the current figure.
plt.clf()
