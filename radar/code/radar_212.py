import matplotlib.pyplot as plt
import numpy as np

# Process the input data
data_string = 'Category, Q1, Q2, Q3, Q4/n Donations Received, 70, 75, 80, 85/n Expenses, 60, 65, 70, 75/n Volunteer Count, 80, 85, 90, 95/n Fundraising Events, 90, 95, 100, 105/n Public Engagements, 75, 80, 85, 90'
data_lines = data_string.split('/n')
dat = [line.split(',') for line in data_lines]
data_labels = [str.strip(item) for item in dat[0][1:]]
data = [[int(str.strip(item)) for item in sub[1:]] for sub in dat[1:]]
line_labels = [str.strip(sub[0]) for sub in dat[1:]]

# Create data array for plotting and add axis labels
data = np.array(data)
data_labels = np.array(data_labels)
line_labels = np.array(line_labels)

# Create figure
fig = plt.figure(figsize=(10,10))

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Create subplot
ax = fig.add_subplot(111, polar=True)

for idx, row in enumerate(data):
    values = np.append(row, row[0])
    ax.plot(angles, values, linewidth=1, label=line_labels[idx])
    ax.fill(angles, values, alpha=0.25)

    radius_vec = np.full_like(angles, (idx+1) * np.amax(data) / len(data))
    for angle, radius in zip(angles, radius_vec):
        ax.plot([0, angle], [0, radius], color='silver', linestyle='dashed')

# Adjust ticks and labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels, size=12, wrap=True)
ax.set_yticklabels([])

# Remove background and add grid
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set title
ax.set_title('Charity and Nonprofit Organizations - Performance Overview', fontsize=16, loc='center')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/65_2023122292141.png')

# Clear figure
plt.clf()
