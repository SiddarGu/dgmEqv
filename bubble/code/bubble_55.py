import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import matplotlib.colors as colors

# Prepare data
raw_data = """
Farming Method,Yield (Tonnes per Hectare),Cost (Million $),Pesticide Use (Tonnes),Water Usage (m³ per Hectare)
Conventional,10,4,15,2000
Organic,7,5,3,1500
Hydroponic,20,7,2,1000
Vertical Farming,30,10,1,500
Aquaponics,12,6,0,1000
Agroforestry,6,3,5,1500
"""

# Parse data into list of lists
data_list = [row.split(",") for row in raw_data.strip().split("\n")]

# Create labels and data
data_labels = data_list[0][1:]
line_labels = [f"{row[0]} {row[3]}" for row in data_list[1:]]
data = np.array([[float(val) for val in row[1:]] for row in data_list[1:]])

# Create color map
cmap = cm.get_cmap("viridis")

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
for i, line_label in enumerate(line_labels):
    size = data[i, 2]*800 + 60 # Normalize bubble size
    data_color = data[i, 3]/max(data[:, 3])  # Normalize color value to range of color map
    ax.scatter(data[i, 0], data[i, 1], s=size, c=cmap(data_color), alpha=0.6, edgecolors='w', label=None)
    ax.scatter([], [], c=cmap(data_color), alpha=0.6, s=20, label=line_label)

# Legend
ax.legend(title=data_labels[2], loc='lower right')

# Color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation="vertical", fraction=0.15, pad=0.05).set_label(data_labels[3])

# Titles
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Comparison of Different Farming Methods in Food Production 2023')

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/97_202312301731.png', dpi=300)
plt.clf()
