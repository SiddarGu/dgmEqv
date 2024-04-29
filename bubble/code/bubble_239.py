import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd

# Given data
data = np.array([
[2000, 4000, 30, 15],
[1500, 3800, 35, 20],
[500, 3000, 50, 5],
[100, 2800, 40, 95],
[50, 2000, 60, 100],
[30, 1800, 55, 100],
[20, 1600, 45, 100],
[40, 1400, 45, 70]])

data_labels = ["Emission (Million Tonnes)", "Consumption (Million MWh)", "Profit ($ Billion)", "Renewable Energy Use (%)"]
line_labels = ["Coal", "Natural Gas", "Nuclear", "Hydroelectric", "Solar", "Wind", "Geothermal", "Biomass"]

# Setup color map 
cmap = plt.get_cmap('viridis')

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(111)

# Normalize the bubble size and color
bubble_size = mcolors.Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
bubble_color = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

for i in range(len(data)):
    line_label = f"{line_labels[i]} {data[i, 2]}"
    ax.scatter(data[i, 0], data[i, 1], c=cmap(bubble_color(data[i, 3])), s=600 + 4400 * bubble_size(data[i, 2]), label=None)
    ax.scatter([], [], c=cmap(bubble_color(data[i, 3])), s=20, label=line_label)

ax.set_ylabel(data_labels[0])
ax.set_xlabel(data_labels[1])

# Add a color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=5,vmax=100))
sm.set_array([])
fig.colorbar(sm, orientation="vertical", shrink=0.5, label=data_labels[3])

ax.grid(True)
ax.legend(title=data_labels[2], loc='upper left', fontsize=8)

plt.title("Emissions, Consumption, and Profit of Various Energy Utilities")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/179_202312310045.png")
plt.clf()
