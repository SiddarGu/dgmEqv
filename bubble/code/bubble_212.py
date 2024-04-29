import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Prepare data
raw_data = """
Transport Method,Fuel Efficiency (km/litre),Cargo Capacity (Tonnes),Speed (km/h),Safety Rating (Score)
Truck,6,30,100,8
Train,18,180,120,7
Ship,23,20000,50,9
Airplane,0.5,200,900,9
Pipeline,0,10000,0,10
Drone,40,2,120,6
"""
rows = [row.split(",") for row in raw_data.split("\n") if row]
data_labels = rows[0][1:]
data = np.array([list(map(float, row[1:])) for row in rows[1:]])
line_labels = [f"{row[0]} {row[3]}" for row in rows[1:]]

# Normalize bubble size and color
norm_size = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
norm_color = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sizes = np.array([(norm_size(v) + 0.1) * 5000 for v in data[:, 2]])

fig, ax = plt.subplots(figsize=(12, 10))

# Scatter plot
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=data[i, 3], 
               cmap="viridis", s=sizes[i], norm=norm_color, label=None)
    ax.scatter([], [], label=line_label, color="black", s=20)

# Legend and colorbar
ax.legend(title=data_labels[2], loc="upper left")
fig.colorbar(ScalarMappable(norm=norm_color, cmap="viridis"), ax=ax, 
             label=data_labels[3])

# Labels and title
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Efficiency and Safety of Different Transportation Methods in Logistics 2023')

# Save figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/161_202312310045.png')

# Clear figure
plt.clf()
