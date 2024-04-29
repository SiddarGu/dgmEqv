import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into required variables
data_string = 'Event,Festival 1,Festival 2,Festival 3,Festival 4/n Audience Attendance,70,75,80,85/n Vendor Satisfaction,60,65,70,75/n Event Organization,80,85,90,95/n Security Efficiency,65,70,75,80/n Performances Quality,75,80,85,90 '
data_strings = data_string.split('/n ')
data_labels = data_strings[0].split(',')[1:]
line_labels = [s.split(',')[0] for s in data_strings[1:]]
data = [list(map(int, s.split(',')[1:])) for s in data_strings[1:]]

# Create the radar chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

max_val = np.max(data)

# Plot data and gridlines
for i, row_data in enumerate(data):
    row_data.append(row_data[0])  # close the loop
    ax.plot(angles, row_data, color=plt.cm.jet(i / len(data)), label=line_labels[i])
    radius = np.full_like(angles, (i+1) * max_val / len(data))
    ax.plot(angles, radius, color='lightgrey', linestyle='-')

# Remove redundant elements and set labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, max_val)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right")

plt.title('Sports and Entertainment Festival Comparison Analysis', size=15, color='black', pad=20)
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/88_2023122292141.png')
plt.close()
