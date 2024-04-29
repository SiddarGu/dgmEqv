import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_str = "Country,C02 Emissions (Million Tonnes),Renewable Energy Investment (Billion $),Deforestation (Million Hectares),Air Quality Index (Score)/n USA,5000,300,20,75/n China,10000,350,30,60/n Brazil,2000,150,50,80/n India,3000,200,40,70/n Germany,1500,250,10,85/n Canada,1000,175,15,80"
data_str = data_str.split("/n")
data_labels = data_str[0].split(',')
data_str = data_str[1:]

data = np.zeros((len(data_str), len(data_labels)-1))
line_labels = []
for i, line in enumerate(data_str):
    elements = line.split(',')
    line_labels.append(elements[0] + str(int(elements[2])))
    data[i] = list(map(float, elements[1:]))

color = [data[i, 3] for i in range(len(data))]
size = [data[i, 2] for i in range(len(data))]

fig, ax = plt.subplots(figsize=(np.clip(len(line_labels), 16, 16), 8))

cmap = get_cmap('viridis')
norm = Normalize(vmin=min(color), vmax=max(color))
sizes = np.abs(data[:, 2])/max(np.abs(data[:, 2])) * 5000 + 600

sc = ax.scatter(
    data[:, 0], data[:, 1],
    c=color, s=sizes, 
    cmap=cmap, norm=norm, 
    alpha=0.6, edgecolors='w', linewidths=0.2,
    label=None
)

for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c=cmap(norm(color[i])), alpha=0.6, s=20, label=line_label)

ax.set_xlabel(data_labels[1].replace(' ', '\n'))
ax.set_ylabel(data_labels[2].replace(' ', '\n'))
plt.title('Evaluating Environment and Sustainability through CO2 Emissions and Renewable Energy Investments')

plt.grid(True)

lgnd = ax.legend(title=data_labels[2], loc='upper left', fontsize=10)
for handle in lgnd.legendHandles:
    handle.set_sizes([20])

colorbar = plt.colorbar(sc)
colorbar.set_label(data_labels[3])

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/204_202312310045.png')
plt.clf()
