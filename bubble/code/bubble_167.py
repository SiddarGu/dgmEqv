import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

data_string = "Vehicle Type,Transportation Volume (Million Tonnes),Fuel Efficiency (Miles per Gallon),Economic Impact (Billion $),Environmental Impact (Score)\n Trucks,3000,6,550,40\n Rail,1500,400,300,80\n Ships,5000,15,750,60\n Airplanes,500,1,200,20\n Pipelines,2000,0,400,90"

temp_data = np.array([i.split(",") for i in data_string.split("\n")])
data_labels = temp_data[0, 1:]
data = temp_data[1:, 1:].astype(float)
line_labels = ["{} {:.0f}".format(i, j) for i, j in zip(temp_data[1:, 0], data[:, 2])]

fig, ax = plt.subplots(figsize=(15, 10))
sc = ax.scatter(data[:, 0], data[:, 1], s=(data[:, 2]-data[:, 2].min())/(data[:, 2].max()-data[:, 2].min())*4400+600, c=(data[:, 3]-data[:, 3].min())/(data[:, 3].max()-data[:, 3].min()), cmap="Blues", label=None)
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c="k", alpha=0.3, s=20, label=line_label)

ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_xlabel(data_labels[0], fontsize=12, wrap=True)
ax.set_ylabel(data_labels[1], fontsize=12, wrap=True)
ax.legend(title=data_labels[2], loc='upper left')

cbar = plt.colorbar(sc, ax=ax)
cbar.set_label(label=data_labels[3], size='x-large')

fig.tight_layout()
plt.title('Economic and Environmental Impact of Various Vehicle Types in Transportation and Logistics', fontsize=16)
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/189_202312310045.png")
plt.clf()
