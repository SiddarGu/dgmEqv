import matplotlib.pyplot as plt
import numpy as np

# Parse the data
data = """
Category,Online,In-Store,Mobile,pop up shops
Sales,85,75,90,80
Customer Satisfaction,80,85,70,75
Advertising Impact,70,65,85,80
Return Customers,75,80,70,65
Inventory Efficiency,90,85,80,75
"""
lines = data.split("\n")[1:-1]
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [list(map(int, line.split(",")[1:])) for line in lines[1:]]

# Create figure
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, polar=True)

# Compute angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Loop over data rows
for idx, row in enumerate(data):
    # Close-loop plot
    values = np.append(row, row[0])
    ax.plot(angles, values, label=line_labels[idx])
    # Gridlines
    r = np.full_like(angles, (idx+1) * np.max(data) / len(data))
    ax.plot(angles, r, color="gray", linestyle="dashed")

# Axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Radial limits
ax.set_ylim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove polar y grid and spines
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set title
plt.title('Retail and E-commerce Performance- 2023')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/42_2023122292141.png')

# Clear the current image state
plt.clf()
