
import matplotlib.pyplot as plt
import numpy as np

# Parsing data

data = """
    Aspect,Gallery A,Gallery B,Gallery C,Gallery D/n 
    Exhibition Quality,80,85,90,95/n 
    Visitor Satisfaction,78,83,88,93/n 
    Seat Accommodation,90,87,84,81/n 
    Sound System,75,80,85,90/n 
    Food and Beverage,68,73,78,83
"""
lines = data.strip().split("/n")
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data_values = [list(map(int, line.split(',')[1:])) for line in lines[1:]]
for d in data_values: d.append(d[0])

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(polar=True)
ax.set_title('Gallery Performance Analysis in Arts and Culture', size=20, color='black', y=1.1)

# Create angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data
colors = ['b', 'g', 'r', 'c', 'm', 'y']
for idx, values in enumerate(data_values):
    ax.plot(angles, values, 'o-', color=colors[idx % len(colors)], label=line_labels[idx], linewidth=2)
    ax.fill(angles, values, color=colors[idx % len(colors)], alpha=0.25)

    radius = np.full_like(angles, (idx + 1) * np.max(data_values) / len(data_values))
    ax.plot(angles, radius, color=colors[idx % len(colors)], alpha=0.1)

# Customize axis
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.ceil(np.max(data_values)))
max_value = np.amax(data_values)
step_size = max_value / len(data_values)
ax.set_rgrids([step_size * i for i in range(1, len(data_values) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data_values) + 1)], angle=-90)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/171_2023122292141.png')

# Clear figure
plt.clf()

