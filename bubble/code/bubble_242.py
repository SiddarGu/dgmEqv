import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib import colors

# Parsing the data 
data_str = "Vehicle Type,Transport Volume (Billion Tonnes),Fuel Consumption (Million Litres),Efficiency (Score),Environmental Impact (Score)\nTrucks,45,250,15,40\nShips,60,500,20,35\nAirplanes,15,1200,28,25\nTrains,30,150,22,50\nPipelines,50,50,30,15 "
lines = data_str.split('\n')
data_labels = lines[0].split(',')
data_lines = [line.split(',') for line in lines[1:]]
line_labels = [f"{line[0]} {line[2]}" for line in data_lines]
data = np.array([[float(val) for val in line[1:]] for line in data_lines])

# Normalizing variables
norm_color = colors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
norm_size = colors.Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
cmap = plt.get_cmap("viridis")

# Figure creation
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# Plots each point
for i, line_label in enumerate(line_labels):
    ax.scatter(
        data[i, 0],
        data[i, 1],
        c=cmap(norm_color(data[i, 3])),
        s=norm_size(data[i, 2]) * (5000-600) + 600,
        label=None
    )
    ax.scatter([], [], c=cmap(norm_color(data[i, 3])), label=line_label)

ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

# Plot legend
legend_title = data_labels[2]
ax.legend(title=legend_title,loc='upper left')

# Add color bar
cbar = plt.colorbar(ScalarMappable(cmap=cmap, norm=norm_color),ax=ax)
cbar.set_label(data_labels[3])

# Figure settings
plt.title("Logistics and Transportation Efficiency Analysis")
plt.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/173_202312310045.png")
plt.clf()
