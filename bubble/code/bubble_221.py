import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

lines = """Energy Source,Production (Million MWh),Consumption (Million MWh),Cost per MWh ($),CO2 Emission (Metric Tonnes)
Natural Gas,2000,1950,50,1200
Coal,1500,1700,45,2000
Nuclear,1000,950,70,10
Hydropower,800,790,75,5
Wind,750,700,80,0
Solar,500,480,105,0
Biomass,250,240,110,600""".split("\n")

# parse the data
data_labels = lines[0].split(",")
raw_data = [l.split(",") for l in lines[1:]]
line_labels = [f"{d[0]} ({d[2]})" for d in raw_data]
data = np.array([[float(v) for v in d[1:]] for d in raw_data])

# create the figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# calculate sizes for scatter
sizes = Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())(data[:,2])
sizes = sizes * (5000-600) + 600

# calculate colors for scatter
colors = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())(data[:,3])
cmap = get_cmap("viridis")

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], c=[cmap(colors[i])], label=None)
    ax.scatter([], [], c=[cmap(colors[i])], s=20, label=line_labels[i])

# add title and labels
ax.set_title("Analysis of Energy Production and Consumption by Source in the Utilities Industry")
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

# plot legend
leg = ax.legend(title=data_labels[2], loc="upper left", fontsize='small')
plt.grid(True)

# plot colorbar
scalarmappable = plt.cm.ScalarMappable(norm=Normalize(vmin=data[:,3].min(), vmax=data[:,3].max()), cmap=cmap)
cbar = plt.colorbar(scalarmappable, ax=ax)
cbar.set_label(data_labels[3])

# save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/174_202312310045.png")

# clear
plt.clf()
