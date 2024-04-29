import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# data from the given input
data = np.array([
    [350, 75, 20, 8],
    [280, 60, 15, 9],
    [230, 45, 18, 7],
    [200, 55, 12, 9],
    [120, 40, 22, 10],
    [300, 70, 15, 8],
    [180, 50, 17, 7]
])
data_labels = ["Donation Raised (Million $)","Number of Beneficiaries (Thousands)","Operational Cost (% of Donation)","Public Awareness (Score)"]
line_labels = ["Red Cross","United Way","Doctors Without Borders","Save the Children","World Wildlife Fund","UNICEF","Oxfam"]
line_labels = [label + ' ' + str(data[i, 2]) for i, label in enumerate(line_labels)]

fig, ax = plt.subplots(figsize=(10,10)) 
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")

for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

ax.legend(title=data_labels[2], loc="upper left")
plt.title("Nonprofit Organizations' Impact and Operational Efficiency in 2023", fontsize=18, fontweight='bold')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/222_202312310045.png')
plt.clf()
