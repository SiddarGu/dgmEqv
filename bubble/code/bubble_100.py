import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import numpy as np

data = """Farm,Sustainability (Score),Profit Margin (%),Land Used (hectares),Crop Yield (tonnes per hectare)
Old MacDonald's,8,20,500,4
Green Pastures,7,25,300,5
Sunny Fields,9,18,400,3.5
Orchard Bloom,6,27,250,4.2
Harvest Grove,10,22,350,3.8
Rural Acres,8.5,30,200,4.5"""
data = data.split("\n")
data = [i.split(",") for i in data]
data = pd.DataFrame(data[1:], columns=data[0])
data_labels = data.columns[1:]
line_labels = [str(i) + " " + str(j) for i, j in zip(data[data.columns[0]], data[data.columns[2]] )]
data = data.to_numpy()[:, 1:].astype(float)

norm = plt.Normalize(data[:, 3].min(), data[:, 3].max())
cmap = get_cmap("viridis")

fig, ax = plt.subplots(figsize=(10, 10))

for i in range(len(data)):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], label=None,
                     color=color, 
                     s=600 + 4400*(data[i, 2]/data[i, 2].max()), alpha=0.6, edgecolors='w')
    ax.scatter([], [], color=color, alpha=1, label=line_labels[i])

ax.legend(title=data_labels[2], loc='upper left')

colorbar = plt.colorbar(scatter)
colorbar.set_label(data_labels[3])

plt.title('Sustainability and Productivity in Different Farms - Agriculture 2023', wrap=True, fontsize=12)
plt.xlabel('Sustainability (Score)', fontsize=10)
plt.ylabel('Profit Margin (%)', fontsize=10)

plt.tight_layout()

plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/95_202312301731.png', dpi=300)
plt.show()

plt.clf()
