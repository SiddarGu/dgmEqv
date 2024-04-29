import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Create variables from data
data_labels = ["Energy Consumption (MWh)", "Renewable Energy (%)", "Total Carbon Emissions (MMT)", "Electricity Price (cents/kWh)"]
data = np.array([
    [1000000, 20, 1000, 10], 
    [800000, 30, 800, 12], 
    [1200000, 25, 1500, 8], 
    [500000, 15, 500, 15], 
    [400000, 10, 300, 20], 
    [200000, 40, 400, 14], 
    [0, 0, 0, 0]
])
line_labels = ["North America", "Europe", "Asia", "South America", "Africa", "Australia", "Antarctica"]

# Create figure and plot data
fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.get_cmap("viridis")
normalize = plt.Normalize(data[:,3].min(), data[:,3].max())

for i in range(data.shape[0]):
    line_label= line_labels[i]+' '+str(data[i, 2]) # preparing line label
    sc = ax.scatter(data[i, 0], data[i, 1], label=None, 
                    s= (data[i, 2] / np.max(data[:, 2]))* 4400 + 600,
                    c= cmap(normalize(data[i, 3])))
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label) 

# Add legend and title
plt.title('Energy Consumption and Environmental Impact by Region')
plt.grid(visible=True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

lgnd = ax.legend(title=data_labels[2], fontsize='small',loc="best",bbox_to_anchor=(1,0.5))
grid = make_axes_locatable(ax)
cax = grid.append_axes("right", size="5%", pad=0.2)
plt.colorbar(sc, cax=cax, orientation='vertical', label=data_labels[3])

fig.tight_layout()

# Save and clear the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/351_202312311429.png')
plt.clf()
