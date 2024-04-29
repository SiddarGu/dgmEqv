import numpy as np
import matplotlib.pyplot as plt

# Given data transformation
data_str = "Aspect,Q1,Q2,Q3,Q4\n Property Sale Volume,500,550,600,650\n Rental Demand,400,450,500,550\n Development Cost,350,400,450,500\n Mortgage Rate,3.0,3.5,4.0,4.5\n Market Liquidity,75,80,85,90 "

data_lines = data_str.split("\n")

data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = [list(map(float, line.split(",")[1:])) for line in data_lines[1:]]

# Create radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(polar=True)

# Create angles for data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data lines
for i, d in enumerate(data):
    data_array = np.array(d + [d[0]])
    line, = ax.plot(angles, data_array, label=line_labels[i])
  
    # Draw multiple straight lines as gridlines
    radius = np.full_like(angles, (i + 1) * max(max(data)) / len(data))
    ax.plot(angles, radius, color='grey', alpha=0.5, linewidth=0.5)

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, wrap=True)

# Set radial limits
ax.set_ylim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set title
plt.title("Real Estate and Housing Market Analysis", size=20, color='black', y=1.1)

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/143_2023122292141.png')

# Clear current image state
plt.clf()
