import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Given data
data_str = ["Fossil Fuels,20000,18000,90,15000",
"Nuclear Power,10000,9500,95,1000",
"Hydroelectric Power,6000,5800,97,500",
"Solar Power,3000,2900,97,200",
"Wind Energy,4000,3900,98,100",
"Geothermal Energy,1000,990,99,50"]

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = "Production (Billion KWh),Consumption (Billion KWh),Efficiency (%),Carbon Footprint (Million Tonnes)".split(',')
line_labels = [x.split(',')[0] for x in data_str]
data = np.array([x.split(',')[1:] for x in data_str]).astype(float)

# Create the figure
plt.figure(figsize=(12,8))

ax = plt.gca()

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i] + f' {data[i, 2]}')

cbar = plt.colorbar(scatter, norm=norm)
cbar.set_label(data_labels[3])
ax.legend(title=data_labels[2], loc='upper left')


plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Energy Production and Consumption - Utilities 2023')
ax.set(xlabel=data_labels[1], ylabel=data_labels[2])
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/291_202312310045.png')
plt.clf()
