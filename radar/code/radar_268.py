import matplotlib.pyplot as plt
import numpy as np

# Prepare data
raw_data = '''Category,Organisation A,Organisation B,Organisation C,Organisation D
Fundraising Efficiency,80,85,90,95
Nonprofit Program Expense Percentage,70,75,80,85
Donation Revenue,85,80,75,70
Public Support,90,85,80,75
Service Outreach,75,80,85,90'''
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [list(map(int, line.split(',')[1:])) for line in lines[1:]]

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data
for idx, datapoints in enumerate(data):
    datapoints.append(datapoints[0])  # Close-loop
    ax.plot(angles, datapoints, label=line_labels[idx])

# Grid lines
for idx in range(len(data)):
    radius = np.full_like(angles, (idx + 1) * max(max(data)) / len(data))
    ax.plot(angles, radius, color='grey', linestyle='--')

# Add the axis label
ax.set_thetagrids((angles[:-1] * 180 / np.pi), labels=data_labels, wrap=True)

# Remove the circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Adjust the radial limits
ax.set_rlim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-90)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, data_labels, loc="upper right")

# Set title
plt.title("Charity and Nonprofit Organization Performance Assessment")

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/163_2023122292141.png')

# Clear the current image state
plt.clf()
