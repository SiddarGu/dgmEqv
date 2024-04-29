import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

text = "Energy Source,Production Capacity (GW),Consumption (Million MWh),Carbon Emission (Million Tonnes),Efficiency (%)\n Coal,2000,9000,3000,40\n Gas,1800,8300,2000,55\n Hydro,1000,4000,0,90\n Nuclear,700,3300,0,92\n Wind,500,2200,0,85\n Solar,300,1200,0,90\n Biomass,200,900,200,70"
lines = text.split("\n")
data_labels = lines[0].split(",")
line_labels = [line.split(",")[0] + line.split(",")[2] for line in lines[1:]] 
data = np.array([line.split(",")[1:] for line in lines[1:]], dtype=float)

fig, ax = plt.subplots(figsize=(12, 8))

sizes = 600 + (data[:, 2] - data[:, 2].min()) * (4000 / (data[:, 2].max() - data[:, 2].min()))
norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
colors = plt.cm.viridis(norm(data[:, 3]))

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], c=[colors[i]], s=sizes[i], alpha=0.5, edgecolors='w', label=None)
    ax.scatter([], [], c=colors[i], s=20, label=line_labels[i])
    
ax.legend(title=data_labels[2],loc="upper left")  
ax.grid(True, linestyle='-', color='0.75')

sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title("Comparison of Different Energy Sources in Terms of Production, Consumption, and Efficiency")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/93_202312301731.png")
plt.clf()
