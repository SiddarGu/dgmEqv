import numpy as np
import matplotlib.pyplot as plt

# Process data
data_str = 'Sector,Q1,Q2,Q3,Q4\n IT,80,85,90,95\n Retail,70,75,80,85\n Manufacturing,60,65,70,75\n Healthcare,50,55,60,65\n Real Estate,65,70,75,80'
data_arr = [line.split(',') for line in data_str.split('\n')]
data_labels = data_arr[0][1:]
line_labels = [line[0] for line in data_arr[1:]]
data = [list(map(int, line[1:])) for line in data_arr[1:]]

# Create angle array
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Expand data for closed loop plotting
data = [np.append(arr, arr[0]) for arr in data]

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

for i in range(len(data)):
    # Draw data lines
    ax.plot(angles, data[i], label=line_labels[i])
    
    # Draw grid lines
    radius = np.full_like(angles, (i+1) * np.max(data) / len(data))
    ax.plot(angles, radius, color='lightgrey', linestyle='--', linewidth=1)

# Configure axis
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.set_ylim(bottom=0, top=np.max(data))
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Draw legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))

# Set title
plt.title('Sector-wise Business Performance - 2023', size=20, color='black', y=1.1)

# Save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/26_2023122292141.png")
plt.clf()
