import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_text = "Disease,Patients (Millions),Life Expectancy (Years),Healthcare Cost per patient ($),Quality of Life (Score)\\n\
Heart Disease,26.6,79,5000,6\\n\
Stroke,6.2,78,4500,7\\n\
Diabetes,34.2,76,4000,5\\n\
Cancer,18.1,72,6000,5\\n\
Alzheimer's,5.8,70,7000,4\\n\
HIV/AIDS,1.2,80,5500,6"

data_lines = data_text.split("\\n")
data_labels = data_lines[0].split(",")[1:]
data = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)
line_labels = [f"{line.split(',')[0]} {data[i, 2]}" for i, line in enumerate(data_lines[1:])]

fig, ax = plt.subplots(figsize=(14, 8))
cmap = plt.get_cmap("viridis")
norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
sm = cm.ScalarMappable(norm=norm, cmap=cmap)

for i in range(len(line_labels)):
    ax.scatter(data[i, 0], data[i, 1], 
               s=(data[i, 2] - np.min(data[:, 2]))/(np.max(data[:, 2]) - np.min(data[:, 2])) * 4400 + 600, 
               c=cmap(norm(data[i, 3])), 
               label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), label=line_labels[i])

ax.grid(True)
plt.colorbar(sm, ax=ax, label=data_labels[3])
ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Impact of Various Diseases on Healthcare Costs and Quality of life')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/132_202312301731.png')
plt.clf()
