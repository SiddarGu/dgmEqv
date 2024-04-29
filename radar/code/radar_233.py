import numpy as np
import matplotlib.pyplot as plt

# Transform raw data
raw_data = ["Aspect,Web A,Web B,Web C,Web D", "Page Views,78,85,82,79", "Site Uptime,95,91,93,94", 
           "User Engagement,68,72,74,70", "Site Speed,82,88,86,84", "Bounce Rate,55,52,50,48"]
raw_data = [x.split(",") for x in raw_data]
data_labels = raw_data[0][1:]
data = np.array([list(map(int, x[1:])) for x in raw_data[1:]])
line_labels = [x[0] for x in raw_data[1:]]

# Set up the figure and subplot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = ['b', 'r', 'g', 'm', 'y']
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

for i, row in enumerate(data):
    ax.plot(angles, np.append(row, row[0]), color=colors[i], label=line_labels[i])
    ax.fill(angles, np.append(row, row[0]), color=colors[i], alpha=0.25)
    ax.plot(angles, np.full_like(angles, (i + 1) * np.amax(data) // len(data), dtype=int), color=colors[i], linestyle='dotted')

# Adjust properties 
ax.set_ylim(0, np.amax(data) * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set title and save figure
plt.title("Website Performance Review", size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/152_2023122292141.png')
plt.close('all') # Closes all the figure windows
