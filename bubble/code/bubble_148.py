import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

city_data = """New York,850,3.6,8.5,65
Los Angeles,750,2.9,4.1,60
Chicago,320,2.2,2.8,56
Houston,240,1.9,2.4,54
Philadelphia,200,1.5,1.6,52
Phoenix,350,1.7,1.8,50"""

# data Transform
lines = city_data.split("\n")
data_labels = ["Average House Price", "Average Rent", "Population", "Average Household Income"]
line_labels = [line.split(",")[0] for line in lines]
data = np.array([list(map(float, line.split(",")[1:])) for line in lines])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

size_norm = Normalize(data[:,2].min(), data[:,2].max())
color_norm = Normalize(data[:,3].min(), data[:,3].max())
                        
for i, line_label in enumerate(line_labels):
    scatter = ax.scatter(data[i, 0], data[i, 1], c=data[i, 3], cmap='viridis', s=size_norm(data[i, 2])*4500+600, norm=color_norm, label=None)
    ax.scatter([], [], color=get_cmap("viridis")(color_norm(data[i, 3])), label=f'{line_label} {data[i,2]}')
                      
ax.legend(title=data_labels[2])
ax.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])

fig.suptitle('Comparative Analysis of Real Estate & Housing Market Across Major U.S. Cities', fontsize=14)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/109_202312301731.png', dpi=300)
plt.cla()
