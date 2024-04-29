import matplotlib.pyplot as plt
import numpy as np

# Given data
data_str = "Policy,Q1,Q2,Q3,Q4\n Public Infrastructures,80,85,90,95\n Education,70,75,80,85\n Healthcare,75,70,70,75\n Security,85,90,95,100\n Environmental Policy,60,65,70,75"

# Split and re-structure the data
data_arr = [item.split(',') for item in data_str.split('\n')]

data_labels = data_arr[0][1:]
line_labels = [item[0] for item in data_arr[1:]]
data = [list(map(int, item[1:])) for item in data_arr[1:]]

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

max_d = np.max(data)

# Plot data and gridlines
for i, d in enumerate(data):
    d.append(d[0])  # close the loop
    ax.plot(angles, d, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * max_d / len(data))
    ax.plot(angles, radius, color='silver', ls='solid')

# Plot axis labels and adjust radial limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, labels=data_labels)
ax.set_rlim(0, max_d)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=180)

# Remove background and circular gridlines
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set title
plt.title("Government Policy Effectiveness Review")

# Automatically adjust the image size 
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/156_2023122292141.png')

# Clear figure
plt.clf()
