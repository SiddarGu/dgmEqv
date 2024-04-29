import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_str = 'Measure,Hydro,Geothermal,Wind,Solar/n Energy Production,80,83,86,89/n Utility Costs,75,70,79,85/n Grid Availability,87,88,89,90/n Sustainability,90,95,88,98/n Regulation Compliance,85,79,90,95'
data_str = data_str.replace('/n ', '\n').split('\n')
data_labels = data_str[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in data_str[1:]]
data = np.array([list(map(int, row.split(',')[1:])) for row in data_str[1:]])

# Plot the data with the type of radar chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
ax.set_title('Energy and Utilities Performance Metrics', size=20, color='black', weight='normal')

# Evenly space the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=45)

# Plot each data line
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for idx, row_data in enumerate(data):
    row_data = np.concatenate((row_data, [row_data[0]]))
    ax.plot(angles, row_data, 'o-', color=colors[idx % len(colors)], label=line_labels[idx], linewidth=2)
    radius = np.full_like(angles, (idx+1) * np.max(data) / len(data))
    ax.plot(angles, radius, '--', color=colors[idx % len(colors)])

# Adjust the radial limits
ax.set_rlim(0, np.ceil(np.max(data) / 10) * 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=180)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove the circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Save and show the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/148_2023122292141.png')
plt.close(fig)
