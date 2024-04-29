import matplotlib.pyplot as plt
import numpy as np

# Parse input
data_input = 'Category,Factory A,Factory B,Factory C,Factory D/n Productivity,85,80,75,70/n Quality Control,90,85,80,75/n Cost Efficiency,75,80,85,90/n Schedule Adherence,80,85,90,95/n Safety,70,65,60,55'
data_input_split = [s.split(',') for s in data_input.split('/n')]

line_labels = [row.pop(0) for row in data_input_split[1:]]
data_labels = data_input_split[0][1:]
data = np.array([[int(val) for val in row] for row in data_input_split[1:]])

# Create figure
fig = plt.figure(figsize = (8, 8))
ax = plt.subplot(111, polar=True)
ax.set_title('Manufacturing Performance Analysis')

max_val = np.max(data)
num_vars = len(data_labels)
angles = np.linspace(0, 2*np.pi, num_vars + 1, endpoint=True)

# Loop over data rows
for i, vals in enumerate(data):
    vals = np.append(vals, vals[0]) # Close loop
    ax.plot(angles, vals, label=line_labels[i])
    ax.fill(angles, vals, alpha=0.1)
    radius = np.full_like(angles, (i + 1) * max_val / len(data))
    ax.plot(angles, radius, color='silver', linestyle='dashed')

# Add axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
# Adjust radial limits
ax.set_rlim(0, max_val)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/135_2023122292141.png')
plt.clf()
