import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

# Transform the data
raw_data = """Vehicle Type,Transport Volume (Million Tonnes),Maintenance Cost ($ Billion),Fuel Efficiency (Miles/Gallon),Safety (Score)
Trucks,6700,25,12,8
Trains,3800,15,90,9
Planes,2800,30,0.45,7
Ships,9400,20,0.10,7
Pipelines,2000,5,0,10"""

df = pd.read_csv(StringIO(raw_data))

data_labels = df.columns[1:].tolist()
line_labels = (df[df.columns[0]] + ' ' + df[df.columns[3]].astype(str)).tolist()
data = df[df.columns[1:]].values

# Create a color map 
cmap = get_cmap("viridis")
norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))

# Create figure and plot
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], 
               s=600 + 4400 * (data[i, 2] / np.max(data[:, 2])), 
               c=cmap(norm(data[i, 3])), 
               label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], color=cmap(norm(data[i, 3])), label=line_label)

ax.legend(title=data_labels[2])
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.title('Analysis of Different Modes of Transportation and Their Efficiency 2023')

# Add a color bar
colorbar_ax = fig.add_axes([0.93, 0.1, 0.02, 0.8])
cb = ColorbarBase(colorbar_ax, cmap="viridis", norm=norm, orientation='vertical')
cb.set_label(data_labels[3])

plt.tight_layout(rect=[0, 0, .9, 1])   
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/175_202312310045.png')
plt.clf()
