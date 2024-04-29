import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Raw data
raw_data = [["Wheat",3,200,15,700],
            ["Rice",6,300,13,600],
            ["Corn",800,250,17,900],
            ["Soybeans",2.5,150,12,800],
            ["Sugar Cane",7,500,20,1000],
            ["Potatoes",20,100,10,500],
            ["Tomatoes",80,50,8,300]]
data_labels = ["Yield (Tonnes/Hectare)","Water Usage (Millions Cubic Meter)","Employment Rate (%)","Waste Produced (Tonnes)"]

# Convert data into numpy array
data = np.array(raw_data)[:, 1:].astype(float)
line_labels = [f"{c} {y}" for c, y in zip(np.array(raw_data)[:, 0], data[:,2])]

# Figure creation
plt.figure(figsize=(16,8))
ax = plt.subplot(111)

cdict = {'red': ((0.0, 0.0, 0.0),   # no red at 0
                 (0.5, 1.0, 1.0),   # all red at 0.5
                 (1.0, 1.0, 1.0)),  # all red at 1
         'green': ((0.0, 0.0, 0.0), # no green at 0
                  (1.0, 0.0, 0.0)), # no green at 1
         'blue': ((0.0, 0.0, 1.0),  # all blue at 0
                  (0.5, 0.1, 0.1),  # no blue at 0.5
                  (1.0, 0.0, 0.0))  # no blue at 1
         }
cmap = mcolors.LinearSegmentedColormap('my_colormap', cdict, 1024)

# Normalize to the range of colors
norm = plt.Normalize(data[:, 3].min(), data[:, 3].max())

# Scatter plot with different color and size
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=cmap(norm(data[i, 3])), s=(data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 4400 + 600, label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_label)

# Add a grid
ax.grid(True, linestyle="-.", color="grey", alpha=0.7)

# Add a colorbar
sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
plt.colorbar(sm, ax=ax, orientation="vertical", format="%d", label=data_labels[3])

# Add a legend
leg = ax.legend(title=data_labels[2], loc="upper right")
plt.setp(leg.get_title(), multialignment='center')

# Set labels
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set title
plt.title("Comparison of Crop Yield, Water Usage, Employment and Waste Production in Agriculture")

# Save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/144_202312301731.png")

# Clear the current image state
plt.clf()
