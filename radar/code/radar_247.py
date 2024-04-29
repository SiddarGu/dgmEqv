import numpy as np
import matplotlib.pyplot as plt

# Transform given data
data_str = "Sector,Q1,Q2,Q3,Q4\nProduct Quality,80,84,88,92\nProduction Efficiency,75,78,81,84\nSupply Management,70,72,74,76\nCost Efficiency,80,82,84,86\nMarket Reach,67,70,73,76"
lines = data_str.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [list(map(int, line.split(",")[1:])) for line in lines[1:]]

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over the rows
for idx, row in enumerate(data):
    values = row + row[:1]  # Close loop
    ax.plot(angles, values, lw=2, label=line_labels[idx])
    ax.fill(angles, values, 'b', alpha=0.05)
    radius = np.full_like(angles, (idx+1) * max(max(data)) / len(data))
    ax.plot(angles, radius, color='black', ls='--', lw=0.5)

# Plot axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.2, 1.1))

# Style adjustments
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Title
plt.title('Manufacturing and Production Performance Analysis')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/64_2023122292141.png', bbox_inches='tight')

# Clear the current image
plt.clf()
