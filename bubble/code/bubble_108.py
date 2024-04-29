import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Prepare the data
data_str = "Product,Production Volume (Million Units),Factory Floor Area (Million Sq.Ft),Net Profit (Billion $),Safety Rating (Score)\n Cars,70,200,35,10\n Smartphones,500,150,60,8\n Computers,300,100,40,9\n Furniture,250,350,20,10\n Clothing,400,250,30,9\n Food Products,1000,300,50,7\n Pharmaceuticals,50,150,60,10"
lines = data_str.split("\n")
data_labels = lines[0].split(",")
data = np.array([line.split(",")[1:] for line in lines[1:]], dtype=float)
line_labels = [f"{line.split(',')[0]} {data[i, 2]}" for i, line in enumerate(lines[1:])]

# Create the figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)

# Plot the data
cmap = plt.get_cmap("rainbow")
norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]-data[:,2].min()/(data[:,2].max()-data[:,2].min()))*440+60, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], color=cmap(norm(data[i, 3])), label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)

# Add color bar
cbar = fig.colorbar(sm)
cbar.ax.set_title(data_labels[3])

# Add title and labels
ax.set_title('Profit and Safety in Different Product Manufacturing - Production 2023')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[0])

# Set settings
ax.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/317_202312310045.png")

# Clear the figure
plt.clf()
