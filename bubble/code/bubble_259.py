import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

data_string = "Product,Production Capacity (Million Units),Factory Occupancy Rate (%),Profit Margin (%),Quality Score (Out of 10)\
                \nSmartphones,500,80,25,9\
                \nLaptops,300,75,20,8\
                \nTelevisions,400,70,22,7\
                \nPrinters,200,65,18,6\
                \nWashing Machines,250,60,24,8\
                \nRefrigerators,350,85,20,7\
                \nMicrowaves,150,80,23,7\
                \nAir Conditioners,300,77,26,9\
                \nElectric Cars,200,90,30,8"

# Parse the string into a numpy array
data_lines = data_string.split("\n")
data_labels = data_lines[0].split(",")
data_values = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)
line_labels = [f"{line.split(',')[0]} ({int(val[2])})" for line, val in zip(data_lines[1:], data_values)]

# Normalize color and size data to range 0-1
min_size, max_size = data_values[:,2].min(), data_values[:,2].max()
size_scale = lambda x: 600+(x-min_size)*(5000-600)/(max_size-min_size)
color_norm = mcolors.Normalize(data_values[:,3].min(), data_values[:,3].max())

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)

cmap = plt.get_cmap("viridis")
for i, line_label in enumerate(line_labels):
    ax.scatter(data_values[i, 0], data_values[i, 1], c=cmap(color_norm(data_values[i, 3])), s=size_scale(data_values[i, 2]), label=None)
    ax.scatter([], [], c=cmap(color_norm(data_values[i, 3])), s=20, label=line_label)

# Title and labels
ax.set_title("Performance Analysis of Various Manufactured Products in 2023")
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

# Legend and colorbar
ax.legend(title=data_labels[2], loc='upper left')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=color_norm)
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Save and show the image
fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/126_202312301731.png")
plt.clf()
