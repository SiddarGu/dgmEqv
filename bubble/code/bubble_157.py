import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable

# Data preparation
data_str = """Cars,70,200,15,8
Smartphones,200,150,20,9
Furniture,100,180,18,8
Clothing,400,250,25,7
Electronics,150,120,22,9
Home Appliances,250,190,16,7
Toys,450,220,30,6"""
data_str = [i.split(',') for i in data_str.split('\n')]

data_labels = ["Annual Production (Million Units)", "Number of Factories", 
               "Profit Margin (%)", "Quality Assurance (Score)"]
data = np.array([i[1:] for i in data_str], dtype=float)
line_labels = [i[0] + ' ' + str(data[i_, 2]) for i_, i in enumerate(data_str)]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10,8))

# Normalizing the color and bubble size
norm = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
sm = ScalarMappable(norm=norm, cmap=plt.get_cmap("viridis"))
bubble_size = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600, 5000))

# Plotting the data
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], color=sm.to_rgba(data[i, 3]),
               alpha=0.6, edgecolors='w', linewidths=1, s=bubble_size[i], label=None)
    ax.scatter([], [], color=sm.to_rgba(data[i, 3]), label=line_label)

# Setting the legend
ax.legend(title=data_labels[2], loc='upper left')

# Adding a color bar
cbar = plt.colorbar(sm)
cbar.ax.set_title(data_labels[3])

# Labels and title
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.grid(True)
plt.title('Profitability and Quality of Various Products in Manufacturing and Production Sector', wrap=True)

# Adjust and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/208_202312310045.png')
plt.clf()
