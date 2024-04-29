import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from matplotlib import lines
import numpy as np

data = """
Disease,Global Prevalence (Millions),Annual Deaths (Millions),R&D Funding (Billion $),Quality of Life Impact (Score)
Heart Disease,120,17.9,50,40
Cancer,80,8.8,150,35
Diabetes,45,1.6,30,30
Alzheimer's,50,2,10,25
HIV/AIDS,38,0.69,20,20
Tuberculosis,10,1.4,5,15
Malaria,210,0.41,3,10
"""

data = [row.split(',') for row in data.split('\n') if row]
data_labels = data[0][1:]
line_labels = [row[0] for row in data[1:]]
data = np.array([list(map(float, row[1:])) for row in data[1:]])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
colormap = cm.get_cmap('viridis')

sizes = 600 + 4400 * (data[:,2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min())
norm = colors.Normalize(data[:,3].min(), data[:,3].max())
colors = colormap(norm(data[:,3]))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], color=colors[i], s=sizes[i], alpha=0.6, edgecolors='w', linewidths=2, label=None)
    ax.scatter([], [], color=colors[i], s=20, label=f"{line_label} {data[i, 2]}")

ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2])

mappable = cm.ScalarMappable(norm=norm, cmap=colormap)
cbar = plt.colorbar(mappable)
cbar.set_label(data_labels[3])

plt.title("Prevalence, Death Rates, R&D Funding, and Life Impact of Major Diseases")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/203_202312310045.png")
plt.clf()
