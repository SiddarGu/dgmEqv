import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

# Parsing data
raw_data = """Product,Cafe A,Cafe B,Restaurant A,Restaurant B
Coffee Quality,85,80,90,87
Food Taste,90,85,87,92
Service Quality,75,80,82,80
Ambient Environment,80,85,90,92
Price Level,70,72,75,78"""

lines = raw_data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
raw_data = [[int(num) for num in line.split(",")[1:]] for line in lines[1:]]
data = np.array(raw_data)

# Initialize the figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
ax.set_title('Food and Beverage Industry Performance Comparison', size=20, color="black", y=1.1)

# Compute angle for each axis
num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars+1, endpoint=True)

# Draw data lines
for idx, d in enumerate(data):
    d = np.concatenate((d, [d[0]])) # complete the loop
    ax.plot(angles, d, 'o-', label=line_labels[idx])
    ax.fill(angles, d, alpha=0.25)

    # Draw grid lines
    grid_value = (idx + 1) * max(data.flatten()) / len(data)
    radial_grid_values = np.full_like(angles, fill_value=grid_value)
    ax.plot(angles, radial_grid_values, color='gray', linestyle=(0, (1, 5))) 

# Set axis labels & legend
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_ylim(0, np.ceil(max(data.flatten())))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Format spines & grid
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False) 

# Save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/126_2023122292141.png")
plt.clf()
