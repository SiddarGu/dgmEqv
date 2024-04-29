import matplotlib.pyplot as plt
import numpy as np

# Preprocess data
data_str = 'Category,Quarter 1,Quarter 2,Quarter 3,Quarter 4/n Employee Retention,85,90,95,87/n Training Efficiency,60,70,80,85/n Job Satisfaction,75,82,88,91/n Performance Assessment,80,85,90,95/n Payroll Management,65,70,75,80'
data_str = data_str.replace('/n', '\n').split('\n')
line_labels = [i.split(',')[0] for i in data_str[1:]]
data_labels = data_str[0].split(',')[1:]
data = np.array([i.split(',')[1:] for i in data_str[1:]], dtype=float)
# Create radar chart
num_vars = len(data_labels)
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
# Iterate over each row in the data array
for row_index, row in enumerate(data):
    # append the first numerical element of that row to its end
    data_row = np.append(row, row[0])
    ax.plot(angles, data_row, label=line_labels[row_index])
    ax.fill(angles, data_row, alpha=0.25)
    radius = np.full_like(angles, (row_index+1) * np.max(data) / len(data))
    ax.plot(angles, radius, color='gray', ls=':')
# Plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Adjust the radial limits
ax.set_ylim(0, np.ceil(np.max(data) / 10) * 10)
# Legend positioning
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
# Remove the circular gridlines and background
ax.yaxis.grid(False)
fig.suptitle('Human Resources and Employee Performance Status')
plt.tight_layout()
# Save the image to a local path
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/25_2023122292141.png')
# Clear the current image state
plt.clf()
