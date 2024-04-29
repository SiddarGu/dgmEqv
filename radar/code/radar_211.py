import matplotlib.pyplot as plt
import numpy as np

# Data transformation
raw_data = "Category,UNICEF,Red Cross,Oxfam,World Vision/n Donations Received,95,90,85,80/n Community Outreach,90,85,80,75/n Volunteer Participation,85,80,75,70/n Project Completion,80,75,70,65/n Administration Costs,75,70,65,60"
raw_data = raw_data.replace("/n", "\n").split("\n")
data_labels = raw_data[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in raw_data[1:]]
data = [list(map(int, line.split(',')[1:])) for line in raw_data[1:]]

# Initiate the radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Plot each line of data
for idx, d in enumerate(data):
    d += d[:1]  # Closing the polygonal line
    ax.plot(angles, d, label=line_labels[idx])
    ax.fill(angles, d, alpha=0.25)
    radii = np.full_like(angles, (idx + 1) * max(max(data)) / len(data))
    ax.plot(angles, radii, color='gray', linestyle='dashed')
    
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_rlim(0, np.ceil(max(max(data))))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

fig.suptitle('Performance Analysis of Nonprofit Organizations')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/41_2023122292141.png')
plt.clf()
